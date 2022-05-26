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
        4,1,37,199,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,1,0,5,0,44,8,0,10,0,12,0,47,9,0,1,0,1,0,1,1,1,1,1,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,3,1,65,8,1,1,2,1,2,1,2,1,3,1,
        3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,3,4,80,8,4,1,4,1,4,1,4,1,4,1,5,
        1,5,3,5,88,8,5,1,6,1,6,1,6,1,6,1,6,1,6,3,6,96,8,6,1,6,1,6,1,7,1,
        7,1,7,1,7,3,7,104,8,7,1,7,1,7,1,7,1,8,1,8,1,8,3,8,112,8,8,1,8,1,
        8,1,9,1,9,1,9,1,9,3,9,120,8,9,1,9,1,9,1,10,1,10,1,10,5,10,127,8,
        10,10,10,12,10,130,9,10,1,11,1,11,1,11,5,11,135,8,11,10,11,12,11,
        138,9,11,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,3,12,152,8,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,1,12,
        1,12,1,12,1,12,1,12,1,12,1,12,1,12,5,12,170,8,12,10,12,12,12,173,
        9,12,1,13,1,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,
        5,18,187,8,18,10,18,12,18,190,9,18,1,18,1,18,1,19,1,19,1,20,1,20,
        1,20,1,20,0,1,24,21,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,30,32,
        34,36,38,40,0,5,1,0,10,12,2,0,9,9,13,13,1,0,14,19,1,0,20,21,1,0,
        29,33,203,0,45,1,0,0,0,2,64,1,0,0,0,4,66,1,0,0,0,6,69,1,0,0,0,8,
        73,1,0,0,0,10,87,1,0,0,0,12,89,1,0,0,0,14,99,1,0,0,0,16,108,1,0,
        0,0,18,115,1,0,0,0,20,123,1,0,0,0,22,131,1,0,0,0,24,151,1,0,0,0,
        26,174,1,0,0,0,28,176,1,0,0,0,30,178,1,0,0,0,32,180,1,0,0,0,34,182,
        1,0,0,0,36,184,1,0,0,0,38,193,1,0,0,0,40,195,1,0,0,0,42,44,3,2,1,
        0,43,42,1,0,0,0,44,47,1,0,0,0,45,43,1,0,0,0,45,46,1,0,0,0,46,48,
        1,0,0,0,47,45,1,0,0,0,48,49,5,0,0,1,49,1,1,0,0,0,50,65,3,4,2,0,51,
        65,3,8,4,0,52,65,3,12,6,0,53,54,3,38,19,0,54,55,5,1,0,0,55,65,1,
        0,0,0,56,65,3,14,7,0,57,58,3,16,8,0,58,59,5,1,0,0,59,65,1,0,0,0,
        60,61,3,40,20,0,61,62,5,1,0,0,62,65,1,0,0,0,63,65,3,18,9,0,64,50,
        1,0,0,0,64,51,1,0,0,0,64,52,1,0,0,0,64,53,1,0,0,0,64,56,1,0,0,0,
        64,57,1,0,0,0,64,60,1,0,0,0,64,63,1,0,0,0,65,3,1,0,0,0,66,67,3,6,
        3,0,67,68,5,1,0,0,68,5,1,0,0,0,69,70,5,37,0,0,70,71,5,2,0,0,71,72,
        3,24,12,0,72,7,1,0,0,0,73,79,5,3,0,0,74,75,5,4,0,0,75,76,3,24,12,
        0,76,77,5,5,0,0,77,80,1,0,0,0,78,80,3,24,12,0,79,74,1,0,0,0,79,78,
        1,0,0,0,80,81,1,0,0,0,81,82,3,36,18,0,82,83,5,6,0,0,83,84,3,10,5,
        0,84,9,1,0,0,0,85,88,3,8,4,0,86,88,3,36,18,0,87,85,1,0,0,0,87,86,
        1,0,0,0,88,11,1,0,0,0,89,95,5,26,0,0,90,91,5,4,0,0,91,92,3,24,12,
        0,92,93,5,5,0,0,93,96,1,0,0,0,94,96,3,24,12,0,95,90,1,0,0,0,95,94,
        1,0,0,0,96,97,1,0,0,0,97,98,3,36,18,0,98,13,1,0,0,0,99,100,5,28,
        0,0,100,101,5,37,0,0,101,103,5,4,0,0,102,104,3,22,11,0,103,102,1,
        0,0,0,103,104,1,0,0,0,104,105,1,0,0,0,105,106,5,5,0,0,106,107,3,
        36,18,0,107,15,1,0,0,0,108,109,5,37,0,0,109,111,5,4,0,0,110,112,
        3,20,10,0,111,110,1,0,0,0,111,112,1,0,0,0,112,113,1,0,0,0,113,114,
        5,5,0,0,114,17,1,0,0,0,115,116,5,27,0,0,116,117,5,37,0,0,117,119,
        5,4,0,0,118,120,3,22,11,0,119,118,1,0,0,0,119,120,1,0,0,0,120,121,
        1,0,0,0,121,122,5,5,0,0,122,19,1,0,0,0,123,128,3,24,12,0,124,125,
        5,7,0,0,125,127,3,24,12,0,126,124,1,0,0,0,127,130,1,0,0,0,128,126,
        1,0,0,0,128,129,1,0,0,0,129,21,1,0,0,0,130,128,1,0,0,0,131,136,5,
        37,0,0,132,133,5,7,0,0,133,135,5,37,0,0,134,132,1,0,0,0,135,138,
        1,0,0,0,136,134,1,0,0,0,136,137,1,0,0,0,137,23,1,0,0,0,138,136,1,
        0,0,0,139,140,6,12,-1,0,140,152,3,34,17,0,141,152,5,37,0,0,142,143,
        5,4,0,0,143,144,3,24,12,0,144,145,5,5,0,0,145,152,1,0,0,0,146,147,
        5,8,0,0,147,152,3,24,12,7,148,149,5,9,0,0,149,152,3,24,12,6,150,
        152,3,16,8,0,151,139,1,0,0,0,151,141,1,0,0,0,151,142,1,0,0,0,151,
        146,1,0,0,0,151,148,1,0,0,0,151,150,1,0,0,0,152,171,1,0,0,0,153,
        154,10,5,0,0,154,155,3,26,13,0,155,156,3,24,12,6,156,170,1,0,0,0,
        157,158,10,4,0,0,158,159,3,28,14,0,159,160,3,24,12,5,160,170,1,0,
        0,0,161,162,10,3,0,0,162,163,3,30,15,0,163,164,3,24,12,4,164,170,
        1,0,0,0,165,166,10,2,0,0,166,167,3,32,16,0,167,168,3,24,12,3,168,
        170,1,0,0,0,169,153,1,0,0,0,169,157,1,0,0,0,169,161,1,0,0,0,169,
        165,1,0,0,0,170,173,1,0,0,0,171,169,1,0,0,0,171,172,1,0,0,0,172,
        25,1,0,0,0,173,171,1,0,0,0,174,175,7,0,0,0,175,27,1,0,0,0,176,177,
        7,1,0,0,177,29,1,0,0,0,178,179,7,2,0,0,179,31,1,0,0,0,180,181,7,
        3,0,0,181,33,1,0,0,0,182,183,7,4,0,0,183,35,1,0,0,0,184,188,5,22,
        0,0,185,187,3,2,1,0,186,185,1,0,0,0,187,190,1,0,0,0,188,186,1,0,
        0,0,188,189,1,0,0,0,189,191,1,0,0,0,190,188,1,0,0,0,191,192,5,23,
        0,0,192,37,1,0,0,0,193,194,5,24,0,0,194,39,1,0,0,0,195,196,5,25,
        0,0,196,197,3,24,12,0,197,41,1,0,0,0,14,45,64,79,87,95,103,111,119,
        128,136,151,169,171,188
    ]

