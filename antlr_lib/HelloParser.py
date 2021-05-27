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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\3/")
        buf.write("\u011a\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7\t\7")
        buf.write("\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r\4\16")
        buf.write("\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23\t\23")
        buf.write("\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30\4\31")
        buf.write("\t\31\4\32\t\32\4\33\t\33\4\34\t\34\3\2\7\2:\n\2\f\2\16")
        buf.write("\2=\13\2\3\2\3\2\7\2A\n\2\f\2\16\2D\13\2\7\2F\n\2\f\2")
        buf.write("\16\2I\13\2\3\2\3\2\3\3\5\3N\n\3\3\3\7\3Q\n\3\f\3\16\3")
        buf.write("T\13\3\3\4\3\4\5\4X\n\4\3\5\3\5\3\5\3\5\3\5\3\5\3\5\5")
        buf.write("\5a\n\5\3\6\3\6\3\6\3\7\3\7\3\7\3\b\3\b\3\b\3\b\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\t\3\t\3\n\3\n\3\n\3\n\3\n\3\13\3\13\3")
        buf.write("\13\3\13\3\13\3\13\3\13\3\13\3\13\7\13\u0082\n\13\f\13")
        buf.write("\16\13\u0085\13\13\5\13\u0087\n\13\3\13\3\13\3\13\3\13")
        buf.write("\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3\f\7\f\u0095\n\f\f\f")
        buf.write("\16\f\u0098\13\f\5\f\u009a\n\f\3\f\3\f\3\r\3\r\3\16\6")
        buf.write("\16\u00a1\n\16\r\16\16\16\u00a2\3\16\3\16\3\17\3\17\3")
        buf.write("\20\3\20\3\21\3\21\3\22\3\22\3\23\3\23\3\23\3\23\3\23")
        buf.write("\7\23\u00b4\n\23\f\23\16\23\u00b7\13\23\3\23\3\23\5\23")
        buf.write("\u00bb\n\23\3\24\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3")
        buf.write("\26\3\26\5\26\u00c7\n\26\3\27\3\27\3\27\3\27\3\30\3\30")
        buf.write("\3\30\3\30\3\31\3\31\3\31\3\31\3\31\3\31\5\31\u00d7\n")
        buf.write("\31\3\32\3\32\3\32\5\32\u00dc\n\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32\3\32")
        buf.write("\3\32\3\32\3\32\7\32\u00f0\n\32\f\32\16\32\u00f3\13\32")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33\3\33")
        buf.write("\3\33\3\33\5\33\u010d\n\33\7\33\u010f\n\33\f\33\16\33")
        buf.write("\u0112\13\33\3\33\3\33\5\33\u0116\n\33\3\34\3\34\3\34")
        buf.write("\2\3\62\35\2\4\6\b\n\f\16\20\22\24\26\30\32\34\36 \"$")
        buf.write("&(*,.\60\62\64\66\2\b\3\2\16\17\4\2\25\25\27\27\4\2\24")
        buf.write("\24\26\26\3\2),\3\2\'(\3\2#$\2\u0128\2;\3\2\2\2\4R\3\2")
        buf.write("\2\2\6W\3\2\2\2\b`\3\2\2\2\nb\3\2\2\2\fe\3\2\2\2\16h\3")
        buf.write("\2\2\2\20o\3\2\2\2\22s\3\2\2\2\24x\3\2\2\2\26\u008f\3")
        buf.write("\2\2\2\30\u009d\3\2\2\2\32\u00a0\3\2\2\2\34\u00a6\3\2")
        buf.write("\2\2\36\u00a8\3\2\2\2 \u00aa\3\2\2\2\"\u00ac\3\2\2\2$")
        buf.write("\u00ae\3\2\2\2&\u00bc\3\2\2\2(\u00bf\3\2\2\2*\u00c6\3")
        buf.write("\2\2\2,\u00c8\3\2\2\2.\u00cc\3\2\2\2\60\u00d6\3\2\2\2")
        buf.write("\62\u00db\3\2\2\2\64\u0115\3\2\2\2\66\u0117\3\2\2\28:")
        buf.write("\7\36\2\298\3\2\2\2:=\3\2\2\2;9\3\2\2\2;<\3\2\2\2<G\3")
        buf.write("\2\2\2=;\3\2\2\2>B\5\6\4\2?A\7\36\2\2@?\3\2\2\2AD\3\2")
        buf.write("\2\2B@\3\2\2\2BC\3\2\2\2CF\3\2\2\2DB\3\2\2\2E>\3\2\2\2")
        buf.write("FI\3\2\2\2GE\3\2\2\2GH\3\2\2\2HJ\3\2\2\2IG\3\2\2\2JK\7")
        buf.write("\2\2\3K\3\3\2\2\2LN\5\b\5\2ML\3\2\2\2MN\3\2\2\2NO\3\2")
        buf.write("\2\2OQ\7\36\2\2PM\3\2\2\2QT\3\2\2\2RP\3\2\2\2RS\3\2\2")
        buf.write("\2S\5\3\2\2\2TR\3\2\2\2UX\5\24\13\2VX\5\20\t\2WU\3\2\2")
        buf.write("\2WV\3\2\2\2X\7\3\2\2\2Ya\5\n\6\2Za\5\f\7\2[a\5\16\b\2")
        buf.write("\\a\5\20\t\2]a\5$\23\2^a\5,\27\2_a\5\32\16\2`Y\3\2\2\2")
        buf.write("`Z\3\2\2\2`[\3\2\2\2`\\\3\2\2\2`]\3\2\2\2`^\3\2\2\2`_")
        buf.write("\3\2\2\2a\t\3\2\2\2bc\7\20\2\2cd\5\66\34\2d\13\3\2\2\2")
        buf.write("ef\7\21\2\2fg\7\23\2\2g\r\3\2\2\2hi\7\23\2\2ij\7\3\2\2")
        buf.write("jk\5\62\32\2kl\7\4\2\2lm\7\22\2\2mn\5\66\34\2n\17\3\2")
        buf.write("\2\2op\7\23\2\2pq\7\22\2\2qr\5\66\34\2r\21\3\2\2\2st\7")
        buf.write("\5\2\2tu\7\23\2\2uv\7\22\2\2vw\5\66\34\2w\23\3\2\2\2x")
        buf.write("y\7\6\2\2yz\5\"\22\2z\u0086\7\7\2\2{|\5\36\20\2|\u0083")
        buf.write("\7\23\2\2}~\7\b\2\2~\177\5\36\20\2\177\u0080\7\23\2\2")
        buf.write("\u0080\u0082\3\2\2\2\u0081}\3\2\2\2\u0082\u0085\3\2\2")
        buf.write("\2\u0083\u0081\3\2\2\2\u0083\u0084\3\2\2\2\u0084\u0087")
        buf.write("\3\2\2\2\u0085\u0083\3\2\2\2\u0086{\3\2\2\2\u0086\u0087")
        buf.write("\3\2\2\2\u0087\u0088\3\2\2\2\u0088\u0089\7\t\2\2\u0089")
        buf.write("\u008a\7\n\2\2\u008a\u008b\5\34\17\2\u008b\u008c\7\13")
        buf.write("\2\2\u008c\u008d\5\30\r\2\u008d\u008e\7\f\2\2\u008e\25")
        buf.write("\3\2\2\2\u008f\u0090\5\"\22\2\u0090\u0099\7\7\2\2\u0091")
        buf.write("\u0096\5\62\32\2\u0092\u0093\7\b\2\2\u0093\u0095\5\62")
        buf.write("\32\2\u0094\u0092\3\2\2\2\u0095\u0098\3\2\2\2\u0096\u0094")
        buf.write("\3\2\2\2\u0096\u0097\3\2\2\2\u0097\u009a\3\2\2\2\u0098")
        buf.write("\u0096\3\2\2\2\u0099\u0091\3\2\2\2\u0099\u009a\3\2\2\2")
        buf.write("\u009a\u009b\3\2\2\2\u009b\u009c\7\t\2\2\u009c\27\3\2")
        buf.write("\2\2\u009d\u009e\5\4\3\2\u009e\31\3\2\2\2\u009f\u00a1")
        buf.write("\7\r\2\2\u00a0\u009f\3\2\2\2\u00a1\u00a2\3\2\2\2\u00a2")
        buf.write("\u00a0\3\2\2\2\u00a2\u00a3\3\2\2\2\u00a3\u00a4\3\2\2\2")
        buf.write("\u00a4\u00a5\5\66\34\2\u00a5\33\3\2\2\2\u00a6\u00a7\5")
        buf.write("\36\20\2\u00a7\35\3\2\2\2\u00a8\u00a9\5 \21\2\u00a9\37")
        buf.write("\3\2\2\2\u00aa\u00ab\t\2\2\2\u00ab!\3\2\2\2\u00ac\u00ad")
        buf.write("\7\23\2\2\u00ad#\3\2\2\2\u00ae\u00af\7 \2\2\u00af\u00b5")
        buf.write("\5&\24\2\u00b0\u00b1\7!\2\2\u00b1\u00b2\7 \2\2\u00b2\u00b4")
        buf.write("\5&\24\2\u00b3\u00b0\3\2\2\2\u00b4\u00b7\3\2\2\2\u00b5")
        buf.write("\u00b3\3\2\2\2\u00b5\u00b6\3\2\2\2\u00b6\u00ba\3\2\2\2")
        buf.write("\u00b7\u00b5\3\2\2\2\u00b8\u00b9\7!\2\2\u00b9\u00bb\5")
        buf.write("*\26\2\u00ba\u00b8\3\2\2\2\u00ba\u00bb\3\2\2\2\u00bb%")
        buf.write("\3\2\2\2\u00bc\u00bd\5\62\32\2\u00bd\u00be\5(\25\2\u00be")
        buf.write("\'\3\2\2\2\u00bf\u00c0\5*\26\2\u00c0)\3\2\2\2\u00c1\u00c2")
        buf.write("\7\13\2\2\u00c2\u00c3\5\4\3\2\u00c3\u00c4\7\f\2\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c7\5\b\5\2\u00c6\u00c1\3\2\2\2")
        buf.write("\u00c6\u00c5\3\2\2\2\u00c7+\3\2\2\2\u00c8\u00c9\7\"\2")
        buf.write("\2\u00c9\u00ca\5.\30\2\u00ca\u00cb\5\60\31\2\u00cb-\3")
        buf.write("\2\2\2\u00cc\u00cd\7\7\2\2\u00cd\u00ce\5\62\32\2\u00ce")
        buf.write("\u00cf\7\t\2\2\u00cf/\3\2\2\2\u00d0\u00d7\3\2\2\2\u00d1")
        buf.write("\u00d2\7\13\2\2\u00d2\u00d3\5\4\3\2\u00d3\u00d4\7\f\2")
        buf.write("\2\u00d4\u00d7\3\2\2\2\u00d5\u00d7\5\b\5\2\u00d6\u00d0")
        buf.write("\3\2\2\2\u00d6\u00d1\3\2\2\2\u00d6\u00d5\3\2\2\2\u00d7")
        buf.write("\61\3\2\2\2\u00d8\u00d9\b\32\1\2\u00d9\u00dc\5\26\f\2")
        buf.write("\u00da\u00dc\5\64\33\2\u00db\u00d8\3\2\2\2\u00db\u00da")
        buf.write("\3\2\2\2\u00dc\u00f1\3\2\2\2\u00dd\u00de\f\t\2\2\u00de")
        buf.write("\u00df\t\3\2\2\u00df\u00f0\5\62\32\n\u00e0\u00e1\f\b\2")
        buf.write("\2\u00e1\u00e2\t\4\2\2\u00e2\u00f0\5\62\32\t\u00e3\u00e4")
        buf.write("\f\7\2\2\u00e4\u00e5\t\5\2\2\u00e5\u00f0\5\62\32\b\u00e6")
        buf.write("\u00e7\f\6\2\2\u00e7\u00e8\t\6\2\2\u00e8\u00f0\5\62\32")
        buf.write("\7\u00e9\u00ea\f\5\2\2\u00ea\u00eb\7&\2\2\u00eb\u00f0")
        buf.write("\5\62\32\6\u00ec\u00ed\f\4\2\2\u00ed\u00ee\7%\2\2\u00ee")
        buf.write("\u00f0\5\62\32\5\u00ef\u00dd\3\2\2\2\u00ef\u00e0\3\2\2")
        buf.write("\2\u00ef\u00e3\3\2\2\2\u00ef\u00e6\3\2\2\2\u00ef\u00e9")
        buf.write("\3\2\2\2\u00ef\u00ec\3\2\2\2\u00f0\u00f3\3\2\2\2\u00f1")
        buf.write("\u00ef\3\2\2\2\u00f1\u00f2\3\2\2\2\u00f2\63\3\2\2\2\u00f3")
        buf.write("\u00f1\3\2\2\2\u00f4\u0116\7\33\2\2\u00f5\u0116\7\35\2")
        buf.write("\2\u00f6\u00f7\7\30\2\2\u00f7\u0116\5\64\33\2\u00f8\u00f9")
        buf.write("\7\31\2\2\u00f9\u0116\5\64\33\2\u00fa\u00fb\7\32\2\2\u00fb")
        buf.write("\u0116\5\64\33\2\u00fc\u0116\t\7\2\2\u00fd\u00fe\7\23")
        buf.write("\2\2\u00fe\u00ff\7\3\2\2\u00ff\u0100\5\62\32\2\u0100\u0101")
        buf.write("\7\4\2\2\u0101\u0116\3\2\2\2\u0102\u0103\7\7\2\2\u0103")
        buf.write("\u0104\5\62\32\2\u0104\u0105\7\t\2\2\u0105\u0116\3\2\2")
        buf.write("\2\u0106\u0116\7\23\2\2\u0107\u0108\7\5\2\2\u0108\u0116")
        buf.write("\7\23\2\2\u0109\u0110\7\13\2\2\u010a\u010c\5\66\34\2\u010b")
        buf.write("\u010d\7\b\2\2\u010c\u010b\3\2\2\2\u010c\u010d\3\2\2\2")
        buf.write("\u010d\u010f\3\2\2\2\u010e\u010a\3\2\2\2\u010f\u0112\3")
        buf.write("\2\2\2\u0110\u010e\3\2\2\2\u0110\u0111\3\2\2\2\u0111\u0113")
        buf.write("\3\2\2\2\u0112\u0110\3\2\2\2\u0113\u0116\7\f\2\2\u0114")
        buf.write("\u0116\7\37\2\2\u0115\u00f4\3\2\2\2\u0115\u00f5\3\2\2")
        buf.write("\2\u0115\u00f6\3\2\2\2\u0115\u00f8\3\2\2\2\u0115\u00fa")
        buf.write("\3\2\2\2\u0115\u00fc\3\2\2\2\u0115\u00fd\3\2\2\2\u0115")
        buf.write("\u0102\3\2\2\2\u0115\u0106\3\2\2\2\u0115\u0107\3\2\2\2")
        buf.write("\u0115\u0109\3\2\2\2\u0115\u0114\3\2\2\2\u0116\65\3\2")
        buf.write("\2\2\u0117\u0118\5\62\32\2\u0118\67\3\2\2\2\30;BGMRW`")
        buf.write("\u0083\u0086\u0096\u0099\u00a2\u00b5\u00ba\u00c6\u00d6")
        buf.write("\u00db\u00ef\u00f1\u010c\u0110\u0115")
        return buf.getvalue()


