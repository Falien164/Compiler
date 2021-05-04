import sys
import FileStream
from antlr4 import *
from antlr_lib.HelloLexer import HelloLexer
from antlr_lib.HelloParser import HelloParser
from rewriter import RewriteHelloListener


def main(argv):
    input_stream = FileStream("tekst.py")
    lexer = HelloLexer(input_stream)
    stream = CommonTokenStream(lexer)
    parser = HelloParser(stream)
    tree = parser.start()

    print(tree.toStringTree(recog=parser))
    # print(";")

    listener = RewriteHelloListener()
    walker = ParseTreeWalker()
    walker.walk(listener, tree)

    # print(listener.getResult())


if __name__ == "__main__":
    main(sys.argv)
