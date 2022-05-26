from ast import match_case
from multiprocessing.dummy import Condition
import sys
from antlr4 import *
from dist.LarishaLexer import LarishaLexer
from dist.LarishaParser import LarishaParser
from dist.LarishaVisitor import LarishaVisitor
from utils import common
from utils import operation

##########################
# Global variables
##########################

variables = {}

functions = {}
##########################
# Helper functions
##########################

def search_args(function,name):
    if(f"${function}" in variables):
        for arg in variables[f"${function}"]:
            if(arg["name"] == name):
                return arg["value"]
    if(name in variables):
        return variables[name]
    common.error(f"Variable {name} not found")

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
                return ret
            if isinstance(ret, common.returnpoint):
                return ret

    def visitBreak(self, ctx: LarishaParser.BreakContext):
        return common.breakpoint()

    def visitLine(self, ctx: LarishaParser.LineContext):
        if(ctx.returnStatement()):
            return self.visit(ctx.returnStatement())
        if(ctx.break_()):
            return self.visit(ctx.break_())
        return super().visitLine(ctx)

    def visitFunctionDefinition(self, ctx: LarishaParser.FunctionDefinitionContext):
        functionName = ctx.IDENTIFIER().getText()
        argsBase = ctx.parameters()
        args = []
        if(argsBase):
            args = argsBase.IDENTIFIER()
            args = [arg.getText() for arg in args]
        argsObject = []
        for arg in args:
            argObject = {}
            argObject["name"] = arg
            argObject["value"] = None
            argsObject.append(argObject)
        variables[f"${functionName}"] = argsObject
        body = ctx.block()
        if(f"${functionName}" in functions):
            common.error(f"Function {functionName} is already defined")
        function = {
            "name": functionName,
            "args": args,
            "body": body
        }
        functions[functionName] = function

    def visitFunctionCall(self, ctx: LarishaParser.FunctionCallContext):
        functionName = ctx.IDENTIFIER().getText()
        argsBase = ctx.arguments()
        args = []
        if(argsBase):
            args = argsBase.expression()
            args = [self.visit(arg) for arg in args]
        if(functionName not in functions):
            common.error(f"Function {functionName} is not defined")
        if(len(args) != len(functions[functionName]["args"])):
            common.error(
                f"Function {functionName} expects {len(functions[functionName]['args'])} arguments, but got {len(args)}")
        # returnValue = self.visit(functions[functionName]["body"])
        body = functions[functionName]["body"]
        for index,arg in enumerate(args):
            var = variables[f"${functionName}"][index]
            variables[f"${functionName}"][index]["value"] = arg
        for line in body.line():
            if(line.statement()):
                if(line.statement().assignment()):
                    assignment = line.statement().assignment()
                    variable_name = assignment.IDENTIFIER().getText()
                    if(assignment.expression()):
                        expression = assignment.expression()
                        if(expression.IDENTIFIER()):
                            variables[variable_name] = search_args(functionName,expression.IDENTIFIER().getText())
                        else:
                            variables[variable_name] = self.visit(expression)
            else:
                returnValue = self.visit(line)
                if isinstance(returnValue, common.breakpoint):
                    return returnValue
                if isinstance(returnValue, common.returnpoint):
                    return returnValue
        return returnValue.getValue() if isinstance(returnValue, common.returnpoint) else returnValue

    def visitFunctionCallExpression(self, ctx: LarishaParser.FunctionCallExpressionContext):
        returnValue = self.visit(ctx.functionCall())
        return returnValue.getValue() if isinstance(returnValue, common.returnpoint) else returnValue

    def visitReturnStatement(self, ctx: LarishaParser.ReturnStatementContext):
        value = common.returnpoint(self.visit(ctx.expression()))
        return value

    


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
