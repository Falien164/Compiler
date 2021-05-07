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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3\32")
        buf.write("h\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7\4\b")
        buf.write("\t\b\4\t\t\t\4\n\t\n\4\13\t\13\3\2\3\2\3\2\3\3\5\3\33")
        buf.write("\n\3\3\3\7\3\36\n\3\f\3\16\3!\13\3\3\4\3\4\3\4\3\4\5\4")
        buf.write("\'\n\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\7\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\7\tC\n\t\f\t\16\tF\13\t\3\n\3\n\3\n\3\n\3\n\3\n\3\n")
        buf.write("\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\3\n\5\n[")
        buf.write("\n\n\7\n]\n\n\f\n\16\n`\13\n\3\n\3\n\5\nd\n\n\3\13\3\13")
        buf.write("\3\13\2\3\20\f\2\4\6\b\n\f\16\20\22\24\2\4\4\2\17\17\21")
        buf.write("\21\4\2\16\16\20\20\2n\2\26\3\2\2\2\4\37\3\2\2\2\6&\3")
        buf.write("\2\2\2\b(\3\2\2\2\n+\3\2\2\2\f.\3\2\2\2\16\65\3\2\2\2")
        buf.write("\209\3\2\2\2\22c\3\2\2\2\24e\3\2\2\2\26\27\5\4\3\2\27")
        buf.write("\30\7\2\2\3\30\3\3\2\2\2\31\33\5\6\4\2\32\31\3\2\2\2\32")
        buf.write("\33\3\2\2\2\33\34\3\2\2\2\34\36\7\27\2\2\35\32\3\2\2\2")
        buf.write("\36!\3\2\2\2\37\35\3\2\2\2\37 \3\2\2\2 \5\3\2\2\2!\37")
        buf.write("\3\2\2\2\"\'\5\b\5\2#\'\5\n\6\2$\'\5\f\7\2%\'\5\16\b\2")
        buf.write("&\"\3\2\2\2&#\3\2\2\2&$\3\2\2\2&%\3\2\2\2\'\7\3\2\2\2")
        buf.write("()\7\n\2\2)*\5\24\13\2*\t\3\2\2\2+,\7\13\2\2,-\7\r\2\2")
        buf.write("-\13\3\2\2\2./\7\r\2\2/\60\7\3\2\2\60\61\5\20\t\2\61\62")
        buf.write("\7\4\2\2\62\63\7\f\2\2\63\64\5\24\13\2\64\r\3\2\2\2\65")
        buf.write("\66\7\r\2\2\66\67\7\f\2\2\678\5\24\13\28\17\3\2\2\29:")
        buf.write("\b\t\1\2:;\5\22\n\2;D\3\2\2\2<=\f\5\2\2=>\t\2\2\2>C\5")
        buf.write("\20\t\6?@\f\4\2\2@A\t\3\2\2AC\5\20\t\5B<\3\2\2\2B?\3\2")
        buf.write("\2\2CF\3\2\2\2DB\3\2\2\2DE\3\2\2\2E\21\3\2\2\2FD\3\2\2")
        buf.write("\2Gd\7\24\2\2Hd\7\26\2\2IJ\7\22\2\2Jd\5\22\n\2KL\7\23")
        buf.write("\2\2Ld\5\22\n\2MN\7\5\2\2NO\5\20\t\2OP\7\6\2\2Pd\3\2\2")
        buf.write("\2Qd\7\r\2\2RS\7\r\2\2ST\7\3\2\2TU\5\20\t\2UV\7\4\2\2")
        buf.write("Vd\3\2\2\2W^\7\7\2\2XZ\5\24\13\2Y[\7\b\2\2ZY\3\2\2\2Z")
        buf.write("[\3\2\2\2[]\3\2\2\2\\X\3\2\2\2]`\3\2\2\2^\\\3\2\2\2^_")
        buf.write("\3\2\2\2_a\3\2\2\2`^\3\2\2\2ad\7\t\2\2bd\7\30\2\2cG\3")
        buf.write("\2\2\2cH\3\2\2\2cI\3\2\2\2cK\3\2\2\2cM\3\2\2\2cQ\3\2\2")
        buf.write("\2cR\3\2\2\2cW\3\2\2\2cb\3\2\2\2d\23\3\2\2\2ef\5\20\t")
        buf.write("\2f\25\3\2\2\2\n\32\37&BDZ^c")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'('", "')'", "'{'", "','", 
                     "'}'", "'print'", "'read'", "'='", "<INVALID>", "'+'", 
                     "'*'", "'-'", "'/'", "'(int)'", "'(real)'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "STD_OUT", "STD_IN", "ASSIGN", "ID", "ADD", "MUL", 
                      "SUB", "DIV", "TOINT", "TOREAL", "INT", "UINT", "REAL", 
                      "NEWLINE", "STRING", "WS", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_printf = 3
    RULE_scanf = 4
    RULE_array_assign = 5
    RULE_assign = 6
    RULE_expr = 7
    RULE_atom = 8
    RULE_value = 9

    ruleNames =  [ "start", "block", "stat", "printf", "scanf", "array_assign", 
                   "assign", "expr", "atom", "value" ]

    EOF = Token.EOF
    T__0=1
    T__1=2
    T__2=3
    T__3=4
    T__4=5
    T__5=6
    T__6=7
    STD_OUT=8
    STD_IN=9
    ASSIGN=10
    ID=11
    ADD=12
    MUL=13
    SUB=14
    DIV=15
    TOINT=16
    TOREAL=17
    INT=18
    UINT=19
    REAL=20
    NEWLINE=21
    STRING=22
    WS=23
    LINE_COMMENT=24

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
            self.state = 20
            self.block()
            self.state = 21
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
            self.state = 29
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE))) != 0):
                self.state = 24
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID))) != 0):
                    self.state = 23
                    self.stat()


                self.state = 26
                self.match(HelloParser.NEWLINE)
                self.state = 31
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


        def scanf(self):
            return self.getTypedRuleContext(HelloParser.ScanfContext,0)


        def array_assign(self):
            return self.getTypedRuleContext(HelloParser.Array_assignContext,0)


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
            self.state = 36
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 32
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 33
                self.scanf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 34
                self.array_assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 35
                self.assign()
                pass


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
            self.state = 38
            self.match(HelloParser.STD_OUT)
            self.state = 39
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class ScanfContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def STD_IN(self):
            return self.getToken(HelloParser.STD_IN, 0)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_scanf

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterScanf" ):
                listener.enterScanf(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitScanf" ):
                listener.exitScanf(self)




    def scanf(self):

        localctx = HelloParser.ScanfContext(self, self._ctx, self.state)
        self.enterRule(localctx, 8, self.RULE_scanf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 41
            self.match(HelloParser.STD_IN)
            self.state = 42
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Array_assignContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def ASSIGN(self):
            return self.getToken(HelloParser.ASSIGN, 0)

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_array_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray_assign" ):
                listener.enterArray_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray_assign" ):
                listener.exitArray_assign(self)




    def array_assign(self):

        localctx = HelloParser.Array_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 10, self.RULE_array_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 44
            self.match(HelloParser.ID)
            self.state = 45
            self.match(HelloParser.T__0)
            self.state = 46
            self.expr(0)
            self.state = 47
            self.match(HelloParser.T__1)
            self.state = 48
            self.match(HelloParser.ASSIGN)
            self.state = 49
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
        self.enterRule(localctx, 12, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 51
            self.match(HelloParser.ID)
            self.state = 52
            self.match(HelloParser.ASSIGN)
            self.state = 53
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
        _startState = 14
        self.enterRecursionRule(localctx, 14, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            localctx = HelloParser.AtomExprContext(self, localctx)
            self._ctx = localctx
            _prevctx = localctx

            self.state = 56
            self.atom()
            self._ctx.stop = self._input.LT(-1)
            self.state = 66
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,4,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 64
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,3,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.MultiplicationExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 58
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 59
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.MUL or _la==HelloParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 60
                        self.expr(4)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.AdditiveExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 61
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 62
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.ADD or _la==HelloParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 63
                        self.expr(3)
                        pass

             
                self.state = 68
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


    class ArrayContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def value(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ValueContext)
            else:
                return self.getTypedRuleContext(HelloParser.ValueContext,i)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterArray" ):
                listener.enterArray(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitArray" ):
                listener.exitArray(self)


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


    class Id_dereferenceContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)
        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterId_dereference" ):
                listener.enterId_dereference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitId_dereference" ):
                listener.exitId_dereference(self)


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
        self.enterRule(localctx, 16, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 97
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,7,self._ctx)
            if la_ == 1:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 69
                self.match(HelloParser.INT)
                pass

            elif la_ == 2:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 70
                self.match(HelloParser.REAL)
                pass

            elif la_ == 3:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 71
                self.match(HelloParser.TOINT)
                self.state = 72
                self.atom()
                pass

            elif la_ == 4:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 73
                self.match(HelloParser.TOREAL)
                self.state = 74
                self.atom()
                pass

            elif la_ == 5:
                localctx = HelloParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 75
                self.match(HelloParser.T__2)
                self.state = 76
                self.expr(0)
                self.state = 77
                self.match(HelloParser.T__3)
                pass

            elif la_ == 6:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 79
                self.match(HelloParser.ID)
                pass

            elif la_ == 7:
                localctx = HelloParser.Id_dereferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 80
                self.match(HelloParser.ID)
                self.state = 81
                self.match(HelloParser.T__0)
                self.state = 82
                self.expr(0)
                self.state = 83
                self.match(HelloParser.T__1)
                pass

            elif la_ == 8:
                localctx = HelloParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 85
                self.match(HelloParser.T__4)
                self.state = 92
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__2) | (1 << HelloParser.T__4) | (1 << HelloParser.ID) | (1 << HelloParser.TOINT) | (1 << HelloParser.TOREAL) | (1 << HelloParser.INT) | (1 << HelloParser.REAL) | (1 << HelloParser.STRING))) != 0):
                    self.state = 86
                    self.value()
                    self.state = 88
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HelloParser.T__5:
                        self.state = 87
                        self.match(HelloParser.T__5)


                    self.state = 94
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 95
                self.match(HelloParser.T__6)
                pass

            elif la_ == 9:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 96
                self.match(HelloParser.STRING)
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
        self.enterRule(localctx, 18, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
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
        self._predicates[7] = self.expr_sempred
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
         




