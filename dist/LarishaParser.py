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
        4,1,39,212,2,0,7,0,2,1,7,1,2,2,7,2,2,3,7,3,2,4,7,4,2,5,7,5,2,6,7,
        6,2,7,7,7,2,8,7,8,2,9,7,9,2,10,7,10,2,11,7,11,2,12,7,12,2,13,7,13,
        2,14,7,14,2,15,7,15,2,16,7,16,2,17,7,17,2,18,7,18,2,19,7,19,2,20,
        7,20,2,21,7,21,1,0,5,0,46,8,0,10,0,12,0,49,9,0,1,0,1,0,1,1,1,1,1,
        1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,
        1,3,1,72,8,1,1,2,1,2,1,2,1,3,1,3,1,3,1,3,1,4,1,4,1,4,1,4,1,4,1,4,
        3,4,87,8,4,1,4,1,4,1,4,1,4,1,5,1,5,3,5,95,8,5,1,6,1,6,1,6,1,6,1,
        6,1,6,3,6,103,8,6,1,6,1,6,1,7,1,7,1,7,1,7,3,7,111,8,7,1,7,1,7,1,
        7,1,8,1,8,1,8,3,8,119,8,8,1,8,1,8,1,9,1,9,1,9,1,9,3,9,127,8,9,1,
        9,1,9,1,10,1,10,1,10,1,10,3,10,135,8,10,1,11,1,11,1,11,5,11,140,
        8,11,10,11,12,11,143,9,11,1,12,1,12,1,12,5,12,148,8,12,10,12,12,
        12,151,9,12,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,3,13,165,8,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,1,
        13,1,13,1,13,1,13,1,13,1,13,1,13,1,13,5,13,183,8,13,10,13,12,13,
        186,9,13,1,14,1,14,1,15,1,15,1,16,1,16,1,17,1,17,1,18,1,18,1,19,
        1,19,5,19,200,8,19,10,19,12,19,203,9,19,1,19,1,19,1,20,1,20,1,21,
        1,21,1,21,1,21,0,1,26,22,0,2,4,6,8,10,12,14,16,18,20,22,24,26,28,
        30,32,34,36,38,40,42,0,5,1,0,11,13,2,0,10,10,14,14,1,0,15,20,1,0,
        21,22,1,0,31,35,217,0,47,1,0,0,0,2,71,1,0,0,0,4,73,1,0,0,0,6,76,
        1,0,0,0,8,80,1,0,0,0,10,94,1,0,0,0,12,96,1,0,0,0,14,106,1,0,0,0,
        16,115,1,0,0,0,18,122,1,0,0,0,20,130,1,0,0,0,22,136,1,0,0,0,24,144,
        1,0,0,0,26,164,1,0,0,0,28,187,1,0,0,0,30,189,1,0,0,0,32,191,1,0,
        0,0,34,193,1,0,0,0,36,195,1,0,0,0,38,197,1,0,0,0,40,206,1,0,0,0,
        42,208,1,0,0,0,44,46,3,2,1,0,45,44,1,0,0,0,46,49,1,0,0,0,47,45,1,
        0,0,0,47,48,1,0,0,0,48,50,1,0,0,0,49,47,1,0,0,0,50,51,5,0,0,1,51,
        1,1,0,0,0,52,72,3,4,2,0,53,72,3,8,4,0,54,72,3,12,6,0,55,56,3,40,
        20,0,56,57,5,1,0,0,57,72,1,0,0,0,58,72,3,14,7,0,59,60,3,16,8,0,60,
        61,5,1,0,0,61,72,1,0,0,0,62,63,3,42,21,0,63,64,5,1,0,0,64,72,1,0,
        0,0,65,66,3,18,9,0,66,67,5,1,0,0,67,72,1,0,0,0,68,69,3,20,10,0,69,
        70,5,1,0,0,70,72,1,0,0,0,71,52,1,0,0,0,71,53,1,0,0,0,71,54,1,0,0,
        0,71,55,1,0,0,0,71,58,1,0,0,0,71,59,1,0,0,0,71,62,1,0,0,0,71,65,
        1,0,0,0,71,68,1,0,0,0,72,3,1,0,0,0,73,74,3,6,3,0,74,75,5,1,0,0,75,
        5,1,0,0,0,76,77,5,39,0,0,77,78,5,2,0,0,78,79,3,26,13,0,79,7,1,0,
        0,0,80,86,5,3,0,0,81,82,5,4,0,0,82,83,3,26,13,0,83,84,5,5,0,0,84,
        87,1,0,0,0,85,87,3,26,13,0,86,81,1,0,0,0,86,85,1,0,0,0,87,88,1,0,
        0,0,88,89,3,38,19,0,89,90,5,6,0,0,90,91,3,10,5,0,91,9,1,0,0,0,92,
        95,3,8,4,0,93,95,3,38,19,0,94,92,1,0,0,0,94,93,1,0,0,0,95,11,1,0,
        0,0,96,102,5,27,0,0,97,98,5,4,0,0,98,99,3,26,13,0,99,100,5,5,0,0,
        100,103,1,0,0,0,101,103,3,26,13,0,102,97,1,0,0,0,102,101,1,0,0,0,
        103,104,1,0,0,0,104,105,3,38,19,0,105,13,1,0,0,0,106,107,5,30,0,
        0,107,108,5,39,0,0,108,110,5,4,0,0,109,111,3,24,12,0,110,109,1,0,
        0,0,110,111,1,0,0,0,111,112,1,0,0,0,112,113,5,5,0,0,113,114,3,38,
        19,0,114,15,1,0,0,0,115,116,5,39,0,0,116,118,5,4,0,0,117,119,3,22,
        11,0,118,117,1,0,0,0,118,119,1,0,0,0,119,120,1,0,0,0,120,121,5,5,
        0,0,121,17,1,0,0,0,122,123,5,28,0,0,123,124,5,39,0,0,124,126,5,4,
        0,0,125,127,3,24,12,0,126,125,1,0,0,0,126,127,1,0,0,0,127,128,1,
        0,0,0,128,129,5,5,0,0,129,19,1,0,0,0,130,131,5,29,0,0,131,134,5,
        32,0,0,132,133,5,7,0,0,133,135,5,39,0,0,134,132,1,0,0,0,134,135,
        1,0,0,0,135,21,1,0,0,0,136,141,3,26,13,0,137,138,5,8,0,0,138,140,
        3,26,13,0,139,137,1,0,0,0,140,143,1,0,0,0,141,139,1,0,0,0,141,142,
        1,0,0,0,142,23,1,0,0,0,143,141,1,0,0,0,144,149,5,39,0,0,145,146,
        5,8,0,0,146,148,5,39,0,0,147,145,1,0,0,0,148,151,1,0,0,0,149,147,
        1,0,0,0,149,150,1,0,0,0,150,25,1,0,0,0,151,149,1,0,0,0,152,153,6,
        13,-1,0,153,165,3,36,18,0,154,165,5,39,0,0,155,156,5,4,0,0,156,157,
        3,26,13,0,157,158,5,5,0,0,158,165,1,0,0,0,159,160,5,9,0,0,160,165,
        3,26,13,7,161,162,5,10,0,0,162,165,3,26,13,6,163,165,3,16,8,0,164,
        152,1,0,0,0,164,154,1,0,0,0,164,155,1,0,0,0,164,159,1,0,0,0,164,
        161,1,0,0,0,164,163,1,0,0,0,165,184,1,0,0,0,166,167,10,5,0,0,167,
        168,3,28,14,0,168,169,3,26,13,6,169,183,1,0,0,0,170,171,10,4,0,0,
        171,172,3,30,15,0,172,173,3,26,13,5,173,183,1,0,0,0,174,175,10,3,
        0,0,175,176,3,32,16,0,176,177,3,26,13,4,177,183,1,0,0,0,178,179,
        10,2,0,0,179,180,3,34,17,0,180,181,3,26,13,3,181,183,1,0,0,0,182,
        166,1,0,0,0,182,170,1,0,0,0,182,174,1,0,0,0,182,178,1,0,0,0,183,
        186,1,0,0,0,184,182,1,0,0,0,184,185,1,0,0,0,185,27,1,0,0,0,186,184,
        1,0,0,0,187,188,7,0,0,0,188,29,1,0,0,0,189,190,7,1,0,0,190,31,1,
        0,0,0,191,192,7,2,0,0,192,33,1,0,0,0,193,194,7,3,0,0,194,35,1,0,
        0,0,195,196,7,4,0,0,196,37,1,0,0,0,197,201,5,23,0,0,198,200,3,2,
        1,0,199,198,1,0,0,0,200,203,1,0,0,0,201,199,1,0,0,0,201,202,1,0,
        0,0,202,204,1,0,0,0,203,201,1,0,0,0,204,205,5,24,0,0,205,39,1,0,
        0,0,206,207,5,25,0,0,207,41,1,0,0,0,208,209,5,26,0,0,209,210,3,26,
        13,0,210,43,1,0,0,0,15,47,71,86,94,102,110,118,126,134,141,149,164,
        182,184,201
    ]

