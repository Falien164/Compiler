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
        buf.write("\3\u608b\ua72a\u8133\ub9ed\u417c\u3be7\u7786\u5964\2-")
        buf.write("\u010a\b\1\4\2\t\2\4\3\t\3\4\4\t\4\4\5\t\5\4\6\t\6\4\7")
        buf.write("\t\7\4\b\t\b\4\t\t\t\4\n\t\n\4\13\t\13\4\f\t\f\4\r\t\r")
        buf.write("\4\16\t\16\4\17\t\17\4\20\t\20\4\21\t\21\4\22\t\22\4\23")
        buf.write("\t\23\4\24\t\24\4\25\t\25\4\26\t\26\4\27\t\27\4\30\t\30")
        buf.write("\4\31\t\31\4\32\t\32\4\33\t\33\4\34\t\34\4\35\t\35\4\36")
        buf.write("\t\36\4\37\t\37\4 \t \4!\t!\4\"\t\"\4#\t#\4$\t$\4%\t%")
        buf.write("\4&\t&\4\'\t\'\4(\t(\4)\t)\4*\t*\4+\t+\4,\t,\3\2\3\2\3")
        buf.write("\3\3\3\3\4\3\4\3\4\3\5\3\5\3\6\3\6\3\7\3\7\3\b\3\b\3\b")
        buf.write("\3\t\3\t\3\n\3\n\3\13\3\13\3\13\3\13\3\f\3\f\3\f\3\f\3")
        buf.write("\f\3\r\3\r\3\r\3\r\3\r\3\r\3\16\3\16\3\16\3\16\3\16\3")
        buf.write("\17\3\17\3\20\3\20\7\20\u0086\n\20\f\20\16\20\u0089\13")
        buf.write("\20\3\21\3\21\3\22\3\22\3\23\3\23\3\24\3\24\3\25\3\25")
        buf.write("\3\25\3\25\3\25\3\25\3\26\3\26\3\26\3\26\3\26\3\26\3\26")
        buf.write("\3\27\3\27\3\27\3\27\3\27\3\27\3\30\5\30\u00a7\n\30\3")
        buf.write("\30\3\30\3\31\6\31\u00ac\n\31\r\31\16\31\u00ad\3\32\3")
        buf.write("\32\3\32\3\32\3\33\5\33\u00b5\n\33\3\33\3\33\3\34\3\34")
        buf.write("\7\34\u00bb\n\34\f\34\16\34\u00be\13\34\3\34\3\34\3\35")
        buf.write("\3\35\3\35\3\35\3\36\3\36\3\36\3\36\3\36\3\36\3\37\3\37")
        buf.write("\3\37\3\37\3\37\3\37\3\37\3 \3 \3 \3 \3 \3 \3!\3!\3!\3")
        buf.write("!\3!\3!\3!\3\"\3\"\3\"\3\"\3#\3#\3#\3#\3#\3$\3$\3$\3%")
        buf.write("\3%\3%\3&\3&\3\'\3\'\3(\3(\3(\3)\3)\3)\3*\3*\3+\6+\u00fc")
        buf.write("\n+\r+\16+\u00fd\3+\3+\3,\3,\7,\u0104\n,\f,\16,\u0107")
        buf.write("\13,\3,\3,\2\2-\3\3\5\4\7\5\t\6\13\7\r\b\17\t\21\n\23")
        buf.write("\13\25\f\27\r\31\16\33\17\35\20\37\21!\22#\23%\24\'\25")
        buf.write(")\26+\27-\30/\31\61\32\63\33\65\34\67\359\36;\37= ?!A")
        buf.write("\"C#E$G%I&K\'M(O)Q*S+U,W-\3\2\b\4\2C\\c|\6\2\62;C\\aa")
        buf.write("c|\3\2\62;\4\2$$^^\4\2\13\13\"\"\4\2\f\f\17\17\2\u0110")
        buf.write("\2\3\3\2\2\2\2\5\3\2\2\2\2\7\3\2\2\2\2\t\3\2\2\2\2\13")
        buf.write("\3\2\2\2\2\r\3\2\2\2\2\17\3\2\2\2\2\21\3\2\2\2\2\23\3")
        buf.write("\2\2\2\2\25\3\2\2\2\2\27\3\2\2\2\2\31\3\2\2\2\2\33\3\2")
        buf.write("\2\2\2\35\3\2\2\2\2\37\3\2\2\2\2!\3\2\2\2\2#\3\2\2\2\2")
        buf.write("%\3\2\2\2\2\'\3\2\2\2\2)\3\2\2\2\2+\3\2\2\2\2-\3\2\2\2")
        buf.write("\2/\3\2\2\2\2\61\3\2\2\2\2\63\3\2\2\2\2\65\3\2\2\2\2\67")
        buf.write("\3\2\2\2\29\3\2\2\2\2;\3\2\2\2\2=\3\2\2\2\2?\3\2\2\2\2")
        buf.write("A\3\2\2\2\2C\3\2\2\2\2E\3\2\2\2\2G\3\2\2\2\2I\3\2\2\2")
        buf.write("\2K\3\2\2\2\2M\3\2\2\2\2O\3\2\2\2\2Q\3\2\2\2\2S\3\2\2")
        buf.write("\2\2U\3\2\2\2\2W\3\2\2\2\3Y\3\2\2\2\5[\3\2\2\2\7]\3\2")
        buf.write("\2\2\t`\3\2\2\2\13b\3\2\2\2\rd\3\2\2\2\17f\3\2\2\2\21")
        buf.write("i\3\2\2\2\23k\3\2\2\2\25m\3\2\2\2\27q\3\2\2\2\31v\3\2")
        buf.write("\2\2\33|\3\2\2\2\35\u0081\3\2\2\2\37\u0083\3\2\2\2!\u008a")
        buf.write("\3\2\2\2#\u008c\3\2\2\2%\u008e\3\2\2\2\'\u0090\3\2\2\2")
        buf.write(")\u0092\3\2\2\2+\u0098\3\2\2\2-\u009f\3\2\2\2/\u00a6\3")
        buf.write("\2\2\2\61\u00ab\3\2\2\2\63\u00af\3\2\2\2\65\u00b4\3\2")
        buf.write("\2\2\67\u00b8\3\2\2\29\u00c1\3\2\2\2;\u00c5\3\2\2\2=\u00cb")
        buf.write("\3\2\2\2?\u00d2\3\2\2\2A\u00d8\3\2\2\2C\u00df\3\2\2\2")
        buf.write("E\u00e3\3\2\2\2G\u00e8\3\2\2\2I\u00eb\3\2\2\2K\u00ee\3")
        buf.write("\2\2\2M\u00f0\3\2\2\2O\u00f2\3\2\2\2Q\u00f5\3\2\2\2S\u00f8")
        buf.write("\3\2\2\2U\u00fb\3\2\2\2W\u0101\3\2\2\2YZ\7]\2\2Z\4\3\2")
        buf.write("\2\2[\\\7_\2\2\\\6\3\2\2\2]^\7h\2\2^_\7p\2\2_\b\3\2\2")
        buf.write("\2`a\7*\2\2a\n\3\2\2\2bc\7.\2\2c\f\3\2\2\2de\7+\2\2e\16")
        buf.write("\3\2\2\2fg\7/\2\2gh\7@\2\2h\20\3\2\2\2ij\7}\2\2j\22\3")
        buf.write("\2\2\2kl\7\177\2\2l\24\3\2\2\2mn\7k\2\2no\7p\2\2op\7v")
        buf.write("\2\2p\26\3\2\2\2qr\7t\2\2rs\7g\2\2st\7c\2\2tu\7n\2\2u")
        buf.write("\30\3\2\2\2vw\7r\2\2wx\7t\2\2xy\7k\2\2yz\7p\2\2z{\7v\2")
        buf.write("\2{\32\3\2\2\2|}\7t\2\2}~\7g\2\2~\177\7c\2\2\177\u0080")
        buf.write("\7f\2\2\u0080\34\3\2\2\2\u0081\u0082\7?\2\2\u0082\36\3")
        buf.write("\2\2\2\u0083\u0087\t\2\2\2\u0084\u0086\t\3\2\2\u0085\u0084")
        buf.write("\3\2\2\2\u0086\u0089\3\2\2\2\u0087\u0085\3\2\2\2\u0087")
        buf.write("\u0088\3\2\2\2\u0088 \3\2\2\2\u0089\u0087\3\2\2\2\u008a")
        buf.write("\u008b\7-\2\2\u008b\"\3\2\2\2\u008c\u008d\7,\2\2\u008d")
        buf.write("$\3\2\2\2\u008e\u008f\7/\2\2\u008f&\3\2\2\2\u0090\u0091")
        buf.write("\7\61\2\2\u0091(\3\2\2\2\u0092\u0093\7*\2\2\u0093\u0094")
        buf.write("\7k\2\2\u0094\u0095\7p\2\2\u0095\u0096\7v\2\2\u0096\u0097")
        buf.write("\7+\2\2\u0097*\3\2\2\2\u0098\u0099\7*\2\2\u0099\u009a")
        buf.write("\7t\2\2\u009a\u009b\7g\2\2\u009b\u009c\7c\2\2\u009c\u009d")
        buf.write("\7n\2\2\u009d\u009e\7+\2\2\u009e,\3\2\2\2\u009f\u00a0")
        buf.write("\7*\2\2\u00a0\u00a1\7u\2\2\u00a1\u00a2\7v\2\2\u00a2\u00a3")
        buf.write("\7t\2\2\u00a3\u00a4\7+\2\2\u00a4.\3\2\2\2\u00a5\u00a7")
        buf.write("\7/\2\2\u00a6\u00a5\3\2\2\2\u00a6\u00a7\3\2\2\2\u00a7")
        buf.write("\u00a8\3\2\2\2\u00a8\u00a9\5\61\31\2\u00a9\60\3\2\2\2")
        buf.write("\u00aa\u00ac\t\4\2\2\u00ab\u00aa\3\2\2\2\u00ac\u00ad\3")
        buf.write("\2\2\2\u00ad\u00ab\3\2\2\2\u00ad\u00ae\3\2\2\2\u00ae\62")
        buf.write("\3\2\2\2\u00af\u00b0\5/\30\2\u00b0\u00b1\7\60\2\2\u00b1")
        buf.write("\u00b2\5\61\31\2\u00b2\64\3\2\2\2\u00b3\u00b5\7\17\2\2")
        buf.write("\u00b4\u00b3\3\2\2\2\u00b4\u00b5\3\2\2\2\u00b5\u00b6\3")
        buf.write("\2\2\2\u00b6\u00b7\7\f\2\2\u00b7\66\3\2\2\2\u00b8\u00bc")
        buf.write("\7$\2\2\u00b9\u00bb\n\5\2\2\u00ba\u00b9\3\2\2\2\u00bb")
        buf.write("\u00be\3\2\2\2\u00bc\u00ba\3\2\2\2\u00bc\u00bd\3\2\2\2")
        buf.write("\u00bd\u00bf\3\2\2\2\u00be\u00bc\3\2\2\2\u00bf\u00c0\7")
        buf.write("$\2\2\u00c08\3\2\2\2\u00c1\u00c2\7k\2\2\u00c2\u00c3\7")
        buf.write("h\2\2\u00c3\u00c4\7\"\2\2\u00c4:\3\2\2\2\u00c5\u00c6\7")
        buf.write("g\2\2\u00c6\u00c7\7n\2\2\u00c7\u00c8\7u\2\2\u00c8\u00c9")
        buf.write("\7g\2\2\u00c9\u00ca\7\"\2\2\u00ca<\3\2\2\2\u00cb\u00cc")
        buf.write("\7y\2\2\u00cc\u00cd\7j\2\2\u00cd\u00ce\7k\2\2\u00ce\u00cf")
        buf.write("\7n\2\2\u00cf\u00d0\7g\2\2\u00d0\u00d1\7\"\2\2\u00d1>")
        buf.write("\3\2\2\2\u00d2\u00d3\7v\2\2\u00d3\u00d4\7t\2\2\u00d4\u00d5")
        buf.write("\7w\2\2\u00d5\u00d6\7g\2\2\u00d6\u00d7\7\"\2\2\u00d7@")
        buf.write("\3\2\2\2\u00d8\u00d9\7h\2\2\u00d9\u00da\7c\2\2\u00da\u00db")
        buf.write("\7n\2\2\u00db\u00dc\7u\2\2\u00dc\u00dd\7g\2\2\u00dd\u00de")
        buf.write("\7\"\2\2\u00deB\3\2\2\2\u00df\u00e0\7q\2\2\u00e0\u00e1")
        buf.write("\7t\2\2\u00e1\u00e2\7\"\2\2\u00e2D\3\2\2\2\u00e3\u00e4")
        buf.write("\7c\2\2\u00e4\u00e5\7p\2\2\u00e5\u00e6\7f\2\2\u00e6\u00e7")
        buf.write("\7\"\2\2\u00e7F\3\2\2\2\u00e8\u00e9\7?\2\2\u00e9\u00ea")
        buf.write("\7?\2\2\u00eaH\3\2\2\2\u00eb\u00ec\7#\2\2\u00ec\u00ed")
        buf.write("\7?\2\2\u00edJ\3\2\2\2\u00ee\u00ef\7@\2\2\u00efL\3\2\2")
        buf.write("\2\u00f0\u00f1\7>\2\2\u00f1N\3\2\2\2\u00f2\u00f3\7@\2")
        buf.write("\2\u00f3\u00f4\7?\2\2\u00f4P\3\2\2\2\u00f5\u00f6\7>\2")
        buf.write("\2\u00f6\u00f7\7?\2\2\u00f7R\3\2\2\2\u00f8\u00f9\7#\2")
        buf.write("\2\u00f9T\3\2\2\2\u00fa\u00fc\t\6\2\2\u00fb\u00fa\3\2")
        buf.write("\2\2\u00fc\u00fd\3\2\2\2\u00fd\u00fb\3\2\2\2\u00fd\u00fe")
        buf.write("\3\2\2\2\u00fe\u00ff\3\2\2\2\u00ff\u0100\b+\2\2\u0100")
        buf.write("V\3\2\2\2\u0101\u0105\7%\2\2\u0102\u0104\n\7\2\2\u0103")
        buf.write("\u0102\3\2\2\2\u0104\u0107\3\2\2\2\u0105\u0103\3\2\2\2")
        buf.write("\u0105\u0106\3\2\2\2\u0106\u0108\3\2\2\2\u0107\u0105\3")
        buf.write("\2\2\2\u0108\u0109\b,\2\2\u0109X\3\2\2\2\n\2\u0087\u00a6")
        buf.write("\u00ad\u00b4\u00bc\u00fd\u0105\3\b\2\2")
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
    STD_OUT = 12
    STD_IN = 13
    ASSIGN = 14
    ID = 15
    ADD = 16
    MUL = 17
    SUB = 18
    DIV = 19
    TOINT = 20
    TOREAL = 21
    TOSTR = 22
    INT = 23
    UINT = 24
    REAL = 25
    NEWLINE = 26
    STRING = 27
    IF = 28
    ELSE = 29
    WHILE = 30
    TRUE = 31
    FALSE = 32
    OR = 33
    AND = 34
    EQ = 35
    NEQ = 36
    GT = 37
    LT = 38
    GTEQ = 39
    LTEQ = 40
    NOT = 41
    WS = 42
    LINE_COMMENT = 43

    channelNames = [ u"DEFAULT_TOKEN_CHANNEL", u"HIDDEN" ]

    modeNames = [ "DEFAULT_MODE" ]

    literalNames = [ "<INVALID>",
            "'['", "']'", "'fn'", "'('", "','", "')'", "'->'", "'{'", "'}'", 
            "'int'", "'real'", "'print'", "'read'", "'='", "'+'", "'*'", 
            "'-'", "'/'", "'(int)'", "'(real)'", "'(str)'", "'if '", "'else '", 
            "'while '", "'true '", "'false '", "'or '", "'and '", "'=='", 
            "'!='", "'>'", "'<'", "'>='", "'<='", "'!'" ]

    symbolicNames = [ "<INVALID>",
            "STD_OUT", "STD_IN", "ASSIGN", "ID", "ADD", "MUL", "SUB", "DIV", 
            "TOINT", "TOREAL", "TOSTR", "INT", "UINT", "REAL", "NEWLINE", 
            "STRING", "IF", "ELSE", "WHILE", "TRUE", "FALSE", "OR", "AND", 
            "EQ", "NEQ", "GT", "LT", "GTEQ", "LTEQ", "NOT", "WS", "LINE_COMMENT" ]

    ruleNames = [ "T__0", "T__1", "T__2", "T__3", "T__4", "T__5", "T__6", 
                  "T__7", "T__8", "T__9", "T__10", "STD_OUT", "STD_IN", 
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


