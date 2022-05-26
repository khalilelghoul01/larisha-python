from ast import match_case
from inspect import Parameter
from multiprocessing.dummy import Condition
import sys
from antlr4 import *
from more_itertools import exactly_n
from dist.LarishaLexer import LarishaLexer
from dist.LarishaParser import LarishaParser
from dist.LarishaVisitor import LarishaVisitor
from utils import common
from utils import operation
from includes import methods

##########################
# Global variables
##########################

variables = {}

functions = {}

functionsExport = {}

##########################
# Helper functions
##########################



##########################
# Main
##########################

def get_username():
    from pwd import getpwuid
    from os import getuid
    return getpwuid(getuid())[0]


class MyVisitor(LarishaVisitor):
    def __init__(self):
        pass

    def visitAssignment(self, ctx: LarishaParser.AssignmentContext):
        name = ctx.IDENTIFIER().getText()
        value = self.visit(ctx.expression())
        print(f"{name} = {value}")
        variables[name] = value
        return value

    def visitConstantExpression(self, ctx: LarishaParser.ConstantExpressionContext):
        value = common.parse(ctx.getText())
        return value

    def visitIdentifierExpression(self, ctx: LarishaParser.IdentifierExpressionContext):
        name = ctx.IDENTIFIER().getText()
        value = variables.get(name, None)
        if value is None:
            common.error(f"Variable {name} is not defined")
        return value

    def visitParenthesizedExpression(self, ctx: LarishaParser.ParenthesizedExpressionContext):
        return self.visit(ctx.expression())

    def visitMultiplicativeExpression(self, ctx: LarishaParser.MultiplicativeExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.multOp().getText()
        match op:
            case '*':
                return operation.mult(left, right)
            case '/':
                return operation.div(left, right)
            case '%':
                return operation.mod(left, right)
            case _:
                common.error(f"Unknown operator {op}")

    def visitAdditiveExpression(self, ctx: LarishaParser.AdditiveExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.addOp().getText()
        match op:
            case '+':
                return operation.add(left, right)
            case '-':
                return operation.sub(left, right)
            case _:
                common.error(f"Unknown operator {op}")

    def visitComparativeExpression(self, ctx: LarishaParser.ComparativeExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.compreOp().getText()
        match op:
            case '<':
                return operation.lt(left, right)
            case '>':
                return operation.gt(left, right)
            case '<=':
                return operation.le(left, right)
            case '>=':
                return operation.ge(left, right)
            case '==':
                return operation.eq(left, right)
            case '!=':
                return operation.ne(left, right)
            case _:
                common.error(f"Unknown operator {op}")

    def visitBooleanExpression(self, ctx: LarishaParser.BooleanExpressionContext):
        left = self.visit(ctx.expression(0))
        right = self.visit(ctx.expression(1))
        op = ctx.boolOp().getText()
        match op:
            case '&&':
                return operation.and_(left, right)
            case '||':
                return operation.or_(left, right)
            case _:
                common.error(f"Unknown operator {op}")

    def visitIfBlock(self, ctx: LarishaParser.IfBlockContext):
        condition = self.visit(ctx.expression())
        elseifblock = ctx.elseIfBlock()
        if condition:
            ret = self.visit(ctx.block())
            if isinstance(ret, common.breakpoint):
                return ret
            if isinstance(ret, common.returnpoint):
                return ret
        else:
            if(elseifblock):
                ret = self.visit(ctx.elseIfBlock())
                if isinstance(ret, common.breakpoint):
                    return ret
                if isinstance(ret, common.returnpoint):
                    return ret

    def visitWhileBlock(self, ctx: LarishaParser.WhileBlockContext):
        condition = self.visit(ctx.expression())
        while condition:
            ret = self.visit(ctx.block())
            if isinstance(ret, common.breakpoint):
                break
            if isinstance(ret, common.returnpoint):
                return ret
            condition = self.visit(ctx.expression())

    def visitBlock(self, ctx: LarishaParser.BlockContext):
        for line in ctx.line():
            ret = self.visit(line)
            if isinstance(ret, common.breakpoint):
                break
            if isinstance(ret, common.returnpoint):
                return ret

    

    def visitFunctionDefinition(self, ctx: LarishaParser.FunctionDefinitionContext):
        functionName = ctx.IDENTIFIER().getText()
        argsBase = ctx.parameters()
        args = []
        if(argsBase):
            args = argsBase.IDENTIFIER()
            args = [arg.getText() for arg in args]
        body = ctx.block()
        if(functionName in functions):
            common.error(f"Function {functionName} is already defined")
        function = {
            "name": functionName,
            "args": args,
            "body": body
        }
        functions[functionName] = function

    def visitFunctionCall(self, ctx: LarishaParser.FunctionCallContext):
        return functionCallHandler(self,ctx)
    
    def visitFunctionCallExpression(self, ctx: LarishaParser.FunctionCallExpressionContext):
        return super().visitFunctionCallExpression(ctx)
    
    def visitExport(self, ctx: LarishaParser.ExportContext):
        name = ctx.IDENTIFIER().getText()
        if(name in functionsExport):
            common.error(f"Function {name} is already exported")
        try:
            exportedFunction = getattr(methods, name)
        except Exception as e:
            common.error(f"Function {name} is not defined")
        print(exportedFunction)
        parameters = ctx.parameters()
        if(parameters):
            parameters = parameters.IDENTIFIER()
            parameters = [param.getText() for param in parameters]
        print(f"Exporting function {name} with parameters {parameters}")











##########################
# Helper functions
##########################

def functionCallHandler(self, ctx: LarishaParser.FunctionCallContext):
    functionName = ctx.IDENTIFIER().getText()
    argsBase = ctx.arguments()
    args = []
    if(argsBase):
        args = argsBase.expression()
        args = [self.visit(arg) for arg in args]
    function = functions.get(functionName, None)
    if function is None:
        common.error(f"Function {functionName} is not defined")
    if len(function["args"]) != len(args):
        expectedArgsLength = len(function["args"])
        actualArgsLength = len(args)
        common.error(f"Function {functionName} expects {expectedArgsLength} arguments, but got {actualArgsLength}")
    functionLocal = {
        "variables": {}
    }
    for i in range(len(function["args"])):
        functionLocal["variables"][function["args"][i]] = args[i]

    print(functionLocal["variables"])

    body = function["body"]
    for line in body.line():
        returnValue =  handleVariables(self, line, functionName,functionLocal)
        if isinstance(returnValue, common.returnpoint):
            returnValue = returnValue.value
            break
    return returnValue

def handleVariables(self, ctx: LarishaParser.LineContext,functionName: str, functionLocal: dict):
    if (ctx.returnStatement()):
        returnValue = handleExpression(self, ctx.returnStatement().expression(), functionName, functionLocal)
        return common.returnpoint(returnValue)
    statement = ctx.statement()
    if(not statement):
        return self.visit(ctx)
    
    assignment = statement.assignment()
    variableName = assignment.IDENTIFIER().getText()
    expression = assignment.expression()
    if(expression):
        value = handleExpression(self, expression, functionName, functionLocal)
        functionLocal["variables"][variableName] = value
    else:
        value = None
    

def handleExpression(self, ctx: LarishaParser.ExpressionContext,functionName: str, functionLocal: dict):
    global valueEL
    valueEL = None
    if(isinstance(ctx, LarishaParser.IdentifierExpressionContext)):
        identifier = ctx.IDENTIFIER()
        variableName = identifier.getText()
        if variableName in functionLocal["variables"]:
            valueEL = functionLocal["variables"][variableName]
        elif variableName in variables:
            valueEL = variables[variableName]
        else:
            common.error(f"Variable {variableName} is not defined")
    elif(isinstance(ctx, LarishaParser.ConstantExpressionContext)):
        valueEL = common.parse(ctx.getText())
    elif(isinstance(ctx, LarishaParser.ParenthesizedExpressionContext)):
        valueEL = handleExpression(self, ctx.expression(),functionName,functionLocal)
    elif(isinstance(ctx, LarishaParser.NotExpressionContext)):
        valueEL = operation.not_(handleExpression(self, ctx.expression(),functionName,functionLocal))
    elif(isinstance(ctx, LarishaParser.MultiplicativeExpressionContext)):
        left = handleExpression(self, ctx.expression(0),functionName,functionLocal)
        right = handleExpression(self, ctx.expression(1),functionName,functionLocal)
        op = ctx.multOp().getText()
        match op:
            case '*':
                valueEL =  operation.mult(left, right)
            case '/':
                valueEL =  operation.div(left, right)
            case '%':
                valueEL =  operation.mod(left, right)
            case _:
                common.error(f"Unknown operator {op}")
    elif(isinstance(ctx, LarishaParser.AdditiveExpressionContext)):
        left = handleExpression(self, ctx.expression(0),functionName,functionLocal)
        right = handleExpression(self, ctx.expression(1),functionName,functionLocal)
        op = ctx.addOp().getText()
        match op:
            case '+':
                valueEL =  operation.add(left, right)
            case '-':
                valueEL =  operation.sub(left, right)
            case _:
                common.error(f"Unknown operator {op}")
    elif(isinstance(ctx, LarishaParser.ComparativeExpressionContext)):
        left = handleExpression(self, ctx.expression(0),functionName,functionLocal)
        right = handleExpression(self, ctx.expression(1),functionName,functionLocal)
        op = ctx.compOp().getText()
        match op:
            case '<':
                valueEL =  operation.lt(left, right)
            case '>':
                valueEL =  operation.gt(left, right)
            case '<=':
                valueEL =  operation.le(left, right)
            case '>=':
                valueEL =  operation.ge(left, right)
            case '==':
                valueEL =  operation.eq(left, right)
            case '!=':
                valueEL =  operation.ne(left, right)
            case _:
                common.error(f"Unknown operator {op}")
    elif(isinstance(ctx, LarishaParser.BooleanExpressionContext)):
        left = handleExpression(self, ctx.expression(0),functionName,functionLocal)
        right = handleExpression(self, ctx.expression(1),functionName,functionLocal)
        op = ctx.boolOp().getText()
        match op:
            case '&&':
                valueEL =  operation.and_(left, right)
            case '||':
                valueEL =  operation.or_(left, right)
            case _:
                common.error(f"Unknown operator {op}")
    elif(isinstance(ctx, LarishaParser.FunctionCallExpressionContext)):
        print("function call")
        print(ctx.functionCall().getText())
        valueEL = functionCallInternal(self, ctx.functionCall(),functionName,functionLocal).value
    return valueEL


def functionCallInternal(self, ctx: LarishaParser.FunctionCallContext, functionName: str, functionLocal: dict):
    functionName = ctx.IDENTIFIER().getText()
    argsBase = ctx.arguments()
    args = []
    print(functionLocal["variables"])
    if(argsBase):
        args = argsBase.expression()
        args = [handleExpression(self,arg,functionName,functionLocal) for arg in args]
    function = functions.get(functionName, None)
    if function is None:
        common.error(f"Function {functionName} is not defined")
    if len(function["args"]) != len(args):
        expectedArgsLength = len(function["args"])
        actualArgsLength = len(args)
        common.error(f"Function {functionName} expects {expectedArgsLength} arguments, but got {actualArgsLength}")
    for i in range(len(function["args"])):
        functionLocal["variables"][function["args"][i]] = args[i]
    body = function["body"]
    for line in body.line():
        returnValue =  handleVariables(self, line, functionName,functionLocal)
    return returnValue












if __name__ == "__main__":
    args = sys.argv[1:]
    if len(args) == 0:
        print("Usage: larisha.py <file>")
        sys.exit(1)
    with open(args[0], "r") as f:
        code = f.read()
    data = InputStream(code)
    # lexer
    lexer = LarishaLexer(data)
    stream = CommonTokenStream(lexer)
    # parser
    parser = LarishaParser(stream)
    tree = parser.program()
    # evaluator
    visitor = MyVisitor()
    output = visitor.visit(tree)
