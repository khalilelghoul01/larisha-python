# Generated from grammar/Larisha.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LarishaParser import LarishaParser
else:
    from LarishaParser import LarishaParser

# This class defines a complete listener for a parse tree produced by LarishaParser.
class LarishaListener(ParseTreeListener):

    # Enter a parse tree produced by LarishaParser#program.
    def enterProgram(self, ctx:LarishaParser.ProgramContext):
        pass

    # Exit a parse tree produced by LarishaParser#program.
    def exitProgram(self, ctx:LarishaParser.ProgramContext):
        pass


    # Enter a parse tree produced by LarishaParser#line.
    def enterLine(self, ctx:LarishaParser.LineContext):
        pass

    # Exit a parse tree produced by LarishaParser#line.
    def exitLine(self, ctx:LarishaParser.LineContext):
        pass


    # Enter a parse tree produced by LarishaParser#statement.
    def enterStatement(self, ctx:LarishaParser.StatementContext):
        pass

    # Exit a parse tree produced by LarishaParser#statement.
    def exitStatement(self, ctx:LarishaParser.StatementContext):
        pass


    # Enter a parse tree produced by LarishaParser#assignment.
    def enterAssignment(self, ctx:LarishaParser.AssignmentContext):
        pass

    # Exit a parse tree produced by LarishaParser#assignment.
    def exitAssignment(self, ctx:LarishaParser.AssignmentContext):
        pass


    # Enter a parse tree produced by LarishaParser#ifBlock.
    def enterIfBlock(self, ctx:LarishaParser.IfBlockContext):
        pass

    # Exit a parse tree produced by LarishaParser#ifBlock.
    def exitIfBlock(self, ctx:LarishaParser.IfBlockContext):
        pass


    # Enter a parse tree produced by LarishaParser#elseIfBlock.
    def enterElseIfBlock(self, ctx:LarishaParser.ElseIfBlockContext):
        pass

    # Exit a parse tree produced by LarishaParser#elseIfBlock.
    def exitElseIfBlock(self, ctx:LarishaParser.ElseIfBlockContext):
        pass


    # Enter a parse tree produced by LarishaParser#whileBlock.
    def enterWhileBlock(self, ctx:LarishaParser.WhileBlockContext):
        pass

    # Exit a parse tree produced by LarishaParser#whileBlock.
    def exitWhileBlock(self, ctx:LarishaParser.WhileBlockContext):
        pass


    # Enter a parse tree produced by LarishaParser#functionDefinition.
    def enterFunctionDefinition(self, ctx:LarishaParser.FunctionDefinitionContext):
        pass

    # Exit a parse tree produced by LarishaParser#functionDefinition.
    def exitFunctionDefinition(self, ctx:LarishaParser.FunctionDefinitionContext):
        pass


    # Enter a parse tree produced by LarishaParser#functionCall.
    def enterFunctionCall(self, ctx:LarishaParser.FunctionCallContext):
        pass

    # Exit a parse tree produced by LarishaParser#functionCall.
    def exitFunctionCall(self, ctx:LarishaParser.FunctionCallContext):
        pass


    # Enter a parse tree produced by LarishaParser#arguments.
    def enterArguments(self, ctx:LarishaParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by LarishaParser#arguments.
    def exitArguments(self, ctx:LarishaParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by LarishaParser#parameters.
    def enterParameters(self, ctx:LarishaParser.ParametersContext):
        pass

    # Exit a parse tree produced by LarishaParser#parameters.
    def exitParameters(self, ctx:LarishaParser.ParametersContext):
        pass


    # Enter a parse tree produced by LarishaParser#comparativeExpression.
    def enterComparativeExpression(self, ctx:LarishaParser.ComparativeExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#comparativeExpression.
    def exitComparativeExpression(self, ctx:LarishaParser.ComparativeExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#parenthesizedExpression.
    def enterParenthesizedExpression(self, ctx:LarishaParser.ParenthesizedExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#parenthesizedExpression.
    def exitParenthesizedExpression(self, ctx:LarishaParser.ParenthesizedExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#negativeExpression.
    def enterNegativeExpression(self, ctx:LarishaParser.NegativeExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#negativeExpression.
    def exitNegativeExpression(self, ctx:LarishaParser.NegativeExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#constantExpression.
    def enterConstantExpression(self, ctx:LarishaParser.ConstantExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#constantExpression.
    def exitConstantExpression(self, ctx:LarishaParser.ConstantExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#additiveExpression.
    def enterAdditiveExpression(self, ctx:LarishaParser.AdditiveExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#additiveExpression.
    def exitAdditiveExpression(self, ctx:LarishaParser.AdditiveExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#identifierExpression.
    def enterIdentifierExpression(self, ctx:LarishaParser.IdentifierExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#identifierExpression.
    def exitIdentifierExpression(self, ctx:LarishaParser.IdentifierExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#functionCallExpression.
    def enterFunctionCallExpression(self, ctx:LarishaParser.FunctionCallExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#functionCallExpression.
    def exitFunctionCallExpression(self, ctx:LarishaParser.FunctionCallExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#notExpression.
    def enterNotExpression(self, ctx:LarishaParser.NotExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#notExpression.
    def exitNotExpression(self, ctx:LarishaParser.NotExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#multiplicativeExpression.
    def enterMultiplicativeExpression(self, ctx:LarishaParser.MultiplicativeExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#multiplicativeExpression.
    def exitMultiplicativeExpression(self, ctx:LarishaParser.MultiplicativeExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#booleanExpression.
    def enterBooleanExpression(self, ctx:LarishaParser.BooleanExpressionContext):
        pass

    # Exit a parse tree produced by LarishaParser#booleanExpression.
    def exitBooleanExpression(self, ctx:LarishaParser.BooleanExpressionContext):
        pass


    # Enter a parse tree produced by LarishaParser#multOp.
    def enterMultOp(self, ctx:LarishaParser.MultOpContext):
        pass

    # Exit a parse tree produced by LarishaParser#multOp.
    def exitMultOp(self, ctx:LarishaParser.MultOpContext):
        pass


    # Enter a parse tree produced by LarishaParser#addOp.
    def enterAddOp(self, ctx:LarishaParser.AddOpContext):
        pass

    # Exit a parse tree produced by LarishaParser#addOp.
    def exitAddOp(self, ctx:LarishaParser.AddOpContext):
        pass


    # Enter a parse tree produced by LarishaParser#compreOp.
    def enterCompreOp(self, ctx:LarishaParser.CompreOpContext):
        pass

    # Exit a parse tree produced by LarishaParser#compreOp.
    def exitCompreOp(self, ctx:LarishaParser.CompreOpContext):
        pass


    # Enter a parse tree produced by LarishaParser#boolOp.
    def enterBoolOp(self, ctx:LarishaParser.BoolOpContext):
        pass

    # Exit a parse tree produced by LarishaParser#boolOp.
    def exitBoolOp(self, ctx:LarishaParser.BoolOpContext):
        pass


    # Enter a parse tree produced by LarishaParser#constant.
    def enterConstant(self, ctx:LarishaParser.ConstantContext):
        pass

    # Exit a parse tree produced by LarishaParser#constant.
    def exitConstant(self, ctx:LarishaParser.ConstantContext):
        pass


    # Enter a parse tree produced by LarishaParser#block.
    def enterBlock(self, ctx:LarishaParser.BlockContext):
        pass

    # Exit a parse tree produced by LarishaParser#block.
    def exitBlock(self, ctx:LarishaParser.BlockContext):
        pass


    # Enter a parse tree produced by LarishaParser#break.
    def enterBreak(self, ctx:LarishaParser.BreakContext):
        pass

    # Exit a parse tree produced by LarishaParser#break.
    def exitBreak(self, ctx:LarishaParser.BreakContext):
        pass


    # Enter a parse tree produced by LarishaParser#returnStatement.
    def enterReturnStatement(self, ctx:LarishaParser.ReturnStatementContext):
        pass

    # Exit a parse tree produced by LarishaParser#returnStatement.
    def exitReturnStatement(self, ctx:LarishaParser.ReturnStatementContext):
        pass



del LarishaParser