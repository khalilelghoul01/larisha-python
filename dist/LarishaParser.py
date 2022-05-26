# Generated from grammar/Larisha.g4 by ANTLR 4.10.1
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO

def serializedATN():
    return [
        4,1,36,188,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,1,0,
        5,0,42,8,0,10,0,12,0,45,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,3,1,62,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,
        4,1,4,1,4,1,4,1,4,1,4,3,4,77,8,4,1,4,1,4,1,4,1,4,1,5,1,5,3,5,85,
        8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,93,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,
        7,101,8,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,109,8,8,1,8,1,8,1,9,1,9,1,
        9,5,9,116,8,9,10,9,12,9,119,9,9,1,10,1,10,1,10,5,10,124,8,10,10,
        10,12,10,127,9,10,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,3,11,141,8,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,
        11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,1,11,5,11,159,8,11,10,11,12,
        11,162,9,11,1,12,1,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,
        17,1,17,5,17,176,8,17,10,17,12,17,179,9,17,1,17,1,17,1,18,1,18,1,
        19,1,19,1,19,1,19,0,1,22,20,0,2,4,6,8,10,12,14,16,18,20,22,24,26,
        28,30,32,34,36,38,0,5,1,0,10,12,2,0,9,9,13,13,1,0,14,19,1,0,20,21,
        1,0,28,32,191,0,43,1,0,0,0,2,61,1,0,0,0,4,63,1,0,0,0,6,66,1,0,0,
        0,8,70,1,0,0,0,10,84,1,0,0,0,12,86,1,0,0,0,14,96,1,0,0,0,16,105,
        1,0,0,0,18,112,1,0,0,0,20,120,1,0,0,0,22,140,1,0,0,0,24,163,1,0,
        0,0,26,165,1,0,0,0,28,167,1,0,0,0,30,169,1,0,0,0,32,171,1,0,0,0,
        34,173,1,0,0,0,36,182,1,0,0,0,38,184,1,0,0,0,40,42,3,2,1,0,41,40,
        1,0,0,0,42,45,1,0,0,0,43,41,1,0,0,0,43,44,1,0,0,0,44,46,1,0,0,0,
        45,43,1,0,0,0,46,47,5,0,0,1,47,1,1,0,0,0,48,62,3,4,2,0,49,62,3,8,
        4,0,50,62,3,12,6,0,51,52,3,36,18,0,52,53,5,1,0,0,53,62,1,0,0,0,54,
        62,3,14,7,0,55,56,3,16,8,0,56,57,5,1,0,0,57,62,1,0,0,0,58,59,3,38,
        19,0,59,60,5,1,0,0,60,62,1,0,0,0,61,48,1,0,0,0,61,49,1,0,0,0,61,
        50,1,0,0,0,61,51,1,0,0,0,61,54,1,0,0,0,61,55,1,0,0,0,61,58,1,0,0,
        0,62,3,1,0,0,0,63,64,3,6,3,0,64,65,5,1,0,0,65,5,1,0,0,0,66,67,5,
        36,0,0,67,68,5,2,0,0,68,69,3,22,11,0,69,7,1,0,0,0,70,76,5,3,0,0,
        71,72,5,4,0,0,72,73,3,22,11,0,73,74,5,5,0,0,74,77,1,0,0,0,75,77,
        3,22,11,0,76,71,1,0,0,0,76,75,1,0,0,0,77,78,1,0,0,0,78,79,3,34,17,
        0,79,80,5,6,0,0,80,81,3,10,5,0,81,9,1,0,0,0,82,85,3,8,4,0,83,85,
        3,34,17,0,84,82,1,0,0,0,84,83,1,0,0,0,85,11,1,0,0,0,86,92,5,26,0,
        0,87,88,5,4,0,0,88,89,3,22,11,0,89,90,5,5,0,0,90,93,1,0,0,0,91,93,
        3,22,11,0,92,87,1,0,0,0,92,91,1,0,0,0,93,94,1,0,0,0,94,95,3,34,17,
        0,95,13,1,0,0,0,96,97,5,27,0,0,97,98,5,36,0,0,98,100,5,4,0,0,99,
        101,3,20,10,0,100,99,1,0,0,0,100,101,1,0,0,0,101,102,1,0,0,0,102,
        103,5,5,0,0,103,104,3,34,17,0,104,15,1,0,0,0,105,106,5,36,0,0,106,
        108,5,4,0,0,107,109,3,18,9,0,108,107,1,0,0,0,108,109,1,0,0,0,109,
        110,1,0,0,0,110,111,5,5,0,0,111,17,1,0,0,0,112,117,3,22,11,0,113,
        114,5,7,0,0,114,116,3,22,11,0,115,113,1,0,0,0,116,119,1,0,0,0,117,
        115,1,0,0,0,117,118,1,0,0,0,118,19,1,0,0,0,119,117,1,0,0,0,120,125,
        5,36,0,0,121,122,5,7,0,0,122,124,5,36,0,0,123,121,1,0,0,0,124,127,
        1,0,0,0,125,123,1,0,0,0,125,126,1,0,0,0,126,21,1,0,0,0,127,125,1,
        0,0,0,128,129,6,11,-1,0,129,141,3,32,16,0,130,141,5,36,0,0,131,132,
        5,4,0,0,132,133,3,22,11,0,133,134,5,5,0,0,134,141,1,0,0,0,135,136,
        5,8,0,0,136,141,3,22,11,7,137,138,5,9,0,0,138,141,3,22,11,6,139,
        141,3,16,8,0,140,128,1,0,0,0,140,130,1,0,0,0,140,131,1,0,0,0,140,
        135,1,0,0,0,140,137,1,0,0,0,140,139,1,0,0,0,141,160,1,0,0,0,142,
        143,10,5,0,0,143,144,3,24,12,0,144,145,3,22,11,6,145,159,1,0,0,0,
        146,147,10,4,0,0,147,148,3,26,13,0,148,149,3,22,11,5,149,159,1,0,
        0,0,150,151,10,3,0,0,151,152,3,28,14,0,152,153,3,22,11,4,153,159,
        1,0,0,0,154,155,10,2,0,0,155,156,3,30,15,0,156,157,3,22,11,3,157,
        159,1,0,0,0,158,142,1,0,0,0,158,146,1,0,0,0,158,150,1,0,0,0,158,
        154,1,0,0,0,159,162,1,0,0,0,160,158,1,0,0,0,160,161,1,0,0,0,161,
        23,1,0,0,0,162,160,1,0,0,0,163,164,7,0,0,0,164,25,1,0,0,0,165,166,
        7,1,0,0,166,27,1,0,0,0,167,168,7,2,0,0,168,29,1,0,0,0,169,170,7,
        3,0,0,170,31,1,0,0,0,171,172,7,4,0,0,172,33,1,0,0,0,173,177,5,22,
        0,0,174,176,3,2,1,0,175,174,1,0,0,0,176,179,1,0,0,0,177,175,1,0,
        0,0,177,178,1,0,0,0,178,180,1,0,0,0,179,177,1,0,0,0,180,181,5,23,
        0,0,181,35,1,0,0,0,182,183,5,24,0,0,183,37,1,0,0,0,184,185,5,25,
        0,0,185,186,3,22,11,0,186,39,1,0,0,0,13,43,61,76,84,92,100,108,117,
        125,140,158,160,177
    ]