class HelloParser ( Parser ):

    grammarFileName = "Hello.g4"

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    sharedContextCache = PredictionContextCache()

    literalNames = [ "<INVALID>", "'['", "']'", "'@'", "'fn'", "'('", "','", 
                     "')'", "'->'", "'{'", "'}'", "'return'", "'int'", "'real'", 
                     "'print'", "'read'", "'='", "<INVALID>", "'+'", "'*'", 
                     "'-'", "'/'", "'(int)'", "'(real)'", "'(str)'", "<INVALID>", 
                     "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                     "'if '", "'else '", "'while '", "'true '", "'false '", 
                     "'or '", "'and '", "'=='", "'!='", "'>'", "'<'", "'>='", 
                     "'<='", "'!'" ]

    symbolicNames = [ "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "<INVALID>", "<INVALID>", 
                      "<INVALID>", "<INVALID>", "STD_OUT", "STD_IN", "ASSIGN", 
                      "ID", "ADD", "MUL", "SUB", "DIV", "TOINT", "TOREAL", 
                      "TOSTR", "INT", "UINT", "REAL", "NEWLINE", "STRING", 
                      "IF", "ELSE", "WHILE", "TRUE", "FALSE", "OR", "AND", 
                      "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "NOT", "WS", 
                      "LINE_COMMENT" ]

    RULE_start = 0
    RULE_block = 1
    RULE_top_level_stat = 2
    RULE_stat = 3
    RULE_printf = 4
    RULE_scanf = 5
    RULE_array_assign = 6
    RULE_assign = 7
    RULE_global_assign = 8
    RULE_function_definiotion = 9
    RULE_function_call = 10
    RULE_function_body = 11
    RULE_return_stat = 12
    RULE_return_type = 13
    RULE_our_type = 14
    RULE_builtin_type = 15
    RULE_function_name = 16
    RULE_if_statement = 17
    RULE_condition_block = 18
    RULE_jump_block = 19
    RULE_stat_block = 20
    RULE_while_stat = 21
    RULE_loop_condition = 22
    RULE_repetitions = 23
    RULE_expr = 24
    RULE_atom = 25
    RULE_value = 26

    ruleNames =  [ "start", "block", "top_level_stat", "stat", "printf", 
                   "scanf", "array_assign", "assign", "global_assign", "function_definiotion", 
                   "function_call", "function_body", "return_stat", "return_type", 
                   "our_type", "builtin_type", "function_name", "if_statement", 
                   "condition_block", "jump_block", "stat_block", "while_stat", 
                   "loop_condition", "repetitions", "expr", "atom", "value" ]

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
    STD_OUT=14
    STD_IN=15
    ASSIGN=16
    ID=17
    ADD=18
    MUL=19
    SUB=20
    DIV=21
    TOINT=22
    TOREAL=23
    TOSTR=24
    INT=25
    UINT=26
    REAL=27
    NEWLINE=28
    STRING=29
    IF=30
    ELSE=31
    WHILE=32
    TRUE=33
    FALSE=34
    OR=35
    AND=36
    EQ=37
    NEQ=38
    GT=39
    LT=40
    GTEQ=41
    LTEQ=42
    NOT=43
    WS=44
    LINE_COMMENT=45

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

        def top_level_stat(self, i:int=None):
            if i is None:
                return self.getTypedRuleContexts(HelloParser.Top_level_statContext)
            else:
                return self.getTypedRuleContext(HelloParser.Top_level_statContext,i)


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
            self.state = 57
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.NEWLINE:
                self.state = 54
                self.match(HelloParser.NEWLINE)
                self.state = 59
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 69
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while _la==HelloParser.T__3 or _la==HelloParser.ID:
                self.state = 60
                self.top_level_stat()
                self.state = 64
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HelloParser.NEWLINE:
                    self.state = 61
                    self.match(HelloParser.NEWLINE)
                    self.state = 66
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 71
                self._errHandler.sync(self)
                _la = self._input.LA(1)

            self.state = 72
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
            self.state = 80
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__10) | (1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID) | (1 << HelloParser.NEWLINE) | (1 << HelloParser.IF) | (1 << HelloParser.WHILE))) != 0):
                self.state = 75
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__10) | (1 << HelloParser.STD_OUT) | (1 << HelloParser.STD_IN) | (1 << HelloParser.ID) | (1 << HelloParser.IF) | (1 << HelloParser.WHILE))) != 0):
                    self.state = 74
                    self.stat()


                self.state = 77
                self.match(HelloParser.NEWLINE)
                self.state = 82
                self._errHandler.sync(self)
                _la = self._input.LA(1)

        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Top_level_statContext(ParserRuleContext):
        __slots__ = 'parser'

        def __init__(self, parser, parent:ParserRuleContext=None, invokingState:int=-1):
            super().__init__(parent, invokingState)
            self.parser = parser

        def function_definiotion(self):
            return self.getTypedRuleContext(HelloParser.Function_definiotionContext,0)


        def assign(self):
            return self.getTypedRuleContext(HelloParser.AssignContext,0)


        def getRuleIndex(self):
            return HelloParser.RULE_top_level_stat

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterTop_level_stat" ):
                listener.enterTop_level_stat(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitTop_level_stat" ):
                listener.exitTop_level_stat(self)




    def top_level_stat(self):

        localctx = HelloParser.Top_level_statContext(self, self._ctx, self.state)
        self.enterRule(localctx, 4, self.RULE_top_level_stat)
        try:
            self.state = 85
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.T__3]:
                self.enterOuterAlt(localctx, 1)
                self.state = 83
                self.function_definiotion()
                pass
            elif token in [HelloParser.ID]:
                self.enterOuterAlt(localctx, 2)
                self.state = 84
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
        self.enterRule(localctx, 6, self.RULE_stat)
        try:
            self.state = 94
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,6,self._ctx)
            if la_ == 1:
                self.enterOuterAlt(localctx, 1)
                self.state = 87
                self.printf()
                pass

            elif la_ == 2:
                self.enterOuterAlt(localctx, 2)
                self.state = 88
                self.scanf()
                pass

            elif la_ == 3:
                self.enterOuterAlt(localctx, 3)
                self.state = 89
                self.array_assign()
                pass

            elif la_ == 4:
                self.enterOuterAlt(localctx, 4)
                self.state = 90
                self.assign()
                pass

            elif la_ == 5:
                self.enterOuterAlt(localctx, 5)
                self.state = 91
                self.if_statement()
                pass

            elif la_ == 6:
                self.enterOuterAlt(localctx, 6)
                self.state = 92
                self.while_stat()
                pass

            elif la_ == 7:
                self.enterOuterAlt(localctx, 7)
                self.state = 93
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
        self.enterRule(localctx, 8, self.RULE_printf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 96
            self.match(HelloParser.STD_OUT)
            self.state = 97
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
        self.enterRule(localctx, 10, self.RULE_scanf)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 99
            self.match(HelloParser.STD_IN)
            self.state = 100
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
        self.enterRule(localctx, 12, self.RULE_array_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 102
            self.match(HelloParser.ID)
            self.state = 103
            self.match(HelloParser.T__0)
            self.state = 104
            self.expr(0)
            self.state = 105
            self.match(HelloParser.T__1)
            self.state = 106
            self.match(HelloParser.ASSIGN)
            self.state = 107
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
        self.enterRule(localctx, 14, self.RULE_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 109
            self.match(HelloParser.ID)
            self.state = 110
            self.match(HelloParser.ASSIGN)
            self.state = 111
            self.value()
        except RecognitionException as re:
            localctx.exception = re
            self._errHandler.reportError(self, re)
            self._errHandler.recover(self, re)
        finally:
            self.exitRule()
        return localctx


    class Global_assignContext(ParserRuleContext):
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
            return HelloParser.RULE_global_assign

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterGlobal_assign" ):
                listener.enterGlobal_assign(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitGlobal_assign" ):
                listener.exitGlobal_assign(self)




    def global_assign(self):

        localctx = HelloParser.Global_assignContext(self, self._ctx, self.state)
        self.enterRule(localctx, 16, self.RULE_global_assign)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 113
            self.match(HelloParser.T__2)
            self.state = 114
            self.match(HelloParser.ID)
            self.state = 115
            self.match(HelloParser.ASSIGN)
            self.state = 116
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
        self.enterRule(localctx, 18, self.RULE_function_definiotion)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 118
            self.match(HelloParser.T__3)
            self.state = 119
            self.function_name()
            self.state = 120
            self.match(HelloParser.T__4)
            self.state = 132
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if _la==HelloParser.T__11 or _la==HelloParser.T__12:
                self.state = 121
                self.our_type()
                self.state = 122
                self.match(HelloParser.ID)
                self.state = 129
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HelloParser.T__5:
                    self.state = 123
                    self.match(HelloParser.T__5)
                    self.state = 124
                    self.our_type()
                    self.state = 125
                    self.match(HelloParser.ID)
                    self.state = 131
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 134
            self.match(HelloParser.T__6)
            self.state = 135
            self.match(HelloParser.T__7)
            self.state = 136
            self.return_type()
            self.state = 137
            self.match(HelloParser.T__8)
            self.state = 138
            self.function_body()
            self.state = 139
            self.match(HelloParser.T__9)
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
        self.enterRule(localctx, 20, self.RULE_function_call)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 141
            self.function_name()
            self.state = 142
            self.match(HelloParser.T__4)
            self.state = 151
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            if (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__2) | (1 << HelloParser.T__4) | (1 << HelloParser.T__8) | (1 << HelloParser.ID) | (1 << HelloParser.TOINT) | (1 << HelloParser.TOREAL) | (1 << HelloParser.TOSTR) | (1 << HelloParser.INT) | (1 << HelloParser.REAL) | (1 << HelloParser.STRING) | (1 << HelloParser.TRUE) | (1 << HelloParser.FALSE))) != 0):
                self.state = 143
                self.expr(0)
                self.state = 148
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while _la==HelloParser.T__5:
                    self.state = 144
                    self.match(HelloParser.T__5)
                    self.state = 145
                    self.expr(0)
                    self.state = 150
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)



            self.state = 153
            self.match(HelloParser.T__6)
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
        self.enterRule(localctx, 22, self.RULE_function_body)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 155
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
        self.enterRule(localctx, 24, self.RULE_return_stat)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 158 
            self._errHandler.sync(self)
            _la = self._input.LA(1)
            while True:
                self.state = 157
                self.match(HelloParser.T__10)
                self.state = 160 
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                if not (_la==HelloParser.T__10):
                    break

            self.state = 162
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
        self.enterRule(localctx, 26, self.RULE_return_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 164
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
        self.enterRule(localctx, 28, self.RULE_our_type)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 166
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
        self.enterRule(localctx, 30, self.RULE_builtin_type)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 168
            _la = self._input.LA(1)
            if not(_la==HelloParser.T__11 or _la==HelloParser.T__12):
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
        self.enterRule(localctx, 32, self.RULE_function_name)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 170
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
        self.enterRule(localctx, 34, self.RULE_if_statement)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 172
            self.match(HelloParser.IF)
            self.state = 173
            self.condition_block()
            self.state = 179
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,12,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    self.state = 174
                    self.match(HelloParser.ELSE)
                    self.state = 175
                    self.match(HelloParser.IF)
                    self.state = 176
                    self.condition_block() 
                self.state = 181
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,12,self._ctx)

            self.state = 184
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,13,self._ctx)
            if la_ == 1:
                self.state = 182
                self.match(HelloParser.ELSE)
                self.state = 183
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
        self.enterRule(localctx, 36, self.RULE_condition_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 186
            self.expr(0)
            self.state = 187
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
        self.enterRule(localctx, 38, self.RULE_jump_block)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 189
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
        self.enterRule(localctx, 40, self.RULE_stat_block)
        try:
            self.state = 196
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.T__8]:
                self.enterOuterAlt(localctx, 1)
                self.state = 191
                self.match(HelloParser.T__8)
                self.state = 192
                self.block()
                self.state = 193
                self.match(HelloParser.T__9)
                pass
            elif token in [HelloParser.T__10, HelloParser.STD_OUT, HelloParser.STD_IN, HelloParser.ID, HelloParser.IF, HelloParser.WHILE]:
                self.enterOuterAlt(localctx, 2)
                self.state = 195
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
        self.enterRule(localctx, 42, self.RULE_while_stat)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 198
            self.match(HelloParser.WHILE)
            self.state = 199
            self.loop_condition()
            self.state = 200
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
        self.enterRule(localctx, 44, self.RULE_loop_condition)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 202
            self.match(HelloParser.T__4)
            self.state = 203
            self.expr(0)
            self.state = 204
            self.match(HelloParser.T__6)
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
        self.enterRule(localctx, 46, self.RULE_repetitions)
        try:
            self.state = 212
            self._errHandler.sync(self)
            token = self._input.LA(1)
            if token in [HelloParser.NEWLINE, HelloParser.ELSE]:
                self.enterOuterAlt(localctx, 1)

                pass
            elif token in [HelloParser.T__8]:
                self.enterOuterAlt(localctx, 2)
                self.state = 207
                self.match(HelloParser.T__8)
                self.state = 208
                self.block()
                self.state = 209
                self.match(HelloParser.T__9)
                pass
            elif token in [HelloParser.T__10, HelloParser.STD_OUT, HelloParser.STD_IN, HelloParser.ID, HelloParser.IF, HelloParser.WHILE]:
                self.enterOuterAlt(localctx, 3)
                self.state = 211
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
        _startState = 48
        self.enterRecursionRule(localctx, 48, self.RULE_expr, _p)
        self._la = 0 # Token type
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 217
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,16,self._ctx)
            if la_ == 1:
                localctx = HelloParser.FunctionCallExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx

                self.state = 215
                self.function_call()
                pass

            elif la_ == 2:
                localctx = HelloParser.AtomExprContext(self, localctx)
                self._ctx = localctx
                _prevctx = localctx
                self.state = 216
                self.atom()
                pass


            self._ctx.stop = self._input.LT(-1)
            self.state = 239
            self._errHandler.sync(self)
            _alt = self._interp.adaptivePredict(self._input,18,self._ctx)
            while _alt!=2 and _alt!=ATN.INVALID_ALT_NUMBER:
                if _alt==1:
                    if self._parseListeners is not None:
                        self.triggerExitRuleEvent()
                    _prevctx = localctx
                    self.state = 237
                    self._errHandler.sync(self)
                    la_ = self._interp.adaptivePredict(self._input,17,self._ctx)
                    if la_ == 1:
                        localctx = HelloParser.MultiplicationExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 219
                        if not self.precpred(self._ctx, 7):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 7)")
                        self.state = 220
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.MUL or _la==HelloParser.DIV):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 221
                        self.expr(8)
                        pass

                    elif la_ == 2:
                        localctx = HelloParser.AdditiveExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 222
                        if not self.precpred(self._ctx, 6):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 6)")
                        self.state = 223
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.ADD or _la==HelloParser.SUB):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 224
                        self.expr(7)
                        pass

                    elif la_ == 3:
                        localctx = HelloParser.RelationalExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 225
                        if not self.precpred(self._ctx, 5):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 5)")
                        self.state = 226
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not((((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.GT) | (1 << HelloParser.LT) | (1 << HelloParser.GTEQ) | (1 << HelloParser.LTEQ))) != 0)):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 227
                        self.expr(6)
                        pass

                    elif la_ == 4:
                        localctx = HelloParser.EqualityExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 228
                        if not self.precpred(self._ctx, 4):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 4)")
                        self.state = 229
                        localctx.op = self._input.LT(1)
                        _la = self._input.LA(1)
                        if not(_la==HelloParser.EQ or _la==HelloParser.NEQ):
                            localctx.op = self._errHandler.recoverInline(self)
                        else:
                            self._errHandler.reportMatch(self)
                            self.consume()
                        self.state = 230
                        self.expr(5)
                        pass

                    elif la_ == 5:
                        localctx = HelloParser.AndExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 231
                        if not self.precpred(self._ctx, 3):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 3)")
                        self.state = 232
                        self.match(HelloParser.AND)
                        self.state = 233
                        self.expr(4)
                        pass

                    elif la_ == 6:
                        localctx = HelloParser.OrExprContext(self, HelloParser.ExprContext(self, _parentctx, _parentState))
                        self.pushNewRecursionContext(localctx, _startState, self.RULE_expr)
                        self.state = 234
                        if not self.precpred(self._ctx, 2):
                            from antlr4.error.Errors import FailedPredicateException
                            raise FailedPredicateException(self, "self.precpred(self._ctx, 2)")
                        self.state = 235
                        self.match(HelloParser.OR)
                        self.state = 236
                        self.expr(3)
                        pass

             
                self.state = 241
                self._errHandler.sync(self)
                _alt = self._interp.adaptivePredict(self._input,18,self._ctx)

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


    class IdGlobalReferenceContext(AtomContext):

        def __init__(self, parser, ctx:ParserRuleContext): # actually a HelloParser.AtomContext
            super().__init__(parser)
            self.copyFrom(ctx)

        def ID(self):
            return self.getToken(HelloParser.ID, 0)

        def enterRule(self, listener:ParseTreeListener):
            if hasattr( listener, "enterIdGlobalReference" ):
                listener.enterIdGlobalReference(self)

        def exitRule(self, listener:ParseTreeListener):
            if hasattr( listener, "exitIdGlobalReference" ):
                listener.exitIdGlobalReference(self)


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
        self.enterRule(localctx, 50, self.RULE_atom)
        self._la = 0 # Token type
        try:
            self.state = 275
            self._errHandler.sync(self)
            la_ = self._interp.adaptivePredict(self._input,21,self._ctx)
            if la_ == 1:
                localctx = HelloParser.IntContext(self, localctx)
                self.enterOuterAlt(localctx, 1)
                self.state = 242
                self.match(HelloParser.INT)
                pass

            elif la_ == 2:
                localctx = HelloParser.RealContext(self, localctx)
                self.enterOuterAlt(localctx, 2)
                self.state = 243
                self.match(HelloParser.REAL)
                pass

            elif la_ == 3:
                localctx = HelloParser.TointContext(self, localctx)
                self.enterOuterAlt(localctx, 3)
                self.state = 244
                self.match(HelloParser.TOINT)
                self.state = 245
                self.atom()
                pass

            elif la_ == 4:
                localctx = HelloParser.TorealContext(self, localctx)
                self.enterOuterAlt(localctx, 4)
                self.state = 246
                self.match(HelloParser.TOREAL)
                self.state = 247
                self.atom()
                pass

            elif la_ == 5:
                localctx = HelloParser.TostrContext(self, localctx)
                self.enterOuterAlt(localctx, 5)
                self.state = 248
                self.match(HelloParser.TOSTR)
                self.state = 249
                self.atom()
                pass

            elif la_ == 6:
                localctx = HelloParser.BooleanAtomContext(self, localctx)
                self.enterOuterAlt(localctx, 6)
                self.state = 250
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
                self.state = 251
                self.match(HelloParser.ID)
                self.state = 252
                self.match(HelloParser.T__0)
                self.state = 253
                self.expr(0)
                self.state = 254
                self.match(HelloParser.T__1)
                pass

            elif la_ == 8:
                localctx = HelloParser.ParContext(self, localctx)
                self.enterOuterAlt(localctx, 8)
                self.state = 256
                self.match(HelloParser.T__4)
                self.state = 257
                self.expr(0)
                self.state = 258
                self.match(HelloParser.T__6)
                pass

            elif la_ == 9:
                localctx = HelloParser.IdContext(self, localctx)
                self.enterOuterAlt(localctx, 9)
                self.state = 260
                self.match(HelloParser.ID)
                pass

            elif la_ == 10:
                localctx = HelloParser.IdGlobalReferenceContext(self, localctx)
                self.enterOuterAlt(localctx, 10)
                self.state = 261
                self.match(HelloParser.T__2)
                self.state = 262
                self.match(HelloParser.ID)
                pass

            elif la_ == 11:
                localctx = HelloParser.ArrayContext(self, localctx)
                self.enterOuterAlt(localctx, 11)
                self.state = 263
                self.match(HelloParser.T__8)
                self.state = 270
                self._errHandler.sync(self)
                _la = self._input.LA(1)
                while (((_la) & ~0x3f) == 0 and ((1 << _la) & ((1 << HelloParser.T__2) | (1 << HelloParser.T__4) | (1 << HelloParser.T__8) | (1 << HelloParser.ID) | (1 << HelloParser.TOINT) | (1 << HelloParser.TOREAL) | (1 << HelloParser.TOSTR) | (1 << HelloParser.INT) | (1 << HelloParser.REAL) | (1 << HelloParser.STRING) | (1 << HelloParser.TRUE) | (1 << HelloParser.FALSE))) != 0):
                    self.state = 264
                    self.value()
                    self.state = 266
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)
                    if _la==HelloParser.T__5:
                        self.state = 265
                        self.match(HelloParser.T__5)


                    self.state = 272
                    self._errHandler.sync(self)
                    _la = self._input.LA(1)

                self.state = 273
                self.match(HelloParser.T__9)
                pass

            elif la_ == 12:
                localctx = HelloParser.StringContext(self, localctx)
                self.enterOuterAlt(localctx, 12)
                self.state = 274
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
        self.enterRule(localctx, 52, self.RULE_value)
        try:
            self.enterOuterAlt(localctx, 1)
            self.state = 277
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
        self._predicates[24] = self.expr_sempred
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
         




