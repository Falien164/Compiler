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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3.")
        buf.write("\u00fb\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\3\2\3\2\3\2\3\3\5\39\n\3\3\3\7\3<\n\3")
        buf.write("\f\3\16\3?\13\3\3\4\3\4\3\4\3\4\3\4\3\4\3\4\3\4\5\4I\n")
        buf.write("\4\3\5\3\5\3\5\3\6\3\6\3\6\3\7\3\7\3\7\3\7\3\7\3\7\3\7")
        buf.write("\3\b\3\b\3\b\3\b\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\3\t\7")
        buf.write("\te\n\t\f\t\16\th\13\t\5\tj\n\t\3\t\3\t\3\t\3\t\3\t\3")
        buf.write("\t\3\t\3\n\3\n\3\n\3\n\3\n\7\nx\n\n\f\n\16\n{\13\n\5\n")
        buf.write("}\n\n\3\n\3\n\3\13\3\13\3\f\6\f\u0084\n\f\r\f\16\f\u0085")
        buf.write("\3\f\3\f\3\r\3\r\3\16\3\16\3\17\3\17\3\20\3\20\3\21\3")
        buf.write("\21\3\21\3\21\3\21\7\21\u0097\n\21\f\21\16\21\u009a\13")
        buf.write("\21\3\21\3\21\5\21\u009e\n\21\3\22\3\22\3\22\3\23\3\23")
        buf.write("\3\24\3\24\3\24\3\24\3\24\5\24\u00aa\n\24\3\25\3\25\3")
        buf.write("\25\3\25\3\26\3\26\3\26\3\26\3\27\3\27\3\27\3\27\3\27")
        buf.write("\3\27\5\27\u00ba\n\27\3\30\3\30\3\30\5\30\u00bf\n\30\3")
        buf.write("\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\30\3\30\3\30\3\30\7\30\u00d3\n\30\f")
        buf.write("\30\16\30\u00d6\13\30\3\31\3\31\3\31\3\31\3\31\3\31\3")
        buf.write("\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31\3\31")
        buf.write("\3\31\3\31\3\31\3\31\3\31\5\31\u00ee\n\31\7\31\u00f0\n")
        buf.write("\31\f\31\16\31\u00f3\13\31\3\31\3\31\5\31\u00f7\n\31\3")
        buf.write("\32\3\32\3\32\2\3.\33\2\4\6\b\n\f\16\20\22\24\26\30\32")
        buf.write("\34\36 \"$&(*,.\60\62\2\b\3\2\r\16\4\2\24\24\26\26\4\2")
        buf.write("\23\23\25\25\3\2(+\3\2&\'\3\2\"#\2\u0107\2\64\3\2\2\2")
        buf.write("\4=\3\2\2\2\6H\3\2\2\2\bJ\3\2\2\2\nM\3\2\2\2\fP\3\2\2")
        buf.write("\2\16W\3\2\2\2\20[\3\2\2\2\22r\3\2\2\2\24\u0080\3\2\2")
        buf.write("\2\26\u0083\3\2\2\2\30\u0089\3\2\2\2\32\u008b\3\2\2\2")
        buf.write("\34\u008d\3\2\2\2\36\u008f\3\2\2\2 \u0091\3\2\2\2\"\u009f")
        buf.write("\3\2\2\2$\u00a2\3\2\2\2&\u00a9\3\2\2\2(\u00ab\3\2\2\2")
        buf.write("*\u00af\3\2\2\2,\u00b9\3\2\2\2.\u00be\3\2\2\2\60\u00f6")
        buf.write("\3\2\2\2\62\u00f8\3\2\2\2\64\65\5\4\3\2\65\66\7\2\2\3")
        buf.write("\66\3\3\2\2\2\679\5\6\4\28\67\3\2\2\289\3\2\2\29:\3\2")
        buf.write("\2\2:<\7\35\2\2;8\3\2\2\2<?\3\2\2\2=;\3\2\2\2=>\3\2\2")
        buf.write("\2>\5\3\2\2\2?=\3\2\2\2@I\5\b\5\2AI\5\n\6\2BI\5\f\7\2")
        buf.write("CI\5\16\b\2DI\5 \21\2EI\5(\25\2FI\5\20\t\2GI\5\26\f\2")
        buf.write("H@\3\2\2\2HA\3\2\2\2HB\3\2\2\2HC\3\2\2\2HD\3\2\2\2HE\3")
        buf.write("\2\2\2HF\3\2\2\2HG\3\2\2\2I\7\3\2\2\2JK\7\17\2\2KL\5\62")
        buf.write("\32\2L\t\3\2\2\2MN\7\20\2\2NO\7\22\2\2O\13\3\2\2\2PQ\7")
        buf.write("\22\2\2QR\7\3\2\2RS\5.\30\2ST\7\4\2\2TU\7\21\2\2UV\5\62")
        buf.write("\32\2V\r\3\2\2\2WX\7\22\2\2XY\7\21\2\2YZ\5\62\32\2Z\17")
        buf.write("\3\2\2\2[\\\7\5\2\2\\]\5\36\20\2]i\7\6\2\2^_\5\32\16\2")
        buf.write("_f\7\22\2\2`a\7\7\2\2ab\5\32\16\2bc\7\22\2\2ce\3\2\2\2")
        buf.write("d`\3\2\2\2eh\3\2\2\2fd\3\2\2\2fg\3\2\2\2gj\3\2\2\2hf\3")
        buf.write("\2\2\2i^\3\2\2\2ij\3\2\2\2jk\3\2\2\2kl\7\b\2\2lm\7\t\2")
        buf.write("\2mn\5\30\r\2no\7\n\2\2op\5\24\13\2pq\7\13\2\2q\21\3\2")
        buf.write("\2\2rs\5\36\20\2s|\7\6\2\2ty\5.\30\2uv\7\7\2\2vx\5.\30")
        buf.write("\2wu\3\2\2\2x{\3\2\2\2yw\3\2\2\2yz\3\2\2\2z}\3\2\2\2{")
        buf.write("y\3\2\2\2|t\3\2\2\2|}\3\2\2\2}~\3\2\2\2~\177\7\b\2\2\177")
        buf.write("\23\3\2\2\2\u0080\u0081\5\4\3\2\u0081\25\3\2\2\2\u0082")
        buf.write("\u0084\7\f\2\2\u0083\u0082\3\2\2\2\u0084\u0085\3\2\2\2")
        buf.write("\u0085\u0083\3\2\2\2\u0085\u0086\3\2\2\2\u0086\u0087\3")
        buf.write("\2\2\2\u0087\u0088\5\62\32\2\u0088\27\3\2\2\2\u0089\u008a")
        buf.write("\5\32\16\2\u008a\31\3\2\2\2\u008b\u008c\5\34\17\2\u008c")
        buf.write("\33\3\2\2\2\u008d\u008e\t\2\2\2\u008e\35\3\2\2\2\u008f")
        buf.write("\u0090\7\22\2\2\u0090\37\3\2\2\2\u0091\u0092\7\37\2\2")
        buf.write("\u0092\u0098\5\"\22\2\u0093\u0094\7 \2\2\u0094\u0095\7")
        buf.write("\37\2\2\u0095\u0097\5\"\22\2\u0096\u0093\3\2\2\2\u0097")
        buf.write("\u009a\3\2\2\2\u0098\u0096\3\2\2\2\u0098\u0099\3\2\2\2")
        buf.write("\u0099\u009d\3\2\2\2\u009a\u0098\3\2\2\2\u009b\u009c\7")
        buf.write(" \2\2\u009c\u009e\5&\24\2\u009d\u009b\3\2\2\2\u009d\u009e")
        buf.write("\3\2\2\2\u009e!\3\2\2\2\u009f\u00a0\5.\30\2\u00a0\u00a1")
        buf.write("\5$\23\2\u00a1#\3\2\2\2\u00a2\u00a3\5&\24\2\u00a3%\3\2")
        buf.write("\2\2\u00a4\u00a5\7\n\2\2\u00a5\u00a6\5\4\3\2\u00a6\u00a7")
        buf.write("\7\13\2\2\u00a7\u00aa\3\2\2\2\u00a8\u00aa\5\6\4\2\u00a9")
        buf.write("\u00a4\3\2\2\2\u00a9\u00a8\3\2\2\2\u00aa\'\3\2\2\2\u00ab")
        buf.write("\u00ac\7!\2\2\u00ac\u00ad\5*\26\2\u00ad\u00ae\5,\27\2")
        buf.write("\u00ae)\3\2\2\2\u00af\u00b0\7\6\2\2\u00b0\u00b1\5.\30")
        buf.write("\2\u00b1\u00b2\7\b\2\2\u00b2+\3\2\2\2\u00b3\u00ba\3\2")
        buf.write("\2\2\u00b4\u00b5\7\n\2\2\u00b5\u00b6\5\4\3\2\u00b6\u00b7")
        buf.write("\7\13\2\2\u00b7\u00ba\3\2\2\2\u00b8\u00ba\5\6\4\2\u00b9")
        buf.write("\u00b3\3\2\2\2\u00b9\u00b4\3\2\2\2\u00b9\u00b8\3\2\2\2")
        buf.write("\u00ba-\3\2\2\2\u00bb\u00bc\b\30\1\2\u00bc\u00bf\5\22")
        buf.write("\n\2\u00bd\u00bf\5\60\31\2\u00be\u00bb\3\2\2\2\u00be\u00bd")
        buf.write("\3\2\2\2\u00bf\u00d4\3\2\2\2\u00c0\u00c1\f\t\2\2\u00c1")
        buf.write("\u00c2\t\3\2\2\u00c2\u00d3\5.\30\n\u00c3\u00c4\f\b\2\2")
        buf.write("\u00c4\u00c5\t\4\2\2\u00c5\u00d3\5.\30\t\u00c6\u00c7\f")
        buf.write("\7\2\2\u00c7\u00c8\t\5\2\2\u00c8\u00d3\5.\30\b\u00c9\u00ca")
        buf.write("\f\6\2\2\u00ca\u00cb\t\6\2\2\u00cb\u00d3\5.\30\7\u00cc")
        buf.write("\u00cd\f\5\2\2\u00cd\u00ce\7%\2\2\u00ce\u00d3\5.\30\6")
        buf.write("\u00cf\u00d0\f\4\2\2\u00d0\u00d1\7$\2\2\u00d1\u00d3\5")
        buf.write(".\30\5\u00d2\u00c0\3\2\2\2\u00d2\u00c3\3\2\2\2\u00d2\u00c6")
        buf.write("\3\2\2\2\u00d2\u00c9\3\2\2\2\u00d2\u00cc\3\2\2\2\u00d2")
        buf.write("\u00cf\3\2\2\2\u00d3\u00d6\3\2\2\2\u00d4\u00d2\3\2\2\2")
        buf.write("\u00d4\u00d5\3\2\2\2\u00d5/\3\2\2\2\u00d6\u00d4\3\2\2")
        buf.write("\2\u00d7\u00f7\7\32\2\2\u00d8\u00f7\7\34\2\2\u00d9\u00da")
        buf.write("\7\27\2\2\u00da\u00f7\5\60\31\2\u00db\u00dc\7\30\2\2\u00dc")
        buf.write("\u00f7\5\60\31\2\u00dd\u00de\7\31\2\2\u00de\u00f7\5\60")
        buf.write("\31\2\u00df\u00f7\t\7\2\2\u00e0\u00e1\7\22\2\2\u00e1\u00e2")
        buf.write("\7\3\2\2\u00e2\u00e3\5.\30\2\u00e3\u00e4\7\4\2\2\u00e4")
        buf.write("\u00f7\3\2\2\2\u00e5\u00e6\7\6\2\2\u00e6\u00e7\5.\30\2")
        buf.write("\u00e7\u00e8\7\b\2\2\u00e8\u00f7\3\2\2\2\u00e9\u00f7\7")
        buf.write("\22\2\2\u00ea\u00f1\7\n\2\2\u00eb\u00ed\5\62\32\2\u00ec")
        buf.write("\u00ee\7\7\2\2\u00ed\u00ec\3\2\2\2\u00ed\u00ee\3\2\2\2")
        buf.write("\u00ee\u00f0\3\2\2\2\u00ef\u00eb\3\2\2\2\u00f0\u00f3\3")
        buf.write("\2\2\2\u00f1\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\u00f4")
        buf.write("\3\2\2\2\u00f3\u00f1\3\2\2\2\u00f4\u00f7\7\13\2\2\u00f5")
        buf.write("\u00f7\7\36\2\2\u00f6\u00d7\3\2\2\2\u00f6\u00d8\3\2\2")
        buf.write("\2\u00f6\u00d9\3\2\2\2\u00f6\u00db\3\2\2\2\u00f6\u00dd")
        buf.write("\3\2\2\2\u00f6\u00df\3\2\2\2\u00f6\u00e0\3\2\2\2\u00f6")
        buf.write("\u00e5\3\2\2\2\u00f6\u00e9\3\2\2\2\u00f6\u00ea\3\2\2\2")
        buf.write("\u00f6\u00f5\3\2\2\2\u00f7\61\3\2\2\2\u00f8\u00f9\5.\30")
        buf.write("\2\u00f9\63\3\2\2\2\248=Hfiy|\u0085\u0098\u009d\u00a9")
        buf.write("\u00b9\u00be\u00d2\u00d4\u00ed\u00f1\u00f6")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'fn'", "'('", "','", "')'", 
                     "'->'", "'{'", "'}'", "'return'", "'int'", "'real'", 
                     "'print'", "'read'", "'='", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'(int)'", "'(real)'", "'(str)'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if '", "'else '", "'while '", "'true '", "'false '", 
                     "'or '", "'and '", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "STD_OUT", "STD_IN", "ASSIGN", "ID", 
                      "ADD", "MUL", "SUB", "DIV", "TOINT", "TOREAL", "TOSTR", 
                      "INT", "UINT", "REAL", "NEWLINE", "STRING", "IF", 
                      "ELSE", "WHILE", "TRUE", "FALSE", "OR", "AND", "EQ", 
                      "NEQ", "GT", "LT", "GTEQ", "LTEQ", "NOT", "WS", "LINE_COMMENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_stat = 2
    RULE_printf = 3
    RULE_scanf = 4
    RULE_array_assign = 5
    RULE_assign = 6
    RULE_function_definiotion = 7
    RULE_function_call = 8
    RULE_function_body = 9
    RULE_return_stat = 10
    RULE_return_type = 11
    RULE_our_type = 12
    RULE_builtin_type = 13
    RULE_function_name = 14
    RULE_if_statement = 15
    RULE_condition_block = 16
    RULE_jump_block = 17
    RULE_stat_block = 18
    RULE_while_stat = 19
    RULE_loop_condition = 20
    RULE_repetitions = 21
    RULE_expr = 22
    RULE_atom = 23
    RULE_value = 24

    ruleNames =  [ "start", "block", "stat", "printf", "scanf", "array_assign", 
                   "assign", "function_definiotion", "function_call", "function_body", 
                   "return_stat", "return_type", "our_type", "builtin_type", 
                   "function_name", "if_statement", "condition_block", "jump_block", 
                   "stat_block", "while_stat", "loop_condition", "repetitions", 
                   "expr", "atom", "value" ]

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
    STD_OUT=13
    STD_IN=14
    ASSIGN=15
    ID=16
    ADD=17
    MUL=18
    SUB=19
    DIV=20
    TOINT=21
    TOREAL=22
    TOSTR=23
    INT=24
    UINT=25
    REAL=26
    NEWLINE=27
    STRING=28
    IF=29
    ELSE=30
    WHILE=31
    TRUE=32
    FALSE=33
    OR=34
    AND=35
    EQ=36
    NEQ=37
    GT=38
    LT=39
    GTEQ=40
    LTEQ=41
    NOT=42
    WS=43
    LINE_COMMENT=44

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
            self.state = 50
            self.block()
            self.state = 51
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
            self.state = 59
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__2) | (1 << HelloParser.T__9) | (1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE) | (1 << HelloParser.IF) | (1 << HelloParser.WHILE))) != 0):
                self.state = 54
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__2) | (1 << HelloParser.T__9) | (1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID) | (1 << HelloParser.IF) | (1 << HelloParser.WHILE))) != 0):
                    self.state = 53
                    self.stat()


                self.state = 56
                self.match(HelloParser.NEWLINE)
                self.state = 61
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


        def if_statement(self):
            return self.getTypedRuleContext(HelloParser.If_statementContext,0)


        def while_stat(self):
            return self.getTypedRuleContext(HelloParser.While_statContext,0)


        def function_definiotion(self):
            return self.getTypedRuleContext(HelloParser.Function_definiotionContext,0)


        def return_stat(self):
            return self.getTypedRuleContext(HelloParser.Return_statContext,0)


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
            self.state = 70
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,2,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 62
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 63
                self.scanf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 64
                self.array_assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 65
                self.assign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 66
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 67
                self.while_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 68
                self.function_definiotion()
                pass

            elif la_ == 8:
                self.enterOuterAlt(localctx, 8)
                self.state = 69
                self.return_stat()
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
            self.state = 72
            self.match(HelloParser.STD_OUT)
            self.state = 73
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
            self.state = 75
            self.match(HelloParser.STD_IN)
            self.state = 76
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
            self.state = 78
            self.match(HelloParser.ID)
            self.state = 79
            self.match(HelloParser.T__0)
            self.state = 80
            self.expr(0)
            self.state = 81
            self.match(HelloParser.T__1)
            self.state = 82
            self.match(HelloParser.ASSIGN)
            self.state = 83
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
            self.state = 85
            self.match(HelloParser.ID)
            self.state = 86
            self.match(HelloParser.ASSIGN)
            self.state = 87
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_definiotionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_name(self):
            return self.getTypedRuleContext(HelloParser.Function_nameContext,0)


        def return_type(self):
            return self.getTypedRuleContext(HelloParser.Return_typeContext,0)


        def function_body(self):
            return self.getTypedRuleContext(HelloParser.Function_bodyContext,0)


        def our_type(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Our_typeContext)
            else:
                return self.getTypedRuleContext(HelloParser.Our_typeContext,i)


        def ID(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ID)
            else:
                return self.getToken(HelloParser.ID, i)

        def getRuleIndex(self):
            return HelloParser.RULE_function_definiotion

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_definiotion" ):
                listener.enterFunction_definiotion(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_definiotion" ):
                listener.exitFunction_definiotion(self)




    def function_definiotion(self):

        localctx = HelloParser.Function_definiotionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 14, self.RULE_function_definiotion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 89
            self.match(HelloParser.T__2)
            self.state = 90
            self.function_name()
            self.state = 91
            self.match(HelloParser.T__3)
            self.state = 103
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HelloParser.T__10 or _la==HelloParser.T__11:
                self.state = 92
                self.our_type()
                self.state = 93
                self.match(HelloParser.ID)
                self.state = 100
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HelloParser.T__4:
                    self.state = 94
                    self.match(HelloParser.T__4)
                    self.state = 95
                    self.our_type()
                    self.state = 96
                    self.match(HelloParser.ID)
                    self.state = 102
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 105
            self.match(HelloParser.T__5)
            self.state = 106
            self.match(HelloParser.T__6)
            self.state = 107
            self.return_type()
            self.state = 108
            self.match(HelloParser.T__7)
            self.state = 109
            self.function_body()
            self.state = 110
            self.match(HelloParser.T__8)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_callContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_name(self):
            return self.getTypedRuleContext(HelloParser.Function_nameContext,0)


        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)


        def getRuleIndex(self):
            return HelloParser.RULE_function_call

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_call" ):
                listener.enterFunction_call(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_call" ):
                listener.exitFunction_call(self)




    def function_call(self):

        localctx = HelloParser.Function_callContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 112
            self.function_name()
            self.state = 113
            self.match(HelloParser.T__3)
            self.state = 122
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__3) | (1 << HelloParser.T__7) | (1 << HelloParser.ID) | (1 << HelloParser.TOINT) | (1 << HelloParser.TOREAL) | (1 << HelloParser.TOSTR) | (1 << HelloParser.INT) | (1 << HelloParser.REAL) | (1 << HelloParser.STRING) | (1 << HelloParser.TRUE) | (1 << HelloParser.FALSE))) != 0):
                self.state = 114
                self.expr(0)
                self.state = 119
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HelloParser.T__4:
                    self.state = 115
                    self.match(HelloParser.T__4)
                    self.state = 116
                    self.expr(0)
                    self.state = 121
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 124
            self.match(HelloParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Function_bodyContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(HelloParser.BlockContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_function_body

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_body" ):
                listener.enterFunction_body(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_body" ):
                listener.exitFunction_body(self)




    def function_body(self):

        localctx = HelloParser.Function_bodyContext(self, self._ctx, self.state)
        self.enterRule(localctx, 18, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 126
            self.block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def value(self):
            return self.getTypedRuleContext(HelloParser.ValueContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_return_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_stat" ):
                listener.enterReturn_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_stat" ):
                listener.exitReturn_stat(self)




    def return_stat(self):

        localctx = HelloParser.Return_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 20, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 129 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 128
                self.match(HelloParser.T__9)
                self.state = 131 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.T__9):
                    break

            self.state = 133
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Return_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def our_type(self):
            return self.getTypedRuleContext(HelloParser.Our_typeContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_return_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterReturn_type" ):
                listener.enterReturn_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitReturn_type" ):
                listener.exitReturn_type(self)




    def return_type(self):

        localctx = HelloParser.Return_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 22, self.RULE_return_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 135
            self.our_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Our_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def builtin_type(self):
            return self.getTypedRuleContext(HelloParser.Builtin_typeContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_our_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOur_type" ):
                listener.enterOur_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOur_type" ):
                listener.exitOur_type(self)




    def our_type(self):

        localctx = HelloParser.Our_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 24, self.RULE_our_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 137
            self.builtin_type()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Builtin_typeContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_builtin_type

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBuiltin_type" ):
                listener.enterBuiltin_type(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBuiltin_type" ):
                listener.exitBuiltin_type(self)




    def builtin_type(self):

        localctx = HelloParser.Builtin_typeContext(self, self._ctx, self.state)
        self.enterRule(localctx, 26, self.RULE_builtin_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 139
            _la = self._input.LA(1)
            if not(_la==HelloParser.T__10 or _la==HelloParser.T__11):
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


    class Function_nameContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def getRuleIndex(self):
            return HelloParser.RULE_function_name

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunction_name" ):
                listener.enterFunction_name(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunction_name" ):
                listener.exitFunction_name(self)




    def function_name(self):

        localctx = HelloParser.Function_nameContext(self, self._ctx, self.state)
        self.enterRule(localctx, 28, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.match(HelloParser.ID)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class If_statementContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def IF(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.IF)
            else:
                return self.getToken(HelloParser.IF, i)

        def condition_block(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Condition_blockContext)
            else:
                return self.getTypedRuleContext(HelloParser.Condition_blockContext,i)


        def ELSE(self, i:int=None):
            if i is None:
                return self.getTokens(HelloParser.ELSE)
            else:
                return self.getToken(HelloParser.ELSE, i)

        def stat_block(self):
            return self.getTypedRuleContext(HelloParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_if_statement

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIf_statement" ):
                listener.enterIf_statement(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIf_statement" ):
                listener.exitIf_statement(self)




    def if_statement(self):

        localctx = HelloParser.If_statementContext(self, self._ctx, self.state)
        self.enterRule(localctx, 30, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 143
            self.match(HelloParser.IF)
            self.state = 144
            self.condition_block()
            self.state = 150
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,8,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 145
                    self.match(HelloParser.ELSE)
                    self.state = 146
                    self.match(HelloParser.IF)
                    self.state = 147
                    self.condition_block() 
                self.state = 152
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,8,self._ctx)

            self.state = 155
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,9,self._ctx)
            if la_ == 1:
                self.state = 153
                self.match(HelloParser.ELSE)
                self.state = 154
                self.stat_block()


        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Condition_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def jump_block(self):
            return self.getTypedRuleContext(HelloParser.Jump_blockContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_condition_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterCondition_block" ):
                listener.enterCondition_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitCondition_block" ):
                listener.exitCondition_block(self)




    def condition_block(self):

        localctx = HelloParser.Condition_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 32, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 157
            self.expr(0)
            self.state = 158
            self.jump_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Jump_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def stat_block(self):
            return self.getTypedRuleContext(HelloParser.Stat_blockContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_jump_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterJump_block" ):
                listener.enterJump_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitJump_block" ):
                listener.exitJump_block(self)




    def jump_block(self):

        localctx = HelloParser.Jump_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 34, self.RULE_jump_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 160
            self.stat_block()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Stat_blockContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(HelloParser.BlockContext,0)


        def stat(self):
            return self.getTypedRuleContext(HelloParser.StatContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_stat_block

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterStat_block" ):
                listener.enterStat_block(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitStat_block" ):
                listener.exitStat_block(self)




    def stat_block(self):

        localctx = HelloParser.Stat_blockContext(self, self._ctx, self.state)
        self.enterRule(localctx, 36, self.RULE_stat_block)
        try:
            self.state = 167
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.T__7]:
                self.enterOuterAlt(localctx, 1)
                self.state = 162
                self.match(HelloParser.T__7)
                self.state = 163
                self.block()
                self.state = 164
                self.match(HelloParser.T__8)
                pass
            elif token in [HelloParser.T__2, HelloParser.T__9, HelloParser.STD_OUT, HelloParser.STD_IN, HelloParser.ID, HelloParser.IF, HelloParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 166
                self.stat()
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


    class While_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def WHILE(self):
            return self.getToken(HelloParser.WHILE, 0)

        def loop_condition(self):
            return self.getTypedRuleContext(HelloParser.Loop_conditionContext,0)


        def repetitions(self):
            return self.getTypedRuleContext(HelloParser.RepetitionsContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_while_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterWhile_stat" ):
                listener.enterWhile_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitWhile_stat" ):
                listener.exitWhile_stat(self)




    def while_stat(self):

        localctx = HelloParser.While_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 38, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 169
            self.match(HelloParser.WHILE)
            self.state = 170
            self.loop_condition()
            self.state = 171
            self.repetitions()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Loop_conditionContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def expr(self):
            return self.getTypedRuleContext(HelloParser.ExprContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_loop_condition

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterLoop_condition" ):
                listener.enterLoop_condition(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitLoop_condition" ):
                listener.exitLoop_condition(self)




    def loop_condition(self):

        localctx = HelloParser.Loop_conditionContext(self, self._ctx, self.state)
        self.enterRule(localctx, 40, self.RULE_loop_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 173
            self.match(HelloParser.T__3)
            self.state = 174
            self.expr(0)
            self.state = 175
            self.match(HelloParser.T__5)
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class RepetitionsContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def block(self):
            return self.getTypedRuleContext(HelloParser.BlockContext,0)


        def stat(self):
            return self.getTypedRuleContext(HelloParser.StatContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_repetitions

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRepetitions" ):
                listener.enterRepetitions(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRepetitions" ):
                listener.exitRepetitions(self)




    def repetitions(self):

        localctx = HelloParser.RepetitionsContext(self, self._ctx, self.state)
        self.enterRule(localctx, 42, self.RULE_repetitions)
        try:
            self.state = 183
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.NEWLINE, HelloParser.ELSE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [HelloParser.T__7]:
                self.enterOuterAlt(localctx, 2)
                self.state = 178
                self.match(HelloParser.T__7)
                self.state = 179
                self.block()
                self.state = 180
                self.match(HelloParser.T__8)
                pass
            elif token in [HelloParser.T__2, HelloParser.T__9, HelloParser.STD_OUT, HelloParser.STD_IN, HelloParser.ID, HelloParser.IF, HelloParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 182
                self.stat()
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


    class ExprContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser


        def getRuleIndex(self):
            return HelloParser.RULE_expr

     
        def copyFrom(self, ctx:ParserRuleContext):
            super().copyFrom(ctx)


    class FunctionCallExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def function_call(self):
            return self.getTypedRuleContext(HelloParser.Function_callContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterFunctionCallExpr" ):
                listener.enterFunctionCallExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitFunctionCallExpr" ):
                listener.exitFunctionCallExpr(self)


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


    class OrExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def OR(self):
            return self.getToken(HelloParser.OR, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterOrExpr" ):
                listener.enterOrExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitOrExpr" ):
                listener.exitOrExpr(self)


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


    class RelationalExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def LTEQ(self):
            return self.getToken(HelloParser.LTEQ, 0)
        def GTEQ(self):
            return self.getToken(HelloParser.GTEQ, 0)
        def LT(self):
            return self.getToken(HelloParser.LT, 0)
        def GT(self):
            return self.getToken(HelloParser.GT, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterRelationalExpr" ):
                listener.enterRelationalExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitRelationalExpr" ):
                listener.exitRelationalExpr(self)


    class EqualityExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.op = None # Token
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def EQ(self):
            return self.getToken(HelloParser.EQ, 0)
        def NEQ(self):
            return self.getToken(HelloParser.NEQ, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterEqualityExpr" ):
                listener.enterEqualityExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitEqualityExpr" ):
                listener.exitEqualityExpr(self)


    class AndExprContext(ExprContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.ExprContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def expr(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.ExprContext)
            else:
                return self.getTypedRuleContext(HelloParser.ExprContext,i)

        def AND(self):
            return self.getToken(HelloParser.AND, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterAndExpr" ):
                listener.enterAndExpr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitAndExpr" ):
                listener.exitAndExpr(self)



    def expr(self, _p:int=0):
        _parentctx = self._ctx
        _parentState = self.state
        localctx = HelloParser.ExprContext(self, self._ctx, _parentState)
        _prevctx = localctx
        _startState = 44
        self.enterRecursionRule(localctx, 44, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 188
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,12,self._ctx)
            if la_ == 1:
                localctx = HelloParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 186
                self.function_call()
                pass

            elif la_ == 2:
                localctx = HelloParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 187
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 210
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,14,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 208
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.MultiplicationExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 190
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 191
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.MUL or _la==HelloParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 192
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.AdditiveExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 193
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 194
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.ADD or _la==HelloParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 195
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = HelloParser.RelationalExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 196
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 197
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.GT) | (1 << HelloParser.LT) | (1 << HelloParser.GTEQ) | (1 << HelloParser.LTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 198
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = HelloParser.EqualityExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 199
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 200
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.EQ or _la==HelloParser.NEQ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 201
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = HelloParser.AndExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 202
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 203
                        self.match(HelloParser.AND)
                        self.state = 204
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = HelloParser.OrExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 205
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 206
                        self.match(HelloParser.OR)
                        self.state = 207
                        self.expr(3)
                        pass

             
                self.state = 212
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,14,self._ctx)

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



    class TostrContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TOSTR(self):
            return self.getToken(HelloParser.TOSTR, 0)
        def atom(self):
            return self.getTypedRuleContext(HelloParser.AtomContext,0)


        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTostr" ):
                listener.enterTostr(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTostr" ):
                listener.exitTostr(self)


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


    class BooleanAtomContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def TRUE(self):
            return self.getToken(HelloParser.TRUE, 0)
        def FALSE(self):
            return self.getToken(HelloParser.FALSE, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterBooleanAtom" ):
                listener.enterBooleanAtom(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitBooleanAtom" ):
                listener.exitBooleanAtom(self)


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
        self.enterRule(localctx, 46, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 244
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
            if la_ == 1:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 213
                self.match(HelloParser.INT)
                pass

            elif la_ == 2:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 214
                self.match(HelloParser.REAL)
                pass

            elif la_ == 3:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 215
                self.match(HelloParser.TOINT)
                self.state = 216
                self.atom()
                pass

            elif la_ == 4:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 217
                self.match(HelloParser.TOREAL)
                self.state = 218
                self.atom()
                pass

            elif la_ == 5:
                localctx = HelloParser.TostrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 219
                self.match(HelloParser.TOSTR)
                self.state = 220
                self.atom()
                pass

            elif la_ == 6:
                localctx = HelloParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 221
                _la = self._input.LA(1)
                if not(_la==HelloParser.TRUE or _la==HelloParser.FALSE):
                    self._errHandler.recoverInline(self)
                else:
                    self._errHandler.reportMatch(self)
                    self.consume()
                pass

            elif la_ == 7:
                localctx = HelloParser.Id_dereferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 7)
                self.state = 222
                self.match(HelloParser.ID)
                self.state = 223
                self.match(HelloParser.T__0)
                self.state = 224
                self.expr(0)
                self.state = 225
                self.match(HelloParser.T__1)
                pass

            elif la_ == 8:
                localctx = HelloParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 227
                self.match(HelloParser.T__3)
                self.state = 228
                self.expr(0)
                self.state = 229
                self.match(HelloParser.T__5)
                pass

            elif la_ == 9:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 231
                self.match(HelloParser.ID)
                pass

            elif la_ == 10:
                localctx = HelloParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 232
                self.match(HelloParser.T__7)
                self.state = 239
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__3) | (1 << HelloParser.T__7) | (1 << HelloParser.ID) | (1 << HelloParser.TOINT) | (1 << HelloParser.TOREAL) | (1 << HelloParser.TOSTR) | (1 << HelloParser.INT) | (1 << HelloParser.REAL) | (1 << HelloParser.STRING) | (1 << HelloParser.TRUE) | (1 << HelloParser.FALSE))) != 0):
                    self.state = 233
                    self.value()
                    self.state = 235
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HelloParser.T__4:
                        self.state = 234
                        self.match(HelloParser.T__4)


                    self.state = 241
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 242
                self.match(HelloParser.T__8)
                pass

            elif la_ == 11:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 243
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
        self.enterRule(localctx, 48, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 246
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
        self._predicates[22] = self.expr_sempred
        pred = self._predicates.get(ruleIndex, None)
        if pred is None:
            raise Exception("No predicate with index:" + str(ruleIndex))
        else:
            return pred(localctx, predIndex)

    def expr_sempred(self, localctx:ExprContext, predIndex:int):
            if predIndex == 0:
                return self.precpred(self._ctx, 7)
         

            if predIndex == 1:
                return self.precpred(self._ctx, 6)
         

            if predIndex == 2:
                return self.precpred(self._ctx, 5)
         

            if predIndex == 3:
                return self.precpred(self._ctx, 4)
         

            if predIndex == 4:
                return self.precpred(self._ctx, 3)
         

            if predIndex == 5:
                return self.precpred(self._ctx, 2)
         




