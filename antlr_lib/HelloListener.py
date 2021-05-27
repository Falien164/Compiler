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


    # Enter a parse tree produced by HelloParser#top_level_stat.
    def enterTop_level_stat(self, ctx:HelloParser.Top_level_statContext):
        pass

    # Exit a parse tree produced by HelloParser#top_level_stat.
    def exitTop_level_stat(self, ctx:HelloParser.Top_level_statContext):
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


    # Enter a parse tree produced by HelloParser#scanf.
    def enterScanf(self, ctx:HelloParser.ScanfContext):
        pass

    # Exit a parse tree produced by HelloParser#scanf.
    def exitScanf(self, ctx:HelloParser.ScanfContext):
        pass


    # Enter a parse tree produced by HelloParser#array_assign.
    def enterArray_assign(self, ctx:HelloParser.Array_assignContext):
        pass

    # Exit a parse tree produced by HelloParser#array_assign.
    def exitArray_assign(self, ctx:HelloParser.Array_assignContext):
        pass


    # Enter a parse tree produced by HelloParser#assign_local.
    def enterAssign_local(self, ctx:HelloParser.Assign_localContext):
        pass

    # Exit a parse tree produced by HelloParser#assign_local.
    def exitAssign_local(self, ctx:HelloParser.Assign_localContext):
        pass


    # Enter a parse tree produced by HelloParser#assign_global.
    def enterAssign_global(self, ctx:HelloParser.Assign_globalContext):
        pass

    # Exit a parse tree produced by HelloParser#assign_global.
    def exitAssign_global(self, ctx:HelloParser.Assign_globalContext):
        pass


    # Enter a parse tree produced by HelloParser#global_assign.
    def enterGlobal_assign(self, ctx:HelloParser.Global_assignContext):
        pass

    # Exit a parse tree produced by HelloParser#global_assign.
    def exitGlobal_assign(self, ctx:HelloParser.Global_assignContext):
        pass


    # Enter a parse tree produced by HelloParser#function_definiotion.
    def enterFunction_definiotion(self, ctx:HelloParser.Function_definiotionContext):
        pass

    # Exit a parse tree produced by HelloParser#function_definiotion.
    def exitFunction_definiotion(self, ctx:HelloParser.Function_definiotionContext):
        pass


    # Enter a parse tree produced by HelloParser#function_call.
    def enterFunction_call(self, ctx:HelloParser.Function_callContext):
        pass

    # Exit a parse tree produced by HelloParser#function_call.
    def exitFunction_call(self, ctx:HelloParser.Function_callContext):
        pass


    # Enter a parse tree produced by HelloParser#function_body.
    def enterFunction_body(self, ctx:HelloParser.Function_bodyContext):
        pass

    # Exit a parse tree produced by HelloParser#function_body.
    def exitFunction_body(self, ctx:HelloParser.Function_bodyContext):
        pass


    # Enter a parse tree produced by HelloParser#return_stat.
    def enterReturn_stat(self, ctx:HelloParser.Return_statContext):
        pass

    # Exit a parse tree produced by HelloParser#return_stat.
    def exitReturn_stat(self, ctx:HelloParser.Return_statContext):
        pass


    # Enter a parse tree produced by HelloParser#return_type.
    def enterReturn_type(self, ctx:HelloParser.Return_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#return_type.
    def exitReturn_type(self, ctx:HelloParser.Return_typeContext):
        pass


    # Enter a parse tree produced by HelloParser#our_type.
    def enterOur_type(self, ctx:HelloParser.Our_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#our_type.
    def exitOur_type(self, ctx:HelloParser.Our_typeContext):
        pass


    # Enter a parse tree produced by HelloParser#builtin_type.
    def enterBuiltin_type(self, ctx:HelloParser.Builtin_typeContext):
        pass

    # Exit a parse tree produced by HelloParser#builtin_type.
    def exitBuiltin_type(self, ctx:HelloParser.Builtin_typeContext):
        pass


    # Enter a parse tree produced by HelloParser#function_name.
    def enterFunction_name(self, ctx:HelloParser.Function_nameContext):
        pass

    # Exit a parse tree produced by HelloParser#function_name.
    def exitFunction_name(self, ctx:HelloParser.Function_nameContext):
        pass


    # Enter a parse tree produced by HelloParser#if_statement.
    def enterIf_statement(self, ctx:HelloParser.If_statementContext):
        pass

    # Exit a parse tree produced by HelloParser#if_statement.
    def exitIf_statement(self, ctx:HelloParser.If_statementContext):
        pass


    # Enter a parse tree produced by HelloParser#condition_block.
    def enterCondition_block(self, ctx:HelloParser.Condition_blockContext):
        pass

    # Exit a parse tree produced by HelloParser#condition_block.
    def exitCondition_block(self, ctx:HelloParser.Condition_blockContext):
        pass


    # Enter a parse tree produced by HelloParser#jump_block.
    def enterJump_block(self, ctx:HelloParser.Jump_blockContext):
        pass

    # Exit a parse tree produced by HelloParser#jump_block.
    def exitJump_block(self, ctx:HelloParser.Jump_blockContext):
        pass


    # Enter a parse tree produced by HelloParser#stat_block.
    def enterStat_block(self, ctx:HelloParser.Stat_blockContext):
        pass

    # Exit a parse tree produced by HelloParser#stat_block.
    def exitStat_block(self, ctx:HelloParser.Stat_blockContext):
        pass


    # Enter a parse tree produced by HelloParser#while_stat.
    def enterWhile_stat(self, ctx:HelloParser.While_statContext):
        pass

    # Exit a parse tree produced by HelloParser#while_stat.
    def exitWhile_stat(self, ctx:HelloParser.While_statContext):
        pass


    # Enter a parse tree produced by HelloParser#loop_condition.
    def enterLoop_condition(self, ctx:HelloParser.Loop_conditionContext):
        pass

    # Exit a parse tree produced by HelloParser#loop_condition.
    def exitLoop_condition(self, ctx:HelloParser.Loop_conditionContext):
        pass


    # Enter a parse tree produced by HelloParser#repetitions.
    def enterRepetitions(self, ctx:HelloParser.RepetitionsContext):
        pass

    # Exit a parse tree produced by HelloParser#repetitions.
    def exitRepetitions(self, ctx:HelloParser.RepetitionsContext):
        pass


    # Enter a parse tree produced by HelloParser#functionCallExpr.
    def enterFunctionCallExpr(self, ctx:HelloParser.FunctionCallExprContext):
        pass

    # Exit a parse tree produced by HelloParser#functionCallExpr.
    def exitFunctionCallExpr(self, ctx:HelloParser.FunctionCallExprContext):
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


    # Enter a parse tree produced by HelloParser#orExpr.
    def enterOrExpr(self, ctx:HelloParser.OrExprContext):
        pass

    # Exit a parse tree produced by HelloParser#orExpr.
    def exitOrExpr(self, ctx:HelloParser.OrExprContext):
        pass


    # Enter a parse tree produced by HelloParser#additiveExpr.
    def enterAdditiveExpr(self, ctx:HelloParser.AdditiveExprContext):
        pass

    # Exit a parse tree produced by HelloParser#additiveExpr.
    def exitAdditiveExpr(self, ctx:HelloParser.AdditiveExprContext):
        pass


    # Enter a parse tree produced by HelloParser#relationalExpr.
    def enterRelationalExpr(self, ctx:HelloParser.RelationalExprContext):
        pass

    # Exit a parse tree produced by HelloParser#relationalExpr.
    def exitRelationalExpr(self, ctx:HelloParser.RelationalExprContext):
        pass


    # Enter a parse tree produced by HelloParser#equalityExpr.
    def enterEqualityExpr(self, ctx:HelloParser.EqualityExprContext):
        pass

    # Exit a parse tree produced by HelloParser#equalityExpr.
    def exitEqualityExpr(self, ctx:HelloParser.EqualityExprContext):
        pass


    # Enter a parse tree produced by HelloParser#andExpr.
    def enterAndExpr(self, ctx:HelloParser.AndExprContext):
        pass

    # Exit a parse tree produced by HelloParser#andExpr.
    def exitAndExpr(self, ctx:HelloParser.AndExprContext):
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


    # Enter a parse tree produced by HelloParser#tostr.
    def enterTostr(self, ctx:HelloParser.TostrContext):
        pass

    # Exit a parse tree produced by HelloParser#tostr.
    def exitTostr(self, ctx:HelloParser.TostrContext):
        pass


    # Enter a parse tree produced by HelloParser#booleanAtom.
    def enterBooleanAtom(self, ctx:HelloParser.BooleanAtomContext):
        pass

    # Exit a parse tree produced by HelloParser#booleanAtom.
    def exitBooleanAtom(self, ctx:HelloParser.BooleanAtomContext):
        pass


    # Enter a parse tree produced by HelloParser#id_dereference.
    def enterId_dereference(self, ctx:HelloParser.Id_dereferenceContext):
        pass

    # Exit a parse tree produced by HelloParser#id_dereference.
    def exitId_dereference(self, ctx:HelloParser.Id_dereferenceContext):
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


    # Enter a parse tree produced by HelloParser#idGlobalReference.
    def enterIdGlobalReference(self, ctx:HelloParser.IdGlobalReferenceContext):
        pass

    # Exit a parse tree produced by HelloParser#idGlobalReference.
    def exitIdGlobalReference(self, ctx:HelloParser.IdGlobalReferenceContext):
        pass


    # Enter a parse tree produced by HelloParser#array.
    def enterArray(self, ctx:HelloParser.ArrayContext):
        pass

    # Exit a parse tree produced by HelloParser#array.
    def exitArray(self, ctx:HelloParser.ArrayContext):
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