class LarishaParser ( Parser ):

    grammarFileName = "Larisha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'if'", "'('", "')'", "'else'", 
                     "','", "'!'", "'-'", "'*'", "'/'", "'%'", "'+'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'{'", "'}'", "'break'", "'return'", "'while'", "'fun'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WHILE", "FUNCTION", "BOOL", 
                      "STRING", "FLOAT", "INTEGER", "CHAR", "WS", "COMMENT", 
                      "LINE_COMMENT", "IDENTIFIER" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_ifBlock = 4
    RULE_elseIfBlock = 5
    RULE_whileBlock = 6
    RULE_functionDefinition = 7
    RULE_functionCall = 8
    RULE_arguments = 9
    RULE_parameters = 10
    RULE_expression = 11
    RULE_multOp = 12
    RULE_addOp = 13
    RULE_compreOp = 14
    RULE_boolOp = 15
    RULE_constant = 16
    RULE_block = 17
    RULE_break = 18
    RULE_returnStatement = 19

    ruleNames =  [ "program", "line", "statement", "assignment", "ifBlock", 
                   "elseIfBlock", "whileBlock", "functionDefinition", "functionCall", 
                   "arguments", "parameters", "expression", "multOp", "addOp", 
                   "compreOp", "boolOp", "constant", "block", "break", "returnStatement" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    T__7=8
    T__8=9
    T__9=10
    T__10=11
    T__11=12
    T__12=13
    T__13=14
    T__14=15
    T__15=16
    T__16=17
    T__17=18
    T__18=19
    T__19=20
    T__20=21
    T__21=22
    T__22=23
    T__23=24
    T__24=25
    WHILE=26
    FUNCTION=27
    BOOL=28
    STRING=29
    FLOAT=30
    INTEGER=31
    CHAR=32
    WS=33
    COMMENT=34
    LINE_COMMENT=35
    IDENTIFIER=36

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.10.1")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class ProgramContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(LarishaParser.EOF, 0)

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.LineContext)
            else:
                return self.getTypedRuleContext(LarishaParser.LineContext,i)


        def getRuleIndex(self):
            return LarishaParser.RULE_program

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterProgram" ):
                listener.enterProgram(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitProgram" ):
                listener.exitProgram(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitProgram" ):
                return visitor.visitProgram(self)
            else:
                return visitor.visitChildren(self)




    def program(self):

        localctx = LarishaParser.ProgramContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_program)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 43
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__23) | (1 << LarishaParser.T__24) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 40
                self.line()
                self.state = 45
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 46
            self.match(LarishaParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class LineContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def statement(self):
            return self.getTypedRuleContext(LarishaParser.StatementContext,0)


        def ifBlock(self):
            return self.getTypedRuleContext(LarishaParser.IfBlockContext,0)


        def whileBlock(self):
            return self.getTypedRuleContext(LarishaParser.WhileBlockContext,0)


        def break_(self):
            return self.getTypedRuleContext(LarishaParser.BreakContext,0)


        def functionDefinition(self):
            return self.getTypedRuleContext(LarishaParser.FunctionDefinitionContext,0)


        def functionCall(self):
            return self.getTypedRuleContext(LarishaParser.FunctionCallContext,0)


        def returnStatement(self):
            return self.getTypedRuleContext(LarishaParser.ReturnStatementContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_line

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLine" ):
                listener.enterLine(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLine" ):
                listener.exitLine(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitLine" ):
                return visitor.visitLine(self)
            else:
                return visitor.visitChildren(self)




    def line(self):

        localctx = LarishaParser.LineContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_line)
        try:
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 48
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 49
                self.ifBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 50
                self.whileBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 51
                self.break_()
                self.state = 52
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 54
                self.functionDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 55
                self.functionCall()
                self.state = 56
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 58
                self.returnStatement()
                self.state = 59
                self.match(LarishaParser.T__0)
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def assignment(self):
            return self.getTypedRuleContext(LarishaParser.AssignmentContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStatement" ):
                listener.enterStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStatement" ):
                listener.exitStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitStatement" ):
                return visitor.visitStatement(self)
            else:
                return visitor.visitChildren(self)




    def statement(self):

        localctx = LarishaParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 63
            self.assignment()
            self.state = 64
            self.match(LarishaParser.T__0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignmentContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_assignment

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssignment" ):
                listener.enterAssignment(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssignment" ):
                listener.exitAssignment(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAssignment" ):
                return visitor.visitAssignment(self)
            else:
                return visitor.visitChildren(self)




    def assignment(self):

        localctx = LarishaParser.AssignmentContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assignment)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 66
            self.match(LarishaParser.IDENTIFIER)
            self.state = 67
            self.match(LarishaParser.T__1)
            self.state = 68
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class IfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(LarishaParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def elseIfBlock(self):
            return self.getTypedRuleContext(LarishaParser.ElseIfBlockContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_ifBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIfBlock" ):
                listener.enterIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIfBlock" ):
                listener.exitIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIfBlock" ):
                return visitor.visitIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def ifBlock(self):

        localctx = LarishaParser.IfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_ifBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 70
            self.match(LarishaParser.T__2)
            self.state = 76
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 71
                self.match(LarishaParser.T__3)
                self.state = 72
                self.expression(0)
                self.state = 73
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 75
                self.expression(0)
                pass


            self.state = 78
            self.block()

            self.state = 79
            self.match(LarishaParser.T__5)
            self.state = 80
            self.elseIfBlock()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ElseIfBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ifBlock(self):
            return self.getTypedRuleContext(LarishaParser.IfBlockContext,0)


        def block(self):
            return self.getTypedRuleContext(LarishaParser.BlockContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_elseIfBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterElseIfBlock" ):
                listener.enterElseIfBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitElseIfBlock" ):
                listener.exitElseIfBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitElseIfBlock" ):
                return visitor.visitElseIfBlock(self)
            else:
                return visitor.visitChildren(self)




    def elseIfBlock(self):

        localctx = LarishaParser.ElseIfBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_elseIfBlock)
        try:
            self.state = 84
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LarishaParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 82
                self.ifBlock()
                pass
            elif token in [LarishaParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 83
                self.block()
                pass
            else:
                raise NoViableAltException(self)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WhileBlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(LarishaParser.WHILE, 0)

        def block(self):
            return self.getTypedRuleContext(LarishaParser.BlockContext,0)


        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_whileBlock

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhileBlock" ):
                listener.enterWhileBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhileBlock" ):
                listener.exitWhileBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitWhileBlock" ):
                return visitor.visitWhileBlock(self)
            else:
                return visitor.visitChildren(self)




    def whileBlock(self):

        localctx = LarishaParser.WhileBlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_whileBlock)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 86
            self.match(LarishaParser.WHILE)
            self.state = 92
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 87
                self.match(LarishaParser.T__3)
                self.state = 88
                self.expression(0)
                self.state = 89
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 91
                self.expression(0)
                pass


            self.state = 94
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionDefinitionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def FUNCTION(self):
            return self.getToken(LarishaParser.FUNCTION, 0)

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def block(self):
            return self.getTypedRuleContext(LarishaParser.BlockContext,0)


        def parameters(self):
            return self.getTypedRuleContext(LarishaParser.ParametersContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_functionDefinition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionDefinition" ):
                listener.enterFunctionDefinition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionDefinition" ):
                listener.exitFunctionDefinition(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionDefinition" ):
                return visitor.visitFunctionDefinition(self)
            else:
                return visitor.visitChildren(self)




    def functionDefinition(self):

        localctx = LarishaParser.FunctionDefinitionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_functionDefinition)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(LarishaParser.FUNCTION)
            self.state = 97
            self.match(LarishaParser.IDENTIFIER)
            self.state = 98
            self.match(LarishaParser.T__3)
            self.state = 100
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.IDENTIFIER:
                self.state = 99
                self.parameters()


            self.state = 102
            self.match(LarishaParser.T__4)
            self.state = 103
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class FunctionCallContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def arguments(self):
            return self.getTypedRuleContext(LarishaParser.ArgumentsContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_functionCall

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCall" ):
                listener.enterFunctionCall(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCall" ):
                listener.exitFunctionCall(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCall" ):
                return visitor.visitFunctionCall(self)
            else:
                return visitor.visitChildren(self)




    def functionCall(self):

        localctx = LarishaParser.FunctionCallContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_functionCall)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 105
            self.match(LarishaParser.IDENTIFIER)
            self.state = 106
            self.match(LarishaParser.T__3)
            self.state = 108
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__3) | (1 << LarishaParser.T__7) | (1 << LarishaParser.T__8) | (1 << LarishaParser.BOOL) | (1 << LarishaParser.STRING) | (1 << LarishaParser.FLOAT) | (1 << LarishaParser.INTEGER) | (1 << LarishaParser.CHAR) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 107
                self.arguments()


            self.state = 110
            self.match(LarishaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ArgumentsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LarishaParser.ExpressionContext,i)


        def getRuleIndex(self):
            return LarishaParser.RULE_arguments

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArguments" ):
                listener.enterArguments(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArguments" ):
                listener.exitArguments(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitArguments" ):
                return visitor.visitArguments(self)
            else:
                return visitor.visitChildren(self)




    def arguments(self):

        localctx = LarishaParser.ArgumentsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.expression(0)
            self.state = 117
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__6:
                self.state = 113
                self.match(LarishaParser.T__6)
                self.state = 114
                self.expression(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ParametersContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IDENTIFIER(self, i:int=None):
            if i is None:
                return self.getTokens(LarishaParser.IDENTIFIER)
            else:
                return self.getToken(LarishaParser.IDENTIFIER, i)

        def getRuleIndex(self):
            return LarishaParser.RULE_parameters

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParameters" ):
                listener.enterParameters(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParameters" ):
                listener.exitParameters(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParameters" ):
                return visitor.visitParameters(self)
            else:
                return visitor.visitChildren(self)




    def parameters(self):

        localctx = LarishaParser.ParametersContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 120
            self.match(LarishaParser.IDENTIFIER)
            self.state = 125
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__6:
                self.state = 121
                self.match(LarishaParser.T__6)
                self.state = 122
                self.match(LarishaParser.IDENTIFIER)
                self.state = 127
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExpressionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class ComparativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LarishaParser.ExpressionContext,i)

        def compreOp(self):
            return self.getTypedRuleContext(LarishaParser.CompreOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterComparativeExpression" ):
                listener.enterComparativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitComparativeExpression" ):
                listener.exitComparativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitComparativeExpression" ):
                return visitor.visitComparativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class ParenthesizedExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterParenthesizedExpression" ):
                listener.enterParenthesizedExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitParenthesizedExpression" ):
                listener.exitParenthesizedExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitParenthesizedExpression" ):
                return visitor.visitParenthesizedExpression(self)
            else:
                return visitor.visitChildren(self)


    class NegativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNegativeExpression" ):
                listener.enterNegativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNegativeExpression" ):
                listener.exitNegativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNegativeExpression" ):
                return visitor.visitNegativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class ConstantExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def constant(self):
            return self.getTypedRuleContext(LarishaParser.ConstantContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstantExpression" ):
                listener.enterConstantExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstantExpression" ):
                listener.exitConstantExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstantExpression" ):
                return visitor.visitConstantExpression(self)
            else:
                return visitor.visitChildren(self)


    class AdditiveExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LarishaParser.ExpressionContext,i)

        def addOp(self):
            return self.getTypedRuleContext(LarishaParser.AddOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpression" ):
                listener.enterAdditiveExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpression" ):
                listener.exitAdditiveExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAdditiveExpression" ):
                return visitor.visitAdditiveExpression(self)
            else:
                return visitor.visitChildren(self)


    class IdentifierExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdentifierExpression" ):
                listener.enterIdentifierExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdentifierExpression" ):
                listener.exitIdentifierExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitIdentifierExpression" ):
                return visitor.visitIdentifierExpression(self)
            else:
                return visitor.visitChildren(self)


    class FunctionCallExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def functionCall(self):
            return self.getTypedRuleContext(LarishaParser.FunctionCallContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpression" ):
                listener.enterFunctionCallExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpression" ):
                listener.exitFunctionCallExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitFunctionCallExpression" ):
                return visitor.visitFunctionCallExpression(self)
            else:
                return visitor.visitChildren(self)


    class NotExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterNotExpression" ):
                listener.enterNotExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitNotExpression" ):
                listener.exitNotExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitNotExpression" ):
                return visitor.visitNotExpression(self)
            else:
                return visitor.visitChildren(self)


    class MultiplicativeExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LarishaParser.ExpressionContext,i)

        def multOp(self):
            return self.getTypedRuleContext(LarishaParser.MultOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicativeExpression" ):
                listener.enterMultiplicativeExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicativeExpression" ):
                listener.exitMultiplicativeExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultiplicativeExpression" ):
                return visitor.visitMultiplicativeExpression(self)
            else:
                return visitor.visitChildren(self)


    class BooleanExpressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a LarishaParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expression(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.ExpressionContext)
            else:
                return self.getTypedRuleContext(LarishaParser.ExpressionContext,i)

        def boolOp(self):
            return self.getTypedRuleContext(LarishaParser.BoolOpContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanExpression" ):
                listener.enterBooleanExpression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanExpression" ):
                listener.exitBooleanExpression(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBooleanExpression" ):
                return visitor.visitBooleanExpression(self)
            else:
                return visitor.visitChildren(self)



    def expression(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = LarishaParser.ExpressionContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 22
        self.enterRecursionRule(localctx, 22, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 140
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                localctx = LarishaParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 129
                self.constant()
                pass

            elif la_ == 2:
                localctx = LarishaParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 130
                self.match(LarishaParser.IDENTIFIER)
                pass

            elif la_ == 3:
                localctx = LarishaParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 131
                self.match(LarishaParser.T__3)
                self.state = 132
                self.expression(0)
                self.state = 133
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 4:
                localctx = LarishaParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 135
                self.match(LarishaParser.T__7)
                self.state = 136
                self.expression(7)
                pass

            elif la_ == 5:
                localctx = LarishaParser.NegativeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 137
                self.match(LarishaParser.T__8)
                self.state = 138
                self.expression(6)
                pass

            elif la_ == 6:
                localctx = LarishaParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 139
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 160
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,11,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 158
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
                    if la_ == 1:
                        localctx = LarishaParser.MultiplicativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 142
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 143
                        self.multOp()
                        self.state = 144
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = LarishaParser.AdditiveExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 146
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 147
                        self.addOp()
                        self.state = 148
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = LarishaParser.ComparativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 150
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 151
                        self.compreOp()
                        self.state = 152
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = LarishaParser.BooleanExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 154
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 155
                        self.boolOp()
                        self.state = 156
                        self.expression(3)
                        pass

             
                self.state = 162
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,11,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class MultOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_multOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultOp" ):
                listener.enterMultOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultOp" ):
                listener.exitMultOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitMultOp" ):
                return visitor.visitMultOp(self)
            else:
                return visitor.visitChildren(self)




    def multOp(self):

        localctx = LarishaParser.MultOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 163
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__9) | (1 << LarishaParser.T__10) | (1 << LarishaParser.T__11))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AddOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_addOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAddOp" ):
                listener.enterAddOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAddOp" ):
                listener.exitAddOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitAddOp" ):
                return visitor.visitAddOp(self)
            else:
                return visitor.visitChildren(self)




    def addOp(self):

        localctx = LarishaParser.AddOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 165
            _la = self._input.LA(1)
            if not(_la==LarishaParser.T__8 or _la==LarishaParser.T__12):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class CompreOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_compreOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCompreOp" ):
                listener.enterCompreOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCompreOp" ):
                listener.exitCompreOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitCompreOp" ):
                return visitor.visitCompreOp(self)
            else:
                return visitor.visitChildren(self)




    def compreOp(self):

        localctx = LarishaParser.CompreOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_compreOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 167
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__13) | (1 << LarishaParser.T__14) | (1 << LarishaParser.T__15) | (1 << LarishaParser.T__16) | (1 << LarishaParser.T__17) | (1 << LarishaParser.T__18))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BoolOpContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_boolOp

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBoolOp" ):
                listener.enterBoolOp(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBoolOp" ):
                listener.exitBoolOp(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBoolOp" ):
                return visitor.visitBoolOp(self)
            else:
                return visitor.visitChildren(self)




    def boolOp(self):

        localctx = LarishaParser.BoolOpContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_boolOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            _la = self._input.LA(1)
            if not(_la==LarishaParser.T__19 or _la==LarishaParser.T__20):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ConstantContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def INTEGER(self):
            return self.getToken(LarishaParser.INTEGER, 0)

        def FLOAT(self):
            return self.getToken(LarishaParser.FLOAT, 0)

        def STRING(self):
            return self.getToken(LarishaParser.STRING, 0)

        def BOOL(self):
            return self.getToken(LarishaParser.BOOL, 0)

        def CHAR(self):
            return self.getToken(LarishaParser.CHAR, 0)

        def getRuleIndex(self):
            return LarishaParser.RULE_constant

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterConstant" ):
                listener.enterConstant(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitConstant" ):
                listener.exitConstant(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitConstant" ):
                return visitor.visitConstant(self)
            else:
                return visitor.visitChildren(self)




    def constant(self):

        localctx = LarishaParser.ConstantContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 171
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.BOOL) | (1 << LarishaParser.STRING) | (1 << LarishaParser.FLOAT) | (1 << LarishaParser.INTEGER) | (1 << LarishaParser.CHAR))) != 0)):
                self._errHandler.recoverInline(self)
            else:
                self._errHandler.reportMatch(self)
                self.consume()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BlockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def line(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(LarishaParser.LineContext)
            else:
                return self.getTypedRuleContext(LarishaParser.LineContext,i)


        def getRuleIndex(self):
            return LarishaParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBlock" ):
                return visitor.visitBlock(self)
            else:
                return visitor.visitChildren(self)




    def block(self):

        localctx = LarishaParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(LarishaParser.T__21)
            self.state = 177
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__23) | (1 << LarishaParser.T__24) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 174
                self.line()
                self.state = 179
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 180
            self.match(LarishaParser.T__22)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class BreakContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return LarishaParser.RULE_break

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBreak" ):
                listener.enterBreak(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBreak" ):
                listener.exitBreak(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitBreak" ):
                return visitor.visitBreak(self)
            else:
                return visitor.visitChildren(self)




    def break_(self):

        localctx = LarishaParser.BreakContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
            self.match(LarishaParser.T__23)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ReturnStatementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expression(self):
            return self.getTypedRuleContext(LarishaParser.ExpressionContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_returnStatement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturnStatement" ):
                listener.enterReturnStatement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturnStatement" ):
                listener.exitReturnStatement(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitReturnStatement" ):
                return visitor.visitReturnStatement(self)
            else:
                return visitor.visitChildren(self)




    def returnStatement(self):

        localctx = LarishaParser.ReturnStatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(LarishaParser.T__24)
            self.state = 185
            self.expression(0)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx



    def sempred(self, localctx:RuleContext, ruleIndex:int, predIndex:int):
        if self._predicates == None:
            self._predicates = dict()
        self._predicates[11] = self.expression_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expression_sempred(self, localctx:ExpressionContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 2)
         