class LarishaParser ( Parser ):

    grammarFileName = "Larisha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'if'", "'('", "')'", "'else'", 
                     "','", "'!'", "'-'", "'*'", "'/'", "'%'", "'+'", "'<'", 
                     "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", "'||'", 
                     "'{'", "'}'", "'break'", "'return'", "'while'", "'export'", 
                     "'fun'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "WHILE", "EXPORT", "FUNCTION", 
                      "BOOL", "STRING", "FLOAT", "INTEGER", "CHAR", "WS", 
                      "COMMENT", "LINE_COMMENT", "IDENTIFIER" ]

    RULE_program = 0
    RULE_line = 1
    RULE_statement = 2
    RULE_assignment = 3
    RULE_ifBlock = 4
    RULE_elseIfBlock = 5
    RULE_whileBlock = 6
    RULE_functionDefinition = 7
    RULE_functionCall = 8
    RULE_export = 9
    RULE_arguments = 10
    RULE_parameters = 11
    RULE_expression = 12
    RULE_multOp = 13
    RULE_addOp = 14
    RULE_compreOp = 15
    RULE_boolOp = 16
    RULE_constant = 17
    RULE_block = 18
    RULE_break = 19
    RULE_returnStatement = 20

    ruleNames =  [ "program", "line", "statement", "assignment", "ifBlock", 
                   "elseIfBlock", "whileBlock", "functionDefinition", "functionCall", 
                   "export", "arguments", "parameters", "expression", "multOp", 
                   "addOp", "compreOp", "boolOp", "constant", "block", "break", 
                   "returnStatement" ]

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
    EXPORT=27
    FUNCTION=28
    BOOL=29
    STRING=30
    FLOAT=31
    INTEGER=32
    CHAR=33
    WS=34
    COMMENT=35
    LINE_COMMENT=36
    IDENTIFIER=37

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
            self.state = 45
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__23) | (1 << LarishaParser.T__24) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.EXPORT) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 42
                self.line()
                self.state = 47
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 48
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


        def export(self):
            return self.getTypedRuleContext(LarishaParser.ExportContext,0)


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
            self.state = 64
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 50
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 51
                self.ifBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 52
                self.whileBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 53
                self.break_()
                self.state = 54
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 56
                self.functionDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 57
                self.functionCall()
                self.state = 58
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 60
                self.returnStatement()
                self.state = 61
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 63
                self.export()
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
            self.state = 66
            self.assignment()
            self.state = 67
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
            self.state = 69
            self.match(LarishaParser.IDENTIFIER)
            self.state = 70
            self.match(LarishaParser.T__1)
            self.state = 71
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
            self.state = 73
            self.match(LarishaParser.T__2)
            self.state = 79
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 74
                self.match(LarishaParser.T__3)
                self.state = 75
                self.expression(0)
                self.state = 76
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 78
                self.expression(0)
                pass


            self.state = 81
            self.block()

            self.state = 82
            self.match(LarishaParser.T__5)
            self.state = 83
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
            self.state = 87
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LarishaParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 85
                self.ifBlock()
                pass
            elif token in [LarishaParser.T__21]:
                self.enterOuterAlt(localctx, 2)
                self.state = 86
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
            self.state = 89
            self.match(LarishaParser.WHILE)
            self.state = 95
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 90
                self.match(LarishaParser.T__3)
                self.state = 91
                self.expression(0)
                self.state = 92
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 94
                self.expression(0)
                pass


            self.state = 97
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
            self.state = 99
            self.match(LarishaParser.FUNCTION)
            self.state = 100
            self.match(LarishaParser.IDENTIFIER)
            self.state = 101
            self.match(LarishaParser.T__3)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.IDENTIFIER:
                self.state = 102
                self.parameters()


            self.state = 105
            self.match(LarishaParser.T__4)
            self.state = 106
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
            self.state = 108
            self.match(LarishaParser.IDENTIFIER)
            self.state = 109
            self.match(LarishaParser.T__3)
            self.state = 111
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__3) | (1 << LarishaParser.T__7) | (1 << LarishaParser.T__8) | (1 << LarishaParser.BOOL) | (1 << LarishaParser.STRING) | (1 << LarishaParser.FLOAT) | (1 << LarishaParser.INTEGER) | (1 << LarishaParser.CHAR) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 110
                self.arguments()


            self.state = 113
            self.match(LarishaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExportContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EXPORT(self):
            return self.getToken(LarishaParser.EXPORT, 0)

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def parameters(self):
            return self.getTypedRuleContext(LarishaParser.ParametersContext,0)


        def getRuleIndex(self):
            return LarishaParser.RULE_export

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterExport" ):
                listener.enterExport(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitExport" ):
                listener.exitExport(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitExport" ):
                return visitor.visitExport(self)
            else:
                return visitor.visitChildren(self)




    def export(self):

        localctx = LarishaParser.ExportContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_export)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 115
            self.match(LarishaParser.EXPORT)
            self.state = 116
            self.match(LarishaParser.IDENTIFIER)
            self.state = 117
            self.match(LarishaParser.T__3)
            self.state = 119
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.IDENTIFIER:
                self.state = 118
                self.parameters()


            self.state = 121
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
        self.enterRule(localctx, 20, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 123
            self.expression(0)
            self.state = 128
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__6:
                self.state = 124
                self.match(LarishaParser.T__6)
                self.state = 125
                self.expression(0)
                self.state = 130
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
        self.enterRule(localctx, 22, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 131
            self.match(LarishaParser.IDENTIFIER)
            self.state = 136
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__6:
                self.state = 132
                self.match(LarishaParser.T__6)
                self.state = 133
                self.match(LarishaParser.IDENTIFIER)
                self.state = 138
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
        _startState = 24
        self.enterRecursionRule(localctx, 24, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 151
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,10,self._ctx)
            if la_ == 1:
                localctx = LarishaParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 140
                self.constant()
                pass

            elif la_ == 2:
                localctx = LarishaParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 141
                self.match(LarishaParser.IDENTIFIER)
                pass

            elif la_ == 3:
                localctx = LarishaParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 142
                self.match(LarishaParser.T__3)
                self.state = 143
                self.expression(0)
                self.state = 144
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 4:
                localctx = LarishaParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 146
                self.match(LarishaParser.T__7)
                self.state = 147
                self.expression(7)
                pass

            elif la_ == 5:
                localctx = LarishaParser.NegativeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 148
                self.match(LarishaParser.T__8)
                self.state = 149
                self.expression(6)
                pass

            elif la_ == 6:
                localctx = LarishaParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 150
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 171
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 169
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
                    if la_ == 1:
                        localctx = LarishaParser.MultiplicativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 153
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 154
                        self.multOp()
                        self.state = 155
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = LarishaParser.AdditiveExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 157
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 158
                        self.addOp()
                        self.state = 159
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = LarishaParser.ComparativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 161
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 162
                        self.compreOp()
                        self.state = 163
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = LarishaParser.BooleanExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 165
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 166
                        self.boolOp()
                        self.state = 167
                        self.expression(3)
                        pass

             
                self.state = 173
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

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
        self.enterRule(localctx, 26, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 174
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
        self.enterRule(localctx, 28, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 176
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
        self.enterRule(localctx, 30, self.RULE_compreOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 178
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
        self.enterRule(localctx, 32, self.RULE_boolOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 180
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
        self.enterRule(localctx, 34, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 182
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
        self.enterRule(localctx, 36, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 184
            self.match(LarishaParser.T__21)
            self.state = 188
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__23) | (1 << LarishaParser.T__24) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.EXPORT) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 185
                self.line()
                self.state = 190
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 191
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
        self.enterRule(localctx, 38, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
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
        self.enterRule(localctx, 40, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
            self.match(LarishaParser.T__24)
            self.state = 196
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
        self._predicates[12] = self.expression_sempred
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
         




