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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\24")
        buf.write("H\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\3\2\3\2\3\2\3\3\5\3\27\n\3\3\3\7\3\32\n\3")
        buf.write("\f\3\16\3\35\13\3\3\4\3\4\5\4!\n\4\3\5\3\5\3\5\3\6\3\6")
        buf.write("\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\3\7\7\7\63\n")
        buf.write("\7\f\7\16\7\66\13\7\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\b\3\b\5\bD\n\b\3\t\3\t\3\t\2\3\f\n\2\4\6\b\n")
        buf.write("\f\16\20\2\4\4\2\t\t\13\13\4\2\b\b\n\n\2J\2\22\3\2\2\2")
        buf.write("\4\33\3\2\2\2\6 \3\2\2\2\b\"\3\2\2\2\n%\3\2\2\2\f)\3\2")
        buf.write("\2\2\16C\3\2\2\2\20E\3\2\2\2\22\23\5\4\3\2\23\24\7\2\2")
        buf.write("\3\24\3\3\2\2\2\25\27\5\6\4\2\26\25\3\2\2\2\26\27\3\2")
        buf.write("\2\2\27\30\3\2\2\2\30\32\7\21\2\2\31\26\3\2\2\2\32\35")
        buf.write("\3\2\2\2\33\31\3\2\2\2\33\34\3\2\2\2\34\5\3\2\2\2\35\33")
        buf.write("\3\2\2\2\36!\5\b\5\2\37!\5\n\6\2 \36\3\2\2\2 \37\3\2\2")
        buf.write("\2!\7\3\2\2\2\"#\7\5\2\2#$\5\20\t\2$\t\3\2\2\2%&\7\7\2")
        buf.write("\2&\'\7\6\2\2\'(\5\20\t\2(\13\3\2\2\2)*\b\7\1\2*+\5\16")
        buf.write("\b\2+\64\3\2\2\2,-\f\5\2\2-.\t\2\2\2.\63\5\f\7\6/\60\f")
        buf.write("\4\2\2\60\61\t\3\2\2\61\63\5\f\7\5\62,\3\2\2\2\62/\3\2")
        buf.write("\2\2\63\66\3\2\2\2\64\62\3\2\2\2\64\65\3\2\2\2\65\r\3")
        buf.write("\2\2\2\66\64\3\2\2\2\67D\7\16\2\28D\7\20\2\29:\7\f\2\2")
        buf.write(":D\5\16\b\2;<\7\r\2\2<D\5\16\b\2=>\7\3\2\2>?\5\f\7\2?")
        buf.write("@\7\4\2\2@D\3\2\2\2AD\7\7\2\2BD\7\22\2\2C\67\3\2\2\2C")
        buf.write("8\3\2\2\2C9\3\2\2\2C;\3\2\2\2C=\3\2\2\2CA\3\2\2\2CB\3")
        buf.write("\2\2\2D\17\3\2\2\2EF\5\f\7\2F\21\3\2\2\2\b\26\33 \62\64")
        buf.write("C")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'('", "')'", "'print'", "'='", "<INVALID>", 
                     "'+'", "'*'", "'-'", "'/'", "'(int)'", "'(real)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "STD_OUT", 
                      "ASSIGN", "ID", "ADD", "MUL", "SUB", "DIV", "TOINT", 
                      "TOREAL", "INT", "UINT", "REAL", "NEWLINE", "STRING", 
                      "WS", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_printf = 3
    RULE_assign = 4
    RULE_expr = 5
    RULE_atom = 6
    RULE_value = 7

    ruleNames =  [ "start", "block", "stat", "printf", "assign", "expr", 
                   "atom", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    STD_OUT=3
    ASSIGN=4
    ID=5
    ADD=6
    MUL=7
    SUB=8
    DIV=9
    TOINT=10
    TOREAL=11
    INT=12
    UINT=13
    REAL=14
    NEWLINE=15
    STRING=16
    WS=17
    LINE_COMMENT=18

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

        def block(self):
            return self.getTypedRuleContext(HelloParser.BlockContext,0)


        def EOF(self):
            return self.getToken(HelloParser.EOF, 0)

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
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 16
            self.block()
            self.state = 17
            self.match(HelloParser.EOF)
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
            return HelloParser.RULE_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBlock" ):
                listener.enterBlock(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBlock" ):
                listener.exitBlock(self)




    def block(self):

        localctx = HelloParser.BlockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 2, self.RULE_block)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 25
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.STD_OUT) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE))) != 0):
                self.state = 20
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if _la==HelloParser.STD_OUT or _la==HelloParser.ID:
                    self.state = 19
                    self.stat()


                self.state = 22
                self.match(HelloParser.NEWLINE)
                self.state = 27
                self._errHandler.sync(self)
                _la = self._input.LA(1)

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
        self.enterRule(localctx, 4, self.RULE_stat)
        try:
            self.state = 30
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.STD_OUT]:
                self.enterOuterAlt(localctx, 1)
                self.state = 28
                self.printf()
                pass
            elif token in [HelloParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 29
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
        self.enterRule(localctx, 6, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 32
            self.match(HelloParser.STD_OUT)
            self.state = 33
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
        self.enterRule(localctx, 8, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 35
            self.match(HelloParser.ID)
            self.state = 36
            self.match(HelloParser.ASSIGN)
            self.state = 37
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class MultiplicationExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def MUL(self):
            return self.getToken(HelloParser.MUL, 0)
        def DIV(self):
            return self.getToken(HelloParser.DIV, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterMultiplicationExpr" ):
                listener.enterMultiplicationExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitMultiplicationExpr" ):
                listener.exitMultiplicationExpr(self)


    class AtomExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def atom(self):
            return self.getTypedRuleContext(HelloParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAtomExpr" ):
                listener.enterAtomExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAtomExpr" ):
                listener.exitAtomExpr(self)


    class AdditiveExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def ADD(self):
            return self.getToken(HelloParser.ADD, 0)
        def SUB(self):
            return self.getToken(HelloParser.SUB, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAdditiveExpr" ):
                listener.enterAdditiveExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAdditiveExpr" ):
                listener.exitAdditiveExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HelloParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 10
        self.enterRecursionRule(localctx, 10, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HelloParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 40
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 50
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 48
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.MultiplicationExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 42
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 43
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.MUL or _la==HelloParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 44
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.AdditiveExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 45
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 46
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.ADD or _la==HelloParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 47
                        self.expr(3)
                        pass

             
                self.state = 52
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,4,self._ctx)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.unrollRecursionContexts(_parentctx)
        return localctx


    class AtomContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_atom

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)



    class ParContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterPar" ):
                listener.enterPar(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitPar" ):
                listener.exitPar(self)


    class TointContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOINT(self):
            return self.getToken(HelloParser.TOINT, 0)
        def atom(self):
            return self.getTypedRuleContext(HelloParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToint" ):
                listener.enterToint(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToint" ):
                listener.exitToint(self)


    class StringContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
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


    class TorealContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOREAL(self):
            return self.getToken(HelloParser.TOREAL, 0)
        def atom(self):
            return self.getTypedRuleContext(HelloParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterToreal" ):
                listener.enterToreal(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitToreal" ):
                listener.exitToreal(self)


    class RealContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
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


    class IdContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
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


    class IntContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
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



    def atom(self):

        localctx = HelloParser.AtomContext(self, self._ctx, self.state)
        self.enterRule(localctx, 12, self.RULE_atom)
        try:
            self.state = 65
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.INT]:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 53
                self.match(HelloParser.INT)
                pass
            elif token in [HelloParser.REAL]:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 54
                self.match(HelloParser.REAL)
                pass
            elif token in [HelloParser.TOINT]:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 55
                self.match(HelloParser.TOINT)
                self.state = 56
                self.atom()
                pass
            elif token in [HelloParser.TOREAL]:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 57
                self.match(HelloParser.TOREAL)
                self.state = 58
                self.atom()
                pass
            elif token in [HelloParser.T__0]:
                localctx = HelloParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 59
                self.match(HelloParser.T__0)
                self.state = 60
                self.expr(0)
                self.state = 61
                self.match(HelloParser.T__1)
                pass
            elif token in [HelloParser.ID]:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 63
                self.match(HelloParser.ID)
                pass
            elif token in [HelloParser.STRING]:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 64
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


    class ValueContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


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
        self.enterRule(localctx, 14, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 67
            self.expr(0)
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
        self._predicates[5] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 2)
         




