# Generated from ./antlr_lib/Hello.g4 by ANTLR 4.9.2
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .HelloParser import HelloParser
else:
    from HelloParser import HelloParser

# This class defines a complete listener for a parse tree produced by HelloParser.
class HelloListener(ParseTreeListener):

    # Enter a parse tree produced by HelloParser#start.
    def enterStart(self, ctx:HelloParser.StartContext):
        pass

    # Exit a parse tree produced by HelloParser#start.
    def exitStart(self, ctx:HelloParser.StartContext):
        pass


    # Enter a parse tree produced by HelloParser#block.
    def enterBlock(self, ctx:HelloParser.BlockContext):
        pass

    # Exit a parse tree produced by HelloParser#block.
    def exitBlock(self, ctx:HelloParser.BlockContext):
        pass


    # Enter a parse tree produced by HelloParser#stat.
    def enterStat(self, ctx:HelloParser.StatContext):
        pass

    # Exit a parse tree produced by HelloParser#stat.
    def exitStat(self, ctx:HelloParser.StatContext):
        pass


    # Enter a parse tree produced by HelloParser#printf.
    def enterPrintf(self, ctx:HelloParser.PrintfContext):
        pass

    # Exit a parse tree produced by HelloParser#printf.
    def exitPrintf(self, ctx:HelloParser.PrintfContext):
        pass


    # Enter a parse tree produced by HelloParser#assign.
    def enterAssign(self, ctx:HelloParser.AssignContext):
        pass

    # Exit a parse tree produced by HelloParser#assign.
    def exitAssign(self, ctx:HelloParser.AssignContext):
        pass


    # Enter a parse tree produced by HelloParser#multiplicationExpr.
    def enterMultiplicationExpr(self, ctx:HelloParser.MultiplicationExprContext):
        pass

    # Exit a parse tree produced by HelloParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx:HelloParser.MultiplicationExprContext):
        pass


    # Enter a parse tree produced by HelloParser#atomExpr.
    def enterAtomExpr(self, ctx:HelloParser.AtomExprContext):
        pass

    # Exit a parse tree produced by HelloParser#atomExpr.
    def exitAtomExpr(self, ctx:HelloParser.AtomExprContext):
        pass


    # Enter a parse tree produced by HelloParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:HelloParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by HelloParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:HelloParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by HelloParser#int.
    def enterInt(self, ctx:HelloParser.IntContext):
        pass

    # Exit a parse tree produced by HelloParser#int.
    def exitInt(self, ctx:HelloParser.IntContext):
        pass


    # Enter a parse tree produced by HelloParser#real.
    def enterReal(self, ctx:HelloParser.RealContext):
        pass

    # Exit a parse tree produced by HelloParser#real.
    def exitReal(self, ctx:HelloParser.RealContext):
        pass


    # Enter a parse tree produced by HelloParser#toint.
    def enterToint(self, ctx:HelloParser.TointContext):
        pass

    # Exit a parse tree produced by HelloParser#toint.
    def exitToint(self, ctx:HelloParser.TointContext):
        pass


    # Enter a parse tree produced by HelloParser#toreal.
    def enterToreal(self, ctx:HelloParser.TorealContext):
        pass

    # Exit a parse tree produced by HelloParser#toreal.
    def exitToreal(self, ctx:HelloParser.TorealContext):
        pass


    # Enter a parse tree produced by HelloParser#par.
    def enterPar(self, ctx:HelloParser.ParContext):
        pass

    # Exit a parse tree produced by HelloParser#par.
    def exitPar(self, ctx:HelloParser.ParContext):
        pass


    # Enter a parse tree produced by HelloParser#id.
    def enterId(self, ctx:HelloParser.IdContext):
        pass

    # Exit a parse tree produced by HelloParser#id.
    def exitId(self, ctx:HelloParser.IdContext):
        pass


    # Enter a parse tree produced by HelloParser#string.
    def enterString(self, ctx:HelloParser.StringContext):
        pass

    # Exit a parse tree produced by HelloParser#string.
    def exitString(self, ctx:HelloParser.StringContext):
        pass


    # Enter a parse tree produced by HelloParser#value.
    def enterValue(self, ctx:HelloParser.ValueContext):
        pass

    # Exit a parse tree produced by HelloParser#value.
    def exitValue(self, ctx:HelloParser.ValueContext):
        pass



del HelloParser