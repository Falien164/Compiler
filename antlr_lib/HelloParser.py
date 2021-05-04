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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\22")
        buf.write("V\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\5\2\30\n\2\3\2\7\2")
        buf.write("\33\n\2\f\2\16\2\36\13\2\3\2\3\2\3\3\3\3\5\3$\n\3\3\4")
        buf.write("\3\4\3\4\3\5\3\5\3\5\3\5\3\6\3\6\3\6\3\6\3\6\5\6\62\n")
        buf.write("\6\3\7\3\7\3\7\3\7\3\7\5\79\n\7\3\b\3\b\3\b\3\b\3\b\5")
        buf.write("\b@\n\b\3\t\3\t\3\t\3\t\3\t\5\tG\n\t\3\n\3\n\3\n\3\n\3")
        buf.write("\n\3\n\3\n\5\nP\n\n\3\13\3\13\5\13T\n\13\3\13\2\2\f\2")
        buf.write("\4\6\b\n\f\16\20\22\24\2\2\2W\2\34\3\2\2\2\4#\3\2\2\2")
        buf.write("\6%\3\2\2\2\b(\3\2\2\2\n\61\3\2\2\2\f8\3\2\2\2\16?\3\2")
        buf.write("\2\2\20F\3\2\2\2\22O\3\2\2\2\24S\3\2\2\2\26\30\5\4\3\2")
        buf.write("\27\26\3\2\2\2\27\30\3\2\2\2\30\31\3\2\2\2\31\33\7\17")
        buf.write("\2\2\32\27\3\2\2\2\33\36\3\2\2\2\34\32\3\2\2\2\34\35\3")
        buf.write("\2\2\2\35\37\3\2\2\2\36\34\3\2\2\2\37 \7\2\2\3 \3\3\2")
        buf.write("\2\2!$\5\6\4\2\"$\5\b\5\2#!\3\2\2\2#\"\3\2\2\2$\5\3\2")
        buf.write("\2\2%&\7\3\2\2&\'\5\n\6\2\'\7\3\2\2\2()\7\5\2\2)*\7\4")
        buf.write("\2\2*+\5\n\6\2+\t\3\2\2\2,\62\5\22\n\2-.\5\f\7\2./\7\6")
        buf.write("\2\2/\60\5\f\7\2\60\62\3\2\2\2\61,\3\2\2\2\61-\3\2\2\2")
        buf.write("\62\13\3\2\2\2\639\5\16\b\2\64\65\5\16\b\2\65\66\7\b\2")
        buf.write("\2\66\67\5\16\b\2\679\3\2\2\28\63\3\2\2\28\64\3\2\2\2")
        buf.write("9\r\3\2\2\2:@\5\20\t\2;<\5\20\t\2<=\7\7\2\2=>\5\20\t\2")
        buf.write(">@\3\2\2\2?:\3\2\2\2?;\3\2\2\2@\17\3\2\2\2AG\5\22\n\2")
        buf.write("BC\5\22\n\2CD\7\t\2\2DE\5\22\n\2EG\3\2\2\2FA\3\2\2\2F")
        buf.write("B\3\2\2\2G\21\3\2\2\2HP\7\f\2\2IP\7\16\2\2JK\7\n\2\2K")
        buf.write("P\5\22\n\2LM\7\13\2\2MP\5\22\n\2NP\7\5\2\2OH\3\2\2\2O")
        buf.write("I\3\2\2\2OJ\3\2\2\2OL\3\2\2\2ON\3\2\2\2P\23\3\2\2\2QT")
        buf.write("\7\5\2\2RT\7\20\2\2SQ\3\2\2\2SR\3\2\2\2T\25\3\2\2\2\13")
        buf.write("\27\34#\618?FOS")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'print'", "'='", "<INVALID>", "'+'", 
                     "'*'", "'-'", "'/'", "'(int)'", "'(real)'" ]

    symbolicNames = [ "<INVALID>", "STD_OUT", "ASSIGN", "ID", "ADD", "MUL", 
                      "SUB", "DIV", "TOINT", "TOREAL", "INT", "UINT", "REAL", 
                      "NEWLINE", "STRING", "WS", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_statement = 1
    RULE_printf = 2
    RULE_assign = 3
    RULE_expression = 4
    RULE_expr1 = 5
    RULE_expr2 = 6
    RULE_expr3 = 7
    RULE_value = 8
    RULE_word = 9

    ruleNames =  [ "start", "statement", "printf", "assign", "expression", 
                   "expr1", "expr2", "expr3", "value", "word" ]

    EOF = Token.EOF
    STD_OUT=1
    ASSIGN=2
    ID=3
    ADD=4
    MUL=5
    SUB=6
    DIV=7
    TOINT=8
    TOREAL=9
    INT=10
    UINT=11
    REAL=12
    NEWLINE=13
    STRING=14
    WS=15
    LINE_COMMENT=16

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

        def statement(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.StatementContext)
            else:
                return self.getTypedRuleContext(HelloParser.StatementContext,i)


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
            self.state = 26
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.STD_OUT) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE))) != 0):
                self.state = 21
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HelloParser.STD_OUT or _la==HelloParser.ID:
                    self.state = 20
                    self.statement()


                self.state = 23
                self.match(HelloParser.NEWLINE)
                self.state = 28
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 29
            self.match(HelloParser.EOF)
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


        def getRuleIndex(self):
            return HelloParser.RULE_statement

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class StatContext(StatementContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.StatementContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def printf(self):
            return self.getTypedRuleContext(HelloParser.PrintfContext,0)

        def assign(self):
            return self.getTypedRuleContext(HelloParser.AssignContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat" ):
                listener.enterStat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat" ):
                listener.exitStat(self)



    def statement(self):

        localctx = HelloParser.StatementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_statement)
        try:
            self.state = 33
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.STD_OUT]:
                localctx = HelloParser.StatContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 31
                self.printf()
                pass
            elif token in [HelloParser.ID]:
                localctx = HelloParser.StatContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 32
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

        def expression(self):
            return self.getTypedRuleContext(HelloParser.ExpressionContext,0)


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
            self.state = 35
            self.match(HelloParser.STD_OUT)
            self.state = 36
            self.expression()
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

        def expression(self):
            return self.getTypedRuleContext(HelloParser.ExpressionContext,0)


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
            self.state = 38
            self.match(HelloParser.ID)
            self.state = 39
            self.match(HelloParser.ASSIGN)
            self.state = 40
            self.expression()
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
            return HelloParser.RULE_expression

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class AddContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExpressionContext
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


    class Primary_expressionContext(ExpressionContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExpressionContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPrimary_expression" ):
                listener.enterPrimary_expression(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPrimary_expression" ):
                listener.exitPrimary_expression(self)



    def expression(self):

        localctx = HelloParser.ExpressionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_expression)
        try:
            self.state = 47
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Primary_expressionContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 42
                self.value()
                pass

            elif la_ == 2:
                localctx = HelloParser.AddContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 43
                self.expr1()
                self.state = 44
                self.match(HelloParser.ADD)
                self.state = 45
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
            self.state = 54
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,4,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single1Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 49
                self.expr2()
                pass

            elif la_ == 2:
                localctx = HelloParser.SubContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 50
                self.expr2()
                self.state = 51
                self.match(HelloParser.SUB)
                self.state = 52
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
            self.state = 61
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,5,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single2Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 56
                self.expr3()
                pass

            elif la_ == 2:
                localctx = HelloParser.MulContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 57
                self.expr3()
                self.state = 58
                self.match(HelloParser.MUL)
                self.state = 59
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

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ValueContext)
            else:
                return self.getTypedRuleContext(HelloParser.ValueContext,i)

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

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


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
            self.state = 68
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                localctx = HelloParser.Single3Context(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 63
                self.value()
                pass

            elif la_ == 2:
                localctx = HelloParser.DivContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 64
                self.value()
                self.state = 65
                self.match(HelloParser.DIV)
                self.state = 66
                self.value()
                pass


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


        def getRuleIndex(self):
            return HelloParser.RULE_value

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class TointContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(HelloParser.TOINT, 0)
        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)


    class Id_numberContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ValueContext
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


    class TorealContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ValueContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(HelloParser.TOREAL, 0)
        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)


    class RealContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ValueContext
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


    class IntContext(ValueContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ValueContext
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



    def value(self):

        localctx = HelloParser.ValueContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_value)
        try:
            self.state = 77
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.INT]:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 70
                self.match(HelloParser.INT)
                pass
            elif token in [HelloParser.REAL]:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 71
                self.match(HelloParser.REAL)
                pass
            elif token in [HelloParser.TOINT]:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 72
                self.match(HelloParser.TOINT)
                self.state = 73
                self.value()
                pass
            elif token in [HelloParser.TOREAL]:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 74
                self.match(HelloParser.TOREAL)
                self.state = 75
                self.value()
                pass
            elif token in [HelloParser.ID]:
                localctx = HelloParser.Id_numberContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 76
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
        self.enterRule(localctx, 18, self.RULE_word)
        try:
            self.state = 81
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.ID]:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 79
                self.match(HelloParser.ID)
                pass
            elif token in [HelloParser.STRING]:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 80
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





