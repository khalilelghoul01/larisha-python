# Generated from grammar/Larisha.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .LarishaParser import LarishaParser
else:
    from LarishaParser import LarishaParser

# This class defines a complete generic visitor for a parse tree produced by LarishaParser.

class LarishaVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by LarishaParser#program.
    def visitProgram(self, ctx:LarishaParser.ProgramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#line.
    def visitLine(self, ctx:LarishaParser.LineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#statement.
    def visitStatement(self, ctx:LarishaParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#assignment.
    def visitAssignment(self, ctx:LarishaParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#ifBlock.
    def visitIfBlock(self, ctx:LarishaParser.IfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#elseIfBlock.
    def visitElseIfBlock(self, ctx:LarishaParser.ElseIfBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#whileBlock.
    def visitWhileBlock(self, ctx:LarishaParser.WhileBlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#functionDefinition.
    def visitFunctionDefinition(self, ctx:LarishaParser.FunctionDefinitionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#functionCall.
    def visitFunctionCall(self, ctx:LarishaParser.FunctionCallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#arguments.
    def visitArguments(self, ctx:LarishaParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#parameters.
    def visitParameters(self, ctx:LarishaParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#comparativeExpression.
    def visitComparativeExpression(self, ctx:LarishaParser.ComparativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#parenthesizedExpression.
    def visitParenthesizedExpression(self, ctx:LarishaParser.ParenthesizedExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#negativeExpression.
    def visitNegativeExpression(self, ctx:LarishaParser.NegativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#constantExpression.
    def visitConstantExpression(self, ctx:LarishaParser.ConstantExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#additiveExpression.
    def visitAdditiveExpression(self, ctx:LarishaParser.AdditiveExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#identifierExpression.
    def visitIdentifierExpression(self, ctx:LarishaParser.IdentifierExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#functionCallExpression.
    def visitFunctionCallExpression(self, ctx:LarishaParser.FunctionCallExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#notExpression.
    def visitNotExpression(self, ctx:LarishaParser.NotExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#multiplicativeExpression.
    def visitMultiplicativeExpression(self, ctx:LarishaParser.MultiplicativeExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#booleanExpression.
    def visitBooleanExpression(self, ctx:LarishaParser.BooleanExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#multOp.
    def visitMultOp(self, ctx:LarishaParser.MultOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#addOp.
    def visitAddOp(self, ctx:LarishaParser.AddOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#compreOp.
    def visitCompreOp(self, ctx:LarishaParser.CompreOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#boolOp.
    def visitBoolOp(self, ctx:LarishaParser.BoolOpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#constant.
    def visitConstant(self, ctx:LarishaParser.ConstantContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#block.
    def visitBlock(self, ctx:LarishaParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#break.
    def visitBreak(self, ctx:LarishaParser.BreakContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by LarishaParser#returnStatement.
    def visitReturnStatement(self, ctx:LarishaParser.ReturnStatementContext):
        return self.visitChildren(ctx)



del LarishaParser