from antlr4 import *
from antlr_lib.HelloParser import HelloParser
from antlr_lib.HelloListener import HelloListener
from generate import LLVMGenerator
from util import eprint
from typing import Tuple, Dict

# This class defines a complete listener for a parse tree produced by HelloParser.
import sys
import queue

# Przerobic assign by LOAD i wczytywac ze zmiennej

# castowanie reala i inta na stringa
# assing string do zmiennych
class RewriteHelloListener(HelloListener):
    def __init__(self):
        self.stack = queue.LifoQueue()  # (value, type)
        self.labels = queue.LifoQueue()  # if context
        self.variables = {}  # dict    [variable, type]
        self.llvmGenerator = LLVMGenerator()
        self.line = 1
        self.end_if_label= []         # if context

    def error(self, msg):
        eprint("Error: " + msg)
        sys.exit(0)

    # Exit a parse tree produced by HelloParser#start.
    def exitStart(self, ctx: HelloParser.StartContext):
        print(self.llvmGenerator.generate())
        eprint(self.variables)
        eprint("Na stosie zostalo:")
        for i in range(0, self.stack.qsize()):
            eprint(self.stack.get())        
            
        eprint("Na stosie generatora zostalo:")
        for i in range(0, self.labels.qsize()):
            eprint(self.labels.get())


    
    def getTwoValueFromStack(self, ctx):
        if not self.stack.empty():
            v1 = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK with ID =  {ctx.expr()} at line:{l}, column:{c}")
        if not self.stack.empty():
            v2 = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK with ID =  {ctx.expr()} at line:{l}, column:{c}")
        return v1, v2


    def getOneValueFromStack(self, ctx):
        if not self.stack.empty():
            v1 = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK at line:{l}, column:{c}")
        return v1


    # Exit a parse tree produced by HelloParser#stat.
    def exitStat(self, ctx: HelloParser.StatContext):
        self.line += 1

    # Exit a parse tree produced by HelloParser#block.
    def exitBlock(self, ctx: HelloParser.BlockContext):
        pass

    # Exit a parse tree produced by HelloParser#printf.
    def exitPrintf(self, ctx: HelloParser.PrintfContext):
        ID = ctx.value().getText()
        species = self.variables.get(ID)
        if species != None:
            v = self.stack.get_nowait()
            if species == "INT":
                self.llvmGenerator.printf_i32(ID)
            elif species == "REAL":
                self.llvmGenerator.printf_real(ID)
            elif species[-1] == "STR":
                self.llvmGenerator.printf_str()

        elif not self.stack.empty():
            v = self.stack.get_nowait()
            if v[-1] == "INT":
                self.llvmGenerator.printf_undefined_i32(v[0])
            if v[-1] == "REAL":
                self.llvmGenerator.printf_undefined_real(v[0])
            elif v[-1] == "STR":
                value = v[0]
                value = value[:-1]
                value = value[1:]
                value = "%s" + value
                self.llvmGenerator.printf_undefined_str(value)
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"unknown variable {ID} at line:{l}, column:{c}")

    # Exit a parse tree produced by HelloParser#assign.
    def exitAssign(self, ctx: HelloParser.AssignContext):
        ID = ctx.ID().getText()
        if not self.stack.empty():
            v = self.stack.get_nowait()
            if ID not in self.variables:  # for int and real not for string
                if v[1] == "INT":
                    self.llvmGenerator.declare_i32(ID)
                    self.llvmGenerator.assign_i32(ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "REAL":
                    self.llvmGenerator.declare_real(ID)
                    self.llvmGenerator.assign_real(ID, v[0])
                    self.variables[ID] = v[1]
                elif v[-1] == "STR":
                    self.llvmGenerator.declare_str(ID, v[0])
                    self.variables[ID] = (v[-2], v[-1])  # insert type and value
                    value = v[0][:-1]
                    self.llvmGenerator.assign_str(ID, value)
                elif v[1] == "ARRAY":
                    size = self.stack.qsize()
                    last = self.stack.get_nowait()
                    ty = last[1]
                    if ty == "INT":
                        # assign bo źle nazwałem metodę
                        self.llvmGenerator.assign_array_i32(ID, size)
                        self.llvmGenerator.store_array_i32(ID, size - 1, last[0], size)
                    elif ty == "REAL":
                        self.llvmGenerator.assign_array_double(ID, size)
                        self.llvmGenerator.store_array_double(
                            ID, size - 1, last[0], size
                        )
                    else:
                        raise NotImplemented
                    # reverse queue
                    for i in range(size - 2, -1, -1):
                        t = self.stack.get_nowait()
                        if t[1] != ty:
                            l = ctx.start.line
                            c = ctx.start.column
                            self.error(
                                "Array types are inconsistent at line:{l}, column:{c}"
                            )
                        if ty == "INT":
                            # assign bo źle nazwałem metodę
                            self.llvmGenerator.store_array_i32(ID, i, t[0], size)
                        elif ty == "REAL":
                            self.llvmGenerator.store_array_double(ID, i, t[0], size)
                        else:
                            raise NotImplemented

                    self.variables[ID] = (v[1], size, ty)

                else:
                    raise NotImplemented
            else:
                # it re assignment
                if v[1] == "INT":
                    self.llvmGenerator.assign_i32(ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "REAL":
                    self.llvmGenerator.assign_real(ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "ARRAY":
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(f"Re definition of array {ID} at line:{l}, column:{c}")
                elif v[-1] == "STR":
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(f"Re definition of array {ID} at line:{l}, column:{c}")

        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK with ID = {ID} at line:{l}, column:{c}")

    # Exit a parse tree produced by HelloParser#additiveExpr.
    def exitAdditiveExpr(self, ctx: HelloParser.AdditiveExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)

        if str(ctx.ADD()) == "+":
            if v1[-1] == (v2[-1]):
                if v1[-1] == "INT":
                    self.llvmGenerator.add_i32(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    self.llvmGenerator.add_real(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
            elif v1[1][-1] == (v2[1][-1]):
                if v1[1][-1] == "STR":
                    self.llvmGenerator.add_str(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "STR"))
        elif str(ctx.SUB()) == "-":
            if v1[-1] == "INT":
                self.llvmGenerator.sub_i32(v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
            if v1[-1] == "REAL":
                self.llvmGenerator.sub_real(v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"type mismatch ID  =  {ctx.expr()} at line:{l}, column:{c}")

    def exitMultiplicationExpr(self, ctx: HelloParser.MultiplicationExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)

        if str(ctx.MUL()) == "*":
            if v1[-1] == (v2[-1]):
                if v1[-1] == "INT":
                    self.llvmGenerator.mul_i32(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    self.llvmGenerator.mul_real(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        elif str(ctx.DIV()) == "/":
            if v1[-1] == (v2[1]):
                if v1[-1] == "INT":
                    self.llvmGenerator.div_i32(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    self.llvmGenerator.div_real(v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"type mismatch ID  =  {ctx.expr()} at line:{l}, column:{c}")

    def exitInt(self, ctx: HelloParser.IntContext):
        self.stack.put((ctx.INT().getText(), "INT"))

    def exitReal(self, ctx: HelloParser.RealContext):
        self.stack.put((ctx.REAL().getText(), "REAL"))

    def exitString(self, ctx: HelloParser.StringContext):
        self.stack.put((ctx.STRING().getText(), "STR"))

    def exitToint(self, ctx: HelloParser.TointContext):
        if self.stack.empty():
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (int) command at line:{l}, column:{c}")
        
        v = self.stack.get_nowait()
        self.llvmGenerator.fptosi(v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))

    def exitToreal(self, ctx: HelloParser.TorealContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (real) command at line:{l}, column:{c}")
        self.llvmGenerator.sitofp(v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))

    def exitTostr(self, ctx: HelloParser.TostrContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (str) command at line:{l}, column:{c}")

        if ctx.atom().getText() in self.variables:
            self.llvmGenerator.itostr(ctx.atom().getText())
            print(v)
            self.stack.put((ctx.atom().getText(), "STR"))
        else:
            text = '"' + ctx.atom().getText() + '"'
            self.stack.put((text, "STR"))

    def exitId(self, ctx: HelloParser.IdContext):
        ID = ctx.ID().getText()
        species = self.variables.get(ID)  # "ID"
        if species == "INT":
            self.llvmGenerator.load_i32((ID))
            self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), species))
        elif species == "REAL":
            self.llvmGenerator.load_real((ID))
            self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), species))
        elif type(species) is tuple and species[-1] == "STR":
            self.llvmGenerator.load_str(ID, species[0])
            self.stack.put((ID, species))
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"Unexpected type at line:{l}, column:{c}")

    def exitId_dereference(self, ctx: HelloParser.Id_dereferenceContext):
        ID = ctx.ID().getText()
        variable = self.variables.get(ID)  # "ID"
        if variable:
            ty, size, elem_type = variable
            if not self.stack.empty():
                offSet, offSetType = self.stack.get_nowait()
                if ty != "ARRAY":
                    l = ctx.start.line
                    c = ctx.getChild(1).getPayload().column
                    self.error(
                        f"variable {ID} was defined as array at line:{l}, column:{c}"
                    )
                else:
                    if elem_type == "INT":
                        self.llvmGenerator.load_array_i32(ID, offSet, size)
                    elif elem_type == "REAL":
                        self.llvmGenerator.load_array_double(ID, offSet, size)
                self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), elem_type))
            else:
                l = ctx.start.line
                c = ctx.getChild(1).getPayload().column
                self.error(f"Missing array index at line:{l}, column:{c}")
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"Access to undeclared array line:{l}, column:{c}")

    def exitScanf(self, ctx: HelloParser.ScanfContext):
        ID = ctx.ID().getText()
        if ID not in self.variables:
            l = ctx.getChild(1).getPayload().line
            c = ctx.getChild(1).getPayload().column
            self.error(
                f"VARIABLE : {ID} was not declared but is used at line:{l}, column {c}"
            )
        else:
            variable = self.variables[ID]
            typeName = variable
            variableId = ID
            if typeName == "INT":
                self.llvmGenerator.scanf_i32(variableId)
            elif typeName == "REAL":
                self.llvmGenerator.scanf_double(variableId)
            else:
                l = ctx.start.line
                c = ctx.start.column
                self.error(f"cannot read variable: {variable} at line:{l}, column:{c}")
                raise NotImplementedError

    def exitArray(self, ctx: HelloParser.ArrayContext):
        self.stack.put(("", f"ARRAY"))

    def exitArray_assign(self, ctx: HelloParser.Array_assignContext):
        if not self.stack.empty():
            newValue, newType = self.stack.get_nowait()
            if not self.stack.empty():
                offSet, offSetType = self.stack.get_nowait()
                if offSetType != "INT":
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(
                        f"Only integer idexes are allowed at line:{l}, column:{c}"
                    )
                ID = ctx.ID().getText()
                elem = self.variables[ID]
                if type(elem) is tuple and elem[0] == "ARRAY":
                    _, size, elem_type = elem
                    if elem_type != newType:
                        l = ctx.start.line
                        c = ctx.start.column
                        self.error(
                            f"Variables types is different than collection element's type\nTrying to assign {newType} element to array of {elem_type} at line:{l}, column:{c}"
                        )
                    if elem_type == "INT":
                        self.llvmGenerator.store_array_i32(ID, offSet, newValue, size)
                    elif elem_type == "REAL":
                        self.llvmGenerator.store_array_i32(ID, offSet, newValue, size)
                    else:
                        raise NotImplemented
                else:
                    self.error("Type miss match trying to assign ")
            else:
                l = ctx.getChild(2).getPayload().start.line
                c = ctx.getChild(2).getPayload().start.column
                self.error(f"Index is missing is missig at line:{l}, column:{c}")
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"Value to be assigned is missig at line:{l}, column:{c}")
        ### if
    

    #### IF condition
    def enterIf_statement(self, ctx:HelloParser.If_statementContext):
        self.end_if_label.append(self.llvmGenerator.getLabel())

    def exitIf_statement(self, ctx:HelloParser.If_statementContext):
        self.llvmGenerator.goToLabel(self.end_if_label[-1])     # bez tego zagnieżdzone ify beda mialy 2 labele po sobie i to wywali błąd
        self.llvmGenerator.emitLabel(self.end_if_label[-1])
        self.end_if_label.pop(-1)

    def exitStat_block(self, ctx:HelloParser.Stat_blockContext):
        self.llvmGenerator.goToLabel(self.end_if_label[-1])
        
    def enterJump_block(self, ctx:HelloParser.Jump_blockContext):
        if(not self.labels.empty()):
            label = self.labels.get_nowait()
            if("or" in label):
                l_ifthen = label
                l_ifelse = self.llvmGenerator.getLabel()
            elif("and" in label):
                l_ifthen = self.llvmGenerator.getLabel()
                l_ifelse = label
            else:
                self.labels.put(label)
                l_ifelse = self.llvmGenerator.getLabel()
                l_ifthen = self.llvmGenerator.getLabel()
        else:
            l_ifelse = self.llvmGenerator.getLabel()
            l_ifthen = self.llvmGenerator.getLabel()

        condition = self.getOneValueFromStack(ctx)
        if(condition[-1] == "BOOLEAN"):
            self.llvmGenerator.conditional_branch(condition[0], l_ifthen, l_ifelse)
            self.llvmGenerator.emitLabel(l_ifthen)
            self.labels.put(l_ifelse)
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"expected boolean value at line:{l}, column:{c}")

    def exitCondition_block(self, ctx:HelloParser.Condition_blockContext):
        if self.labels.empty():
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"empty stack in generate at line:{l}, column:{c}")
        label = self.labels.get_nowait()
        self.llvmGenerator.emitLabel(label) 


    #### WHILE LOOP   
    def enterWhile_stat(self, ctx:HelloParser.While_statContext):
        pass
    def exitWhile_stat(self, ctx:HelloParser.While_statContext):
        pass
    def enterLoop_condition(self, ctx:HelloParser.Loop_conditionContext):
        enter_label = self.llvmGenerator.getLabel()
        self.llvmGenerator.goToLabel(enter_label)
        self.llvmGenerator.emitLabel(enter_label)
        self.labels.put(enter_label)

    # Exit a parse tree produced by HelloParser#loop_condition.
    def exitLoop_condition(self, ctx:HelloParser.Loop_conditionContext):
        v1 = self.getOneValueFromStack(ctx)

        while_body = self.llvmGenerator.getLabel()
        while_end = self.llvmGenerator.getLabel()
        if(v1[-1] == "BOOLEAN"):
            self.llvmGenerator.conditional_branch(v1[0], while_body, while_end)
            self.llvmGenerator.emitLabel(while_body)
            self.labels.put(while_end)
        

    # Exit a parse tree produced by HelloParser#repetitions.
    def exitRepetitions(self, ctx:HelloParser.RepetitionsContext):
        if (not self.labels.empty()):
            while_end = self.labels.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"empty stack of labels at line:{l}, column:{c}")
        if (not self.labels.empty()):
            while_cond= self.labels.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"empty stack of labels at line:{l}, column:{c}")
        self.llvmGenerator.goToLabel(while_cond)
        self.llvmGenerator.emitLabel(while_end)
        
        

    ### comparison

    def exitEqualityExpr(self, ctx:HelloParser.EqualityExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)
        if(v1[-1] != v2[-1]):
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"Types of expression are not the same at line:{l}, column:{c}")

        if str(ctx.EQ()) == "==":
            self.llvmGenerator.eq(v2[0], v1[0])
        elif str(ctx.NEQ()) == "!=":
            self.llvmGenerator.ne(v2[0], v1[0])
        self.stack.put((f"%{self.llvmGenerator.reg-1}", "BOOLEAN"))

    def exitRelationalExpr(self, ctx:HelloParser.RelationalExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)

        if(v1[-1] != v2[-1]):
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"Types of expression are not the same at line:{l}, column:{c}")

        if str(ctx.GT()) == ">":
            self.llvmGenerator.sgt(v2[0], v1[0])
        elif str(ctx.GTEQ()) == ">=":
            self.llvmGenerator.sge(v2[0], v1[0])
        elif str(ctx.LT()) == "<":
            self.llvmGenerator.slt(v2[0], v1[0])
        elif str(ctx.LTEQ()) == "<=":
            self.llvmGenerator.sle(v2[0], v1[0])
        self.stack.put((f"%{self.llvmGenerator.reg-1}", "BOOLEAN"))


    def exitAndExpr(self, ctx:HelloParser.AndExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)
        if_else = self.llvmGenerator.getLabel()
        if_else = "land_" + if_else
        if_true = self.llvmGenerator.getLabel()
        self.llvmGenerator.conditional_branch(v2[0],if_true, if_else)
        self.llvmGenerator.emitLabel(if_true)
        self.labels.put(if_else)
        self.stack.put(v1)
        
    def exitOrExpr(self, ctx:HelloParser.OrExprContext):
        v1, v2 = self.getTwoValueFromStack(ctx)
        if_true = self.llvmGenerator.getLabel()
        if_true = "lor_" + if_true
        if_false = self.llvmGenerator.getLabel()
        self.llvmGenerator.conditional_branch(v2[0], if_true, if_false)
        self.llvmGenerator.emitLabel(if_false)
        self.labels.put(if_true)
        self.stack.put(v1)


del HelloParser
