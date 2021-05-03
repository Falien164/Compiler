# Generated from ./antlr_lib/Hello.g4 by ANTLR 4.9.2
# encoding: utf-8
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
	from typing import TextIO
else:
	from typing.io import TextIO


def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\27")
        buf.write("o\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\3\2\5\2")
        buf.write("\34\n\2\3\2\7\2\37\n\2\f\2\16\2\"\13\2\3\2\3\2\3\3\3\3")
        buf.write("\5\3(\n\3\3\4\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6")
        buf.write("\3\6\5\6\66\n\6\3\7\3\7\3\7\3\7\3\7\5\7=\n\7\3\b\3\b\3")
        buf.write("\b\3\b\3\b\5\bD\n\b\3\t\3\t\3\t\3\t\3\t\5\tK\n\t\3\n\3")
        buf.write("\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\nX\n\n\3\13\3")
        buf.write("\13\3\13\3\13\7\13^\n\13\f\13\16\13a\13\13\3\13\3\13\3")
        buf.write("\f\3\f\3\f\3\f\5\fi\n\f\3\r\3\r\5\rm\n\r\3\r\2\2\16\2")
        buf.write("\4\6\b\n\f\16\20\22\24\26\30\2\2\2s\2 \3\2\2\2\4\'\3\2")
        buf.write("\2\2\6)\3\2\2\2\b,\3\2\2\2\n\65\3\2\2\2\f<\3\2\2\2\16")
        buf.write("C\3\2\2\2\20J\3\2\2\2\22W\3\2\2\2\24Y\3\2\2\2\26h\3\2")
        buf.write("\2\2\30l\3\2\2\2\32\34\5\4\3\2\33\32\3\2\2\2\33\34\3\2")
        buf.write("\2\2\34\35\3\2\2\2\35\37\7\24\2\2\36\33\3\2\2\2\37\"\3")
        buf.write("\2\2\2 \36\3\2\2\2 !\3\2\2\2!#\3\2\2\2\" \3\2\2\2#$\7")
        buf.write("\2\2\3$\3\3\2\2\2%(\5\6\4\2&(\5\b\5\2\'%\3\2\2\2\'&\3")
        buf.write("\2\2\2(\5\3\2\2\2)*\7\b\2\2*+\5\26\f\2+\7\3\2\2\2,-\7")
        buf.write("\n\2\2-.\7\t\2\2./\5\26\f\2/\t\3\2\2\2\60\66\5\f\7\2\61")
        buf.write("\62\5\f\7\2\62\63\7\13\2\2\63\64\5\f\7\2\64\66\3\2\2\2")
        buf.write("\65\60\3\2\2\2\65\61\3\2\2\2\66\13\3\2\2\2\67=\5\16\b")
        buf.write("\289\5\16\b\29:\7\r\2\2:;\5\16\b\2;=\3\2\2\2<\67\3\2\2")
        buf.write("\2<8\3\2\2\2=\r\3\2\2\2>D\5\20\t\2?@\5\20\t\2@A\7\f\2")
        buf.write("\2AB\5\20\t\2BD\3\2\2\2C>\3\2\2\2C?\3\2\2\2D\17\3\2\2")
        buf.write("\2EK\5\22\n\2FG\5\22\n\2GH\7\16\2\2HI\5\22\n\2IK\3\2\2")
        buf.write("\2JE\3\2\2\2JF\3\2\2\2K\21\3\2\2\2LX\7\22\2\2MX\7\23\2")
        buf.write("\2NO\7\17\2\2OX\5\22\n\2PQ\7\20\2\2QX\5\22\n\2RS\7\3\2")
        buf.write("\2ST\5\n\6\2TU\7\4\2\2UX\3\2\2\2VX\7\n\2\2WL\3\2\2\2W")
        buf.write("M\3\2\2\2WN\3\2\2\2WP\3\2\2\2WR\3\2\2\2WV\3\2\2\2X\23")
        buf.write("\3\2\2\2YZ\7\5\2\2Z_\5\26\f\2[\\\7\6\2\2\\^\5\26\f\2]")
        buf.write("[\3\2\2\2^a\3\2\2\2_]\3\2\2\2_`\3\2\2\2`b\3\2\2\2a_\3")
        buf.write("\2\2\2bc\7\7\2\2c\25\3\2\2\2di\5\30\r\2ei\5\24\13\2fi")
        buf.write("\5\n\6\2gi\5\22\n\2hd\3\2\2\2he\3\2\2\2hf\3\2\2\2hg\3")
        buf.write("\2\2\2i\27\3\2\2\2jm\7\n\2\2km\7\25\2\2lj\3\2\2\2lk\3")
        buf.write("\2\2\2m\31\3\2\2\2\r\33 \'\65<CJW_hl")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'<'", "','", "'>'", "'print'", 
                     "'='", "<INVALID>", "'+'", "'*'", "'-'", "'/'", "'(int)'", 
                     "'(real)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STD_OUT", "ASSIGN", "ID", 
                      "ADD", "MUL", "SUB", "DIV", "TOINT", "TOREAL", "UINT", 
                      "INT", "REAL", "NEWLINE", "STRING", "WS", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_stat = 1
    RULE_printf = 2
    RULE_assign = 3
    RULE_expr0 = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_number = 8
    RULE_array = 9
    RULE_value = 10
    RULE_word = 11

    ruleNames =  [ "start", "stat", "printf", "assign", "expr0", "expr1", 
                   "expr2", "expr3", "number", "array", "value", "word" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    STD_OUT=6
    ASSIGN=7
    ID=8
    ADD=9
    MUL=10
    SUB=11
    DIV=12
    TOINT=13
    TOREAL=14
    UINT=15
    INT=16
    REAL=17
    NEWLINE=18
    STRING=19
    WS=20
    LINE_COMMENT=21

    def __init__(self, input:TokenStream, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = ParserATNSimulator(self, self.atn, self.decisionsToDFA, self.sharedContextCache)
        self._predicates = None




    class StartContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

        def NEWLINE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.NEWLINE)
            else:
                return self.getToken(HelloParser.NEWLINE, i)

        def stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.StatContext)
            else:
                return self.getTypedRuleContext(HelloParser.StatContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_start

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStart" ):
                listener.enterStart(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStart" ):
                listener.exitStart(self)




    def start(self):

        localctx = HelloParser.StartContext(self, self._ctx, self.state)
        self.enterRule(localctx, 0, self.RULE_start)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 30
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.STD_OUT) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE))) != 0):
                self.state = 25
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HelloParser.STD_OUT or _la==HelloParser.ID:
                    self.state = 24
                    self.stat()


                self.state = 27
                self.match(HelloParser.NEWLINE)
                self.state = 32
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 33
            self.match(HelloParser.EOF)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class StatContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def printf(self):
            return self.getTypedRuleContext(HelloParser.PrintfContext,0)


        def assign(self):
            return self.getTypedRuleContext(HelloParser.AssignContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)




    def stat(self):

        localctx = HelloParser.StatContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_stat)
        try:
            self.state = 37
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.STD_OUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 35
                self.printf()
                pass
            elif token in [HelloParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 36
                self.assign()
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


    class PrintfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STD_OUT(self):
            return self.getToken(HelloParser.STD_OUT, 0)

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_printf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrintf" ):
                listener.enterPrintf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrintf" ):
                listener.exitPrintf(self)




    def printf(self):

        localctx = HelloParser.PrintfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 39
            self.match(HelloParser.STD_OUT)
            self.state = 40
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class AssignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def ASSIGN(self):
            return self.getToken(HelloParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAssign" ):
                listener.enterAssign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAssign" ):
                listener.exitAssign(self)




    def assign(self):

        localctx = HelloParser.AssignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 6, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 42
            self.match(HelloParser.ID)
            self.state = 43
            self.match(HelloParser.ASSIGN)
            self.state = 44
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr0Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr0

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single0Context(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self):
            return self.getTypedRuleContext(HelloParser.Expr1Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle0" ):
                listener.enterSingle0(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle0" ):
                listener.exitSingle0(self)


    class AddContext(Expr0Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr0Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr1(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Expr1Context)
            else:
                return self.getTypedRuleContext(HelloParser.Expr1Context,i)

        def ADD(self):
            return self.getToken(HelloParser.ADD, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdd" ):
                listener.enterAdd(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdd" ):
                listener.exitAdd(self)



    def expr0(self):

        localctx = HelloParser.Expr0Context(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expr0)
        try:
            self.state = 51
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single0Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 46
                self.expr1()
                pass

            elif la_ == 2:
                localctx = HelloParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 47
                self.expr1()
                self.state = 48
                self.match(HelloParser.ADD)
                self.state = 49
                self.expr1()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr1Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr1

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single1Context(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self):
            return self.getTypedRuleContext(HelloParser.Expr2Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle1" ):
                listener.enterSingle1(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle1" ):
                listener.exitSingle1(self)


    class SubContext(Expr1Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr1Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr2(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Expr2Context)
            else:
                return self.getTypedRuleContext(HelloParser.Expr2Context,i)

        def SUB(self):
            return self.getToken(HelloParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSub" ):
                listener.enterSub(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSub" ):
                listener.exitSub(self)



    def expr1(self):

        localctx = HelloParser.Expr1Context(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_expr1)
        try:
            self.state = 58
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.expr2()
                pass

            elif la_ == 2:
                localctx = HelloParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.expr2()
                self.state = 55
                self.match(HelloParser.SUB)
                self.state = 56
                self.expr2()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr2Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr2

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class Single2Context(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self):
            return self.getTypedRuleContext(HelloParser.Expr3Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle2" ):
                listener.enterSingle2(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle2" ):
                listener.exitSingle2(self)


    class MulContext(Expr2Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr2Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr3(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Expr3Context)
            else:
                return self.getTypedRuleContext(HelloParser.Expr3Context,i)

        def MUL(self):
            return self.getToken(HelloParser.MUL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMul" ):
                listener.enterMul(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMul" ):
                listener.exitMul(self)



    def expr2(self):

        localctx = HelloParser.Expr2Context(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_expr2)
        try:
            self.state = 65
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 60
                self.expr3()
                pass

            elif la_ == 2:
                localctx = HelloParser.MulContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 61
                self.expr3()
                self.state = 62
                self.match(HelloParser.MUL)
                self.state = 63
                self.expr3()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Expr3Context(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr3

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class DivContext(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.NumberContext)
            else:
                return self.getTypedRuleContext(HelloParser.NumberContext,i)

        def DIV(self):
            return self.getToken(HelloParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterDiv" ):
                listener.enterDiv(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitDiv" ):
                listener.exitDiv(self)


    class Single3Context(Expr3Context):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.Expr3Context
            super().__init__(parser)
            self.copyFrom(ctx)

        def number(self):
            return self.getTypedRuleContext(HelloParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterSingle3" ):
                listener.enterSingle3(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitSingle3" ):
                listener.exitSingle3(self)



    def expr3(self):

        localctx = HelloParser.Expr3Context(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_expr3)
        try:
            self.state = 72
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single3Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 67
                self.number()
                pass

            elif la_ == 2:
                localctx = HelloParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 68
                self.number()
                self.state = 69
                self.match(HelloParser.DIV)
                self.state = 70
                self.number()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class NumberContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_number

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr0(self):
            return self.getTypedRuleContext(HelloParser.Expr0Context,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class TointContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(HelloParser.TOINT, 0)
        def number(self):
            return self.getTypedRuleContext(HelloParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)


    class Id_numberContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_number" ):
                listener.enterId_number(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_number" ):
                listener.exitId_number(self)


    class TorealContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(HelloParser.TOREAL, 0)
        def number(self):
            return self.getTypedRuleContext(HelloParser.NumberContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)


    class RealContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def REAL(self):
            return self.getToken(HelloParser.REAL, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReal" ):
                listener.enterReal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReal" ):
                listener.exitReal(self)


    class IntContext(NumberContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.NumberContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def INT(self):
            return self.getToken(HelloParser.INT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterInt" ):
                listener.enterInt(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitInt" ):
                listener.exitInt(self)



    def number(self):

        localctx = HelloParser.NumberContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_number)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.INT]:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 74
                self.match(HelloParser.INT)
                pass
            elif token in [HelloParser.REAL]:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 75
                self.match(HelloParser.REAL)
                pass
            elif token in [HelloParser.TOINT]:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 76
                self.match(HelloParser.TOINT)
                self.state = 77
                self.number()
                pass
            elif token in [HelloParser.TOREAL]:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 78
                self.match(HelloParser.TOREAL)
                self.state = 79
                self.number()
                pass
            elif token in [HelloParser.T__0]:
                localctx = HelloParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 80
                self.match(HelloParser.T__0)
                self.state = 81
                self.expr0()
                self.state = 82
                self.match(HelloParser.T__1)
                pass
            elif token in [HelloParser.ID]:
                localctx = HelloParser.Id_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 84
                self.match(HelloParser.ID)
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


    class ArrayContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ValueContext)
            else:
                return self.getTypedRuleContext(HelloParser.ValueContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_array

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)




    def array(self):

        localctx = HelloParser.ArrayContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_array)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 87
            self.match(HelloParser.T__2)
            self.state = 88
            self.value()
            self.state = 93
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.T__3:
                self.state = 89
                self.match(HelloParser.T__3)
                self.state = 90
                self.value()
                self.state = 95
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 96
            self.match(HelloParser.T__4)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def word(self):
            return self.getTypedRuleContext(HelloParser.WordContext,0)


        def array(self):
            return self.getTypedRuleContext(HelloParser.ArrayContext,0)


        def expr0(self):
            return self.getTypedRuleContext(HelloParser.Expr0Context,0)


        def number(self):
            return self.getTypedRuleContext(HelloParser.NumberContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_value

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterValue" ):
                listener.enterValue(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitValue" ):
                listener.exitValue(self)




    def value(self):

        localctx = HelloParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_value)
        try:
            self.state = 102
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 98
                self.word()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 99
                self.array()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 100
                self.expr0()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 101
                self.number()
                pass


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class WordContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_word

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StringContext(WordContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.WordContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def STRING(self):
            return self.getToken(HelloParser.STRING, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterString" ):
                listener.enterString(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitString" ):
                listener.exitString(self)


    class IdContext(WordContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.WordContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId" ):
                listener.enterId(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId" ):
                listener.exitId(self)



    def word(self):

        localctx = HelloParser.WordContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_word)
        try:
            self.state = 106
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.ID]:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 104
                self.match(HelloParser.ID)
                pass
            elif token in [HelloParser.STRING]:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 105
                self.match(HelloParser.STRING)
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