class LarishaParser ( Parser ):

    grammarFileName = "Larisha.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "';'", "'='", "'if'", "'('", "')'", "'else'", 
                     "'as'", "','", "'!'", "'-'", "'*'", "'/'", "'%'", "'+'", 
                     "'<'", "'>'", "'<='", "'>='", "'=='", "'!='", "'&&'", 
                     "'||'", "'{'", "'}'", "'break'", "'return'", "'while'", 
                     "'export'", "'import'", "'fun'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "WHILE", "EXPORT", 
                      "IMPORT", "FUNCTION", "BOOL", "STRING", "FLOAT", "INTEGER", 
                      "CHAR", "WS", "COMMENT", "LINE_COMMENT", "IDENTIFIER" ]

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
    RULE_importLib = 10
    RULE_arguments = 11
    RULE_parameters = 12
    RULE_expression = 13
    RULE_multOp = 14
    RULE_addOp = 15
    RULE_compreOp = 16
    RULE_boolOp = 17
    RULE_constant = 18
    RULE_block = 19
    RULE_break = 20
    RULE_returnStatement = 21

    ruleNames =  [ "program", "line", "statement", "assignment", "ifBlock", 
                   "elseIfBlock", "whileBlock", "functionDefinition", "functionCall", 
                   "export", "importLib", "arguments", "parameters", "expression", 
                   "multOp", "addOp", "compreOp", "boolOp", "constant", 
                   "block", "break", "returnStatement" ]

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
    T__25=26
    WHILE=27
    EXPORT=28
    IMPORT=29
    FUNCTION=30
    BOOL=31
    STRING=32
    FLOAT=33
    INTEGER=34
    CHAR=35
    WS=36
    COMMENT=37
    LINE_COMMENT=38
    IDENTIFIER=39

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
            self.state = 47
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__24) | (1 << LarishaParser.T__25) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.EXPORT) | (1 << LarishaParser.IMPORT) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 44
                self.line()
                self.state = 49
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 50
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


        def importLib(self):
            return self.getTypedRuleContext(LarishaParser.ImportLibContext,0)


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
            self.state = 71
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,1,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 52
                self.statement()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 53
                self.ifBlock()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 54
                self.whileBlock()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 55
                self.break_()
                self.state = 56
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 58
                self.functionDefinition()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 59
                self.functionCall()
                self.state = 60
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 62
                self.returnStatement()
                self.state = 63
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 65
                self.export()
                self.state = 66
                self.match(LarishaParser.T__0)
                pass

            elif la_ == 9:
                self.enterOuterAlt(localctx, 9)
                self.state = 68
                self.importLib()
                self.state = 69
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
            self.state = 73
            self.assignment()
            self.state = 74
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
            self.state = 76
            self.match(LarishaParser.IDENTIFIER)
            self.state = 77
            self.match(LarishaParser.T__1)
            self.state = 78
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
            self.state = 80
            self.match(LarishaParser.T__2)
            self.state = 86
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.state = 81
                self.match(LarishaParser.T__3)
                self.state = 82
                self.expression(0)
                self.state = 83
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 85
                self.expression(0)
                pass


            self.state = 88
            self.block()

            self.state = 89
            self.match(LarishaParser.T__5)
            self.state = 90
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
            self.state = 94
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [LarishaParser.T__2]:
                self.enterOuterAlt(localctx, 1)
                self.state = 92
                self.ifBlock()
                pass
            elif token in [LarishaParser.T__22]:
                self.enterOuterAlt(localctx, 2)
                self.state = 93
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
            self.state = 96
            self.match(LarishaParser.WHILE)
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                self.state = 97
                self.match(LarishaParser.T__3)
                self.state = 98
                self.expression(0)
                self.state = 99
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 2:
                self.state = 101
                self.expression(0)
                pass


            self.state = 104
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
            self.state = 106
            self.match(LarishaParser.FUNCTION)
            self.state = 107
            self.match(LarishaParser.IDENTIFIER)
            self.state = 108
            self.match(LarishaParser.T__3)
            self.state = 110
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.IDENTIFIER:
                self.state = 109
                self.parameters()


            self.state = 112
            self.match(LarishaParser.T__4)
            self.state = 113
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
            self.state = 115
            self.match(LarishaParser.IDENTIFIER)
            self.state = 116
            self.match(LarishaParser.T__3)
            self.state = 118
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__3) | (1 << LarishaParser.T__8) | (1 << LarishaParser.T__9) | (1 << LarishaParser.BOOL) | (1 << LarishaParser.STRING) | (1 << LarishaParser.FLOAT) | (1 << LarishaParser.INTEGER) | (1 << LarishaParser.CHAR) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 117
                self.arguments()


            self.state = 120
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
            self.state = 122
            self.match(LarishaParser.EXPORT)
            self.state = 123
            self.match(LarishaParser.IDENTIFIER)
            self.state = 124
            self.match(LarishaParser.T__3)
            self.state = 126
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.IDENTIFIER:
                self.state = 125
                self.parameters()


            self.state = 128
            self.match(LarishaParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ImportLibContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IMPORT(self):
            return self.getToken(LarishaParser.IMPORT, 0)

        def STRING(self):
            return self.getToken(LarishaParser.STRING, 0)

        def IDENTIFIER(self):
            return self.getToken(LarishaParser.IDENTIFIER, 0)

        def getRuleIndex(self):
            return LarishaParser.RULE_importLib

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterImportLib" ):
                listener.enterImportLib(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitImportLib" ):
                listener.exitImportLib(self)

        def accept(self, visitor:ParseTreeVisitor):
            if hasattr( visitor, "visitImportLib" ):
                return visitor.visitImportLib(self)
            else:
                return visitor.visitChildren(self)




    def importLib(self):

        localctx = LarishaParser.ImportLibContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_importLib)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 130
            self.match(LarishaParser.IMPORT)
            self.state = 131
            self.match(LarishaParser.STRING)
            self.state = 134
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==LarishaParser.T__6:
                self.state = 132
                self.match(LarishaParser.T__6)
                self.state = 133
                self.match(LarishaParser.IDENTIFIER)


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
        self.enterRule(localctx, 22, self.RULE_arguments)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 136
            self.expression(0)
            self.state = 141
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__7:
                self.state = 137
                self.match(LarishaParser.T__7)
                self.state = 138
                self.expression(0)
                self.state = 143
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
        self.enterRule(localctx, 24, self.RULE_parameters)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 144
            self.match(LarishaParser.IDENTIFIER)
            self.state = 149
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==LarishaParser.T__7:
                self.state = 145
                self.match(LarishaParser.T__7)
                self.state = 146
                self.match(LarishaParser.IDENTIFIER)
                self.state = 151
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
        _startState = 26
        self.enterRecursionRule(localctx, 26, self.RULE_expression, _p)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,11,self._ctx)
            if la_ == 1:
                localctx = LarishaParser.ConstantExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 153
                self.constant()
                pass

            elif la_ == 2:
                localctx = LarishaParser.IdentifierExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 154
                self.match(LarishaParser.IDENTIFIER)
                pass

            elif la_ == 3:
                localctx = LarishaParser.ParenthesizedExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 155
                self.match(LarishaParser.T__3)
                self.state = 156
                self.expression(0)
                self.state = 157
                self.match(LarishaParser.T__4)
                pass

            elif la_ == 4:
                localctx = LarishaParser.NotExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 159
                self.match(LarishaParser.T__8)
                self.state = 160
                self.expression(7)
                pass

            elif la_ == 5:
                localctx = LarishaParser.NegativeExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 161
                self.match(LarishaParser.T__9)
                self.state = 162
                self.expression(6)
                pass

            elif la_ == 6:
                localctx = LarishaParser.FunctionCallExpressionContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 163
                self.functionCall()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 184
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,13,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 182
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
                    if la_ == 1:
                        localctx = LarishaParser.MultiplicativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 166
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 167
                        self.multOp()
                        self.state = 168
                        self.expression(6)
                        pass

                    elif la_ == 2:
                        localctx = LarishaParser.AdditiveExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 170
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 171
                        self.addOp()
                        self.state = 172
                        self.expression(5)
                        pass

                    elif la_ == 3:
                        localctx = LarishaParser.ComparativeExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 174
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 175
                        self.compreOp()
                        self.state = 176
                        self.expression(4)
                        pass

                    elif la_ == 4:
                        localctx = LarishaParser.BooleanExpressionContext(self, LarishaParser.ExpressionContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expression)
                        self.state = 178
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 179
                        self.boolOp()
                        self.state = 180
                        self.expression(3)
                        pass

             
                self.state = 186
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,13,self._ctx)

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
        self.enterRule(localctx, 28, self.RULE_multOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 187
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__10) | (1 << LarishaParser.T__11) | (1 << LarishaParser.T__12))) != 0)):
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
        self.enterRule(localctx, 30, self.RULE_addOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
            _la = self._input.LA(1)
            if not(_la==LarishaParser.T__9 or _la==LarishaParser.T__13):
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
        self.enterRule(localctx, 32, self.RULE_compreOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 191
            _la = self._input.LA(1)
            if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__14) | (1 << LarishaParser.T__15) | (1 << LarishaParser.T__16) | (1 << LarishaParser.T__17) | (1 << LarishaParser.T__18) | (1 << LarishaParser.T__19))) != 0)):
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
        self.enterRule(localctx, 34, self.RULE_boolOp)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 193
            _la = self._input.LA(1)
            if not(_la==LarishaParser.T__20 or _la==LarishaParser.T__21):
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
        self.enterRule(localctx, 36, self.RULE_constant)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 195
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
        self.enterRule(localctx, 38, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 197
            self.match(LarishaParser.T__22)
            self.state = 201
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << LarishaParser.T__2) | (1 << LarishaParser.T__24) | (1 << LarishaParser.T__25) | (1 << LarishaParser.WHILE) | (1 << LarishaParser.EXPORT) | (1 << LarishaParser.IMPORT) | (1 << LarishaParser.FUNCTION) | (1 << LarishaParser.IDENTIFIER))) != 0):
                self.state = 198
                self.line()
                self.state = 203
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 204
            self.match(LarishaParser.T__23)
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
        self.enterRule(localctx, 40, self.RULE_break)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 206
            self.match(LarishaParser.T__24)
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
        self.enterRule(localctx, 42, self.RULE_returnStatement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 208
            self.match(LarishaParser.T__25)
            self.state = 209
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
        self._predicates[13] = self.expression_sempred
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
         




