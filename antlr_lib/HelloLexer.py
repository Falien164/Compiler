# Generated from ./antlr_lib/Hello.g4 by ANTLR 4.9.2
from antlr4 import *
from io import StringIO
import sys
if sys.version_info[1] > 5:
    from typing import TextIO
else:
    from typing.io import TextIO



def serializedATN():
    with StringIO() as buf:
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2.")
        buf.write("\u0113\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\4-\t-\3\2")
        buf.write("\3\2\3\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3")
        buf.write("\b\3\b\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\13\3\13\3")
        buf.write("\13\3\f\3\f\3\f\3\f\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16")
        buf.write("\3\16\3\16\3\16\3\17\3\17\3\17\3\17\3\17\3\20\3\20\3\21")
        buf.write("\3\21\7\21\u008f\n\21\f\21\16\21\u0092\13\21\3\22\3\22")
        buf.write("\3\23\3\23\3\24\3\24\3\25\3\25\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\26\3\27\3\27\3\27\3\27\3\27\3\27\3\27\3\30\3\30\3\30")
        buf.write("\3\30\3\30\3\30\3\31\5\31\u00b0\n\31\3\31\3\31\3\32\6")
        buf.write("\32\u00b5\n\32\r\32\16\32\u00b6\3\33\3\33\3\33\3\33\3")
        buf.write("\34\5\34\u00be\n\34\3\34\3\34\3\35\3\35\7\35\u00c4\n\35")
        buf.write("\f\35\16\35\u00c7\13\35\3\35\3\35\3\36\3\36\3\36\3\36")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3 \3")
        buf.write("!\3!\3!\3!\3!\3!\3\"\3\"\3\"\3\"\3\"\3\"\3\"\3#\3#\3#")
        buf.write("\3#\3$\3$\3$\3$\3$\3%\3%\3%\3&\3&\3&\3\'\3\'\3(\3(\3)")
        buf.write("\3)\3)\3*\3*\3*\3+\3+\3,\6,\u0105\n,\r,\16,\u0106\3,\3")
        buf.write(",\3-\3-\7-\u010d\n-\f-\16-\u0110\13-\3-\3-\2\2.\3\3\5")
        buf.write("\4\7\5\t\6\13\7\r\b\17\t\21\n\23\13\25\f\27\r\31\16\33")
        buf.write("\17\35\20\37\21!\22#\23%\24\'\25)\26+\27-\30/\31\61\32")
        buf.write("\63\33\65\34\67\359\36;\37= ?!A\"C#E$G%I&K\'M(O)Q*S+U")
        buf.write(",W-Y.\3\2\b\4\2C\\c|\6\2\62;C\\aac|\3\2\62;\4\2$$^^\4")
        buf.write("\2\13\13\"\"\4\2\f\f\17\17\2\u0119\2\3\3\2\2\2\2\5\3\2")
        buf.write("\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13\3\2\2\2\2\r\3\2\2\2")
        buf.write("\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3\2\2\2\2\25\3\2\2\2\2")
        buf.write("\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2\2\2\2\35\3\2\2\2\2\37")
        buf.write("\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2%\3\2\2\2\2\'\3\2\2\2")
        buf.write("\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2\2/\3\2\2\2\2\61\3\2")
        buf.write("\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67\3\2\2\2\29\3\2\2\2")
        buf.write("\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2A\3\2\2\2\2C\3\2\2")
        buf.write("\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2\2K\3\2\2\2\2M\3\2")
        buf.write("\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2\2\2U\3\2\2\2\2W\3")
        buf.write("\2\2\2\2Y\3\2\2\2\3[\3\2\2\2\5]\3\2\2\2\7_\3\2\2\2\tb")
        buf.write("\3\2\2\2\13d\3\2\2\2\rf\3\2\2\2\17h\3\2\2\2\21k\3\2\2")
        buf.write("\2\23m\3\2\2\2\25o\3\2\2\2\27v\3\2\2\2\31z\3\2\2\2\33")
        buf.write("\177\3\2\2\2\35\u0085\3\2\2\2\37\u008a\3\2\2\2!\u008c")
        buf.write("\3\2\2\2#\u0093\3\2\2\2%\u0095\3\2\2\2\'\u0097\3\2\2\2")
        buf.write(")\u0099\3\2\2\2+\u009b\3\2\2\2-\u00a1\3\2\2\2/\u00a8\3")
        buf.write("\2\2\2\61\u00af\3\2\2\2\63\u00b4\3\2\2\2\65\u00b8\3\2")
        buf.write("\2\2\67\u00bd\3\2\2\29\u00c1\3\2\2\2;\u00ca\3\2\2\2=\u00ce")
        buf.write("\3\2\2\2?\u00d4\3\2\2\2A\u00db\3\2\2\2C\u00e1\3\2\2\2")
        buf.write("E\u00e8\3\2\2\2G\u00ec\3\2\2\2I\u00f1\3\2\2\2K\u00f4\3")
        buf.write("\2\2\2M\u00f7\3\2\2\2O\u00f9\3\2\2\2Q\u00fb\3\2\2\2S\u00fe")
        buf.write("\3\2\2\2U\u0101\3\2\2\2W\u0104\3\2\2\2Y\u010a\3\2\2\2")
        buf.write("[\\\7]\2\2\\\4\3\2\2\2]^\7_\2\2^\6\3\2\2\2_`\7h\2\2`a")
        buf.write("\7p\2\2a\b\3\2\2\2bc\7*\2\2c\n\3\2\2\2de\7.\2\2e\f\3\2")
        buf.write("\2\2fg\7+\2\2g\16\3\2\2\2hi\7/\2\2ij\7@\2\2j\20\3\2\2")
        buf.write("\2kl\7}\2\2l\22\3\2\2\2mn\7\177\2\2n\24\3\2\2\2op\7t\2")
        buf.write("\2pq\7g\2\2qr\7v\2\2rs\7w\2\2st\7t\2\2tu\7p\2\2u\26\3")
        buf.write("\2\2\2vw\7k\2\2wx\7p\2\2xy\7v\2\2y\30\3\2\2\2z{\7t\2\2")
        buf.write("{|\7g\2\2|}\7c\2\2}~\7n\2\2~\32\3\2\2\2\177\u0080\7r\2")
        buf.write("\2\u0080\u0081\7t\2\2\u0081\u0082\7k\2\2\u0082\u0083\7")
        buf.write("p\2\2\u0083\u0084\7v\2\2\u0084\34\3\2\2\2\u0085\u0086")
        buf.write("\7t\2\2\u0086\u0087\7g\2\2\u0087\u0088\7c\2\2\u0088\u0089")
        buf.write("\7f\2\2\u0089\36\3\2\2\2\u008a\u008b\7?\2\2\u008b \3\2")
        buf.write("\2\2\u008c\u0090\t\2\2\2\u008d\u008f\t\3\2\2\u008e\u008d")
        buf.write("\3\2\2\2\u008f\u0092\3\2\2\2\u0090\u008e\3\2\2\2\u0090")
        buf.write("\u0091\3\2\2\2\u0091\"\3\2\2\2\u0092\u0090\3\2\2\2\u0093")
        buf.write("\u0094\7-\2\2\u0094$\3\2\2\2\u0095\u0096\7,\2\2\u0096")
        buf.write("&\3\2\2\2\u0097\u0098\7/\2\2\u0098(\3\2\2\2\u0099\u009a")
        buf.write("\7\61\2\2\u009a*\3\2\2\2\u009b\u009c\7*\2\2\u009c\u009d")
        buf.write("\7k\2\2\u009d\u009e\7p\2\2\u009e\u009f\7v\2\2\u009f\u00a0")
        buf.write("\7+\2\2\u00a0,\3\2\2\2\u00a1\u00a2\7*\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7g\2\2\u00a4\u00a5\7c\2\2\u00a5\u00a6")
        buf.write("\7n\2\2\u00a6\u00a7\7+\2\2\u00a7.\3\2\2\2\u00a8\u00a9")
        buf.write("\7*\2\2\u00a9\u00aa\7u\2\2\u00aa\u00ab\7v\2\2\u00ab\u00ac")
        buf.write("\7t\2\2\u00ac\u00ad\7+\2\2\u00ad\60\3\2\2\2\u00ae\u00b0")
        buf.write("\7/\2\2\u00af\u00ae\3\2\2\2\u00af\u00b0\3\2\2\2\u00b0")
        buf.write("\u00b1\3\2\2\2\u00b1\u00b2\5\63\32\2\u00b2\62\3\2\2\2")
        buf.write("\u00b3\u00b5\t\4\2\2\u00b4\u00b3\3\2\2\2\u00b5\u00b6\3")
        buf.write("\2\2\2\u00b6\u00b4\3\2\2\2\u00b6\u00b7\3\2\2\2\u00b7\64")
        buf.write("\3\2\2\2\u00b8\u00b9\5\61\31\2\u00b9\u00ba\7\60\2\2\u00ba")
        buf.write("\u00bb\5\63\32\2\u00bb\66\3\2\2\2\u00bc\u00be\7\17\2\2")
        buf.write("\u00bd\u00bc\3\2\2\2\u00bd\u00be\3\2\2\2\u00be\u00bf\3")
        buf.write("\2\2\2\u00bf\u00c0\7\f\2\2\u00c08\3\2\2\2\u00c1\u00c5")
        buf.write("\7$\2\2\u00c2\u00c4\n\5\2\2\u00c3\u00c2\3\2\2\2\u00c4")
        buf.write("\u00c7\3\2\2\2\u00c5\u00c3\3\2\2\2\u00c5\u00c6\3\2\2\2")
        buf.write("\u00c6\u00c8\3\2\2\2\u00c7\u00c5\3\2\2\2\u00c8\u00c9\7")
        buf.write("$\2\2\u00c9:\3\2\2\2\u00ca\u00cb\7k\2\2\u00cb\u00cc\7")
        buf.write("h\2\2\u00cc\u00cd\7\"\2\2\u00cd<\3\2\2\2\u00ce\u00cf\7")
        buf.write("g\2\2\u00cf\u00d0\7n\2\2\u00d0\u00d1\7u\2\2\u00d1\u00d2")
        buf.write("\7g\2\2\u00d2\u00d3\7\"\2\2\u00d3>\3\2\2\2\u00d4\u00d5")
        buf.write("\7y\2\2\u00d5\u00d6\7j\2\2\u00d6\u00d7\7k\2\2\u00d7\u00d8")
        buf.write("\7n\2\2\u00d8\u00d9\7g\2\2\u00d9\u00da\7\"\2\2\u00da@")
        buf.write("\3\2\2\2\u00db\u00dc\7v\2\2\u00dc\u00dd\7t\2\2\u00dd\u00de")
        buf.write("\7w\2\2\u00de\u00df\7g\2\2\u00df\u00e0\7\"\2\2\u00e0B")
        buf.write("\3\2\2\2\u00e1\u00e2\7h\2\2\u00e2\u00e3\7c\2\2\u00e3\u00e4")
        buf.write("\7n\2\2\u00e4\u00e5\7u\2\2\u00e5\u00e6\7g\2\2\u00e6\u00e7")
        buf.write("\7\"\2\2\u00e7D\3\2\2\2\u00e8\u00e9\7q\2\2\u00e9\u00ea")
        buf.write("\7t\2\2\u00ea\u00eb\7\"\2\2\u00ebF\3\2\2\2\u00ec\u00ed")
        buf.write("\7c\2\2\u00ed\u00ee\7p\2\2\u00ee\u00ef\7f\2\2\u00ef\u00f0")
        buf.write("\7\"\2\2\u00f0H\3\2\2\2\u00f1\u00f2\7?\2\2\u00f2\u00f3")
        buf.write("\7?\2\2\u00f3J\3\2\2\2\u00f4\u00f5\7#\2\2\u00f5\u00f6")
        buf.write("\7?\2\2\u00f6L\3\2\2\2\u00f7\u00f8\7@\2\2\u00f8N\3\2\2")
        buf.write("\2\u00f9\u00fa\7>\2\2\u00faP\3\2\2\2\u00fb\u00fc\7@\2")
        buf.write("\2\u00fc\u00fd\7?\2\2\u00fdR\3\2\2\2\u00fe\u00ff\7>\2")
        buf.write("\2\u00ff\u0100\7?\2\2\u0100T\3\2\2\2\u0101\u0102\7#\2")
        buf.write("\2\u0102V\3\2\2\2\u0103\u0105\t\6\2\2\u0104\u0103\3\2")
        buf.write("\2\2\u0105\u0106\3\2\2\2\u0106\u0104\3\2\2\2\u0106\u0107")
        buf.write("\3\2\2\2\u0107\u0108\3\2\2\2\u0108\u0109\b,\2\2\u0109")
        buf.write("X\3\2\2\2\u010a\u010e\7%\2\2\u010b\u010d\n\7\2\2\u010c")
        buf.write("\u010b\3\2\2\2\u010d\u0110\3\2\2\2\u010e\u010c\3\2\2\2")
        buf.write("\u010e\u010f\3\2\2\2\u010f\u0111\3\2\2\2\u0110\u010e\3")
        buf.write("\2\2\2\u0111\u0112\b-\2\2\u0112Z\3\2\2\2\n\2\u0090\u00af")
        buf.write("\u00b6\u00bd\u00c5\u0106\u010e\3\b\2\2")
        return buf.getvalue()


class HelloLexer(Lexer):

    atn = ATNDeserializer().deserialize(serializedATN())

    decisionsToDFA = [ DFA(ds, i) for i, ds in enumerate(atn.decisionToState) ]

    T__0 = 1
    T__1 = 2
    T__2 = 3
    T__3 = 4
    T__4 = 5
    T__5 = 6
    T__6 = 7
    T__7 = 8
    T__8 = 9
    T__9 = 10
    T__10 = 11
    T__11 = 12
    STD_OUT = 13
    STD_IN = 14
    ASSIGN = 15
    ID = 16
    ADD = 17
    MUL = 18
    SUB = 19
    DIV = 20
    TOINT = 21
    TOREAL = 22
    TOSTR = 23
    INT = 24
    UINT = 25
    REAL = 26
    NEWLINE = 27
    STRING = 28
    IF = 29
    ELSE = 30
    WHILE = 31
    TRUE = 32
    FALSE = 33
    OR = 34
    AND = 35
    EQ = 36
    NEQ = 37
    GT = 38
    LT = 39
    GTEQ = 40
    LTEQ = 41
    NOT = 42
    WS = 43
    LINE_COMMENT = 44

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'fn'", "'('", "','", "')'", "'->'", "'{'", "'}'", 
            "'return'", "'int'", "'real'", "'print'", "'read'", "'='", "'+'", 
            "'*'", "'-'", "'/'", "'(int)'", "'(real)'", "'(str)'", "'if '", 
            "'else '", "'while '", "'true '", "'false '", "'or '", "'and '", 
            "'=='", "'!='", "'>'", "'<'", "'>='", "'<='", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "STD_OUT", "STD_IN", "ASSIGN", "ID", "ADD", "MUL", "SUB", "DIV", 
            "TOINT", "TOREAL", "TOSTR", "INT", "UINT", "REAL", "NEWLINE", 
            "STRING", "IF", "ELSE", "WHILE", "TRUE", "FALSE", "OR", "AND", 
            "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "NOT", "WS", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "T__11", "STD_OUT", "STD_IN", 
                  "ASSIGN", "ID", "ADD", "MUL", "SUB", "DIV", "TOINT", "TOREAL", 
                  "TOSTR", "INT", "UINT", "REAL", "NEWLINE", "STRING", "IF", 
                  "ELSE", "WHILE", "TRUE", "FALSE", "OR", "AND", "EQ", "NEQ", 
                  "GT", "LT", "GTEQ", "LTEQ", "NOT", "WS", "LINE_COMMENT" ]

    grammarFileName = "Hello.g4"

    def __init__(self, input=None, output:TextIO = sys.stdout):
        super().__init__(input, output)
        self.checkVersion("4.9.2")
        self._interp = LexerATNSimulator(self, self.atn, self.decisionsToDFA, PredictionContextCache())
        self._actions = None
        self._predicates = None


