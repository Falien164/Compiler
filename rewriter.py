# Generated from Hello.g4 by ANTLR 4.9.2
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

#castowanie reala i inta na stringa
#assing string do zmiennych
class RewriteHelloListener(HelloListener):
    def __init__(self):
        self.stack = queue.LifoQueue()  # (value, type)
        self.variables = {}  # dict    [variable, type]
        self.llvmGenerator = LLVMGenerator()
        self.line = 1

    def error(self, msg):
        eprint("Error: " + msg)
        sys.exit(0)

    # Exit a parse tree produced by HelloParser#start.
    def exitStart(self, ctx: HelloParser.StartContext):
        print(LLVMGenerator.generate(self.llvmGenerator))
        eprint(self.variables)
        eprint("Na stosie zostalo:")
        for i in range(0, self.stack.qsize()):
            eprint(self.stack.get())


    # Exit a parse tree produced by HelloParser#stat.
    def exitStat(self, ctx:HelloParser.StatContext):
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
                LLVMGenerator.printf_i32(self.llvmGenerator, ID)
            elif species == "REAL":
                LLVMGenerator.printf_real(self.llvmGenerator, ID)
            elif species[-1] == "STR":
                LLVMGenerator.printf_str(self.llvmGenerator)

        elif not self.stack.empty():
            v = self.stack.get_nowait()
            if v[-1] == "INT":
                LLVMGenerator.printf_undefined_i32(self.llvmGenerator, v[0])
            if v[-1] == "REAL":
                LLVMGenerator.printf_undefined_real(self.llvmGenerator, v[0])
            elif v[-1] == "STR":
                value = v[0]
                value = value[:-1]
                value = value[1:]
                value = "%s" + value  
                LLVMGenerator.printf_undefined_str(self.llvmGenerator, value)
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
                    LLVMGenerator.declare_i32(self.llvmGenerator, ID)
                    LLVMGenerator.assign_i32(self.llvmGenerator, ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "REAL":
                    LLVMGenerator.declare_real(self.llvmGenerator, ID)
                    LLVMGenerator.assign_real(self.llvmGenerator, ID, v[0])
                    self.variables[ID] = v[1]
                elif v[-1] == "STR":
                    LLVMGenerator.declare_str(self.llvmGenerator, ID,v[0])
                    self.variables[ID] = (v[-2],v[-1])      #insert type and value
                    value = v[0][:-1]
                    LLVMGenerator.assign_str(self.llvmGenerator,ID, value)
                elif v[1] == "ARRAY":
                    size = self.stack.qsize()
                    last = self.stack.get_nowait()
                    ty = last[1]
                    if ty == "INT":
                        # assign bo źle nazwałem metodę
                        LLVMGenerator.assign_array_i32(self.llvmGenerator, ID, size)
                        LLVMGenerator.store_array_i32(
                            self.llvmGenerator, ID, size - 1, last[0], size
                        )
                    elif ty == "REAL":
                        LLVMGenerator.assign_array_double(self.llvmGenerator, ID, size)
                        LLVMGenerator.store_array_double(
                            self.llvmGenerator, ID, size - 1, last[0], size
                        )
                    else:
                        raise NotImplemented
                    # reverse queue
                    for i in range(size - 2, -1, -1):
                        t = self.stack.get_nowait()
                        if t[1] != ty:            
                            l = ctx.start.line
                            c = ctx.start.column
                            self.error("Array types are inconsistent at line:{l}, column:{c}") 
                        if ty == "INT":
                            # assign bo źle nazwałem metodę
                            LLVMGenerator.store_array_i32(
                                self.llvmGenerator, ID, i, t[0], size
                            )
                        elif ty == "REAL":
                            LLVMGenerator.store_array_double(
                                self.llvmGenerator, ID, i, t[0], size
                            )
                        else:
                            raise NotImplemented

                    self.variables[ID] = (v[1], size, ty)

                else:
                    raise NotImplemented
            else:
                # it re assignment
                if v[1] == "INT":
                    LLVMGenerator.assign_i32(self.llvmGenerator, ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "REAL":
                    LLVMGenerator.assign_real(self.llvmGenerator, ID, v[0])
                    self.variables[ID] = v[1]
                elif v[1] == "ARRAY":
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(f"Re definition of array {ID} at line:{l}, column:{c}")     
                elif(v[-1]=="STR"):
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(f"Re definition of array {ID} at line:{l}, column:{c}")

        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK with ID = {ID} at line:{l}, column:{c}")

    # Exit a parse tree produced by HelloParser#additiveExpr.
    def exitAdditiveExpr(self, ctx: HelloParser.AdditiveExprContext):
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
        if str(ctx.ADD()) == "+":
            if v1[-1] == (v2[-1]):
                if v1[-1] == "INT":
                    LLVMGenerator.add_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    LLVMGenerator.add_real(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
            elif v1[1][-1] == (v2[1][-1]):
                if v1[1][-1] == "STR":
                    LLVMGenerator.add_str(self.llvmGenerator,v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "STR"))
            else:
                l = ctx.start.line
                c = ctx.start.column
                self.error(f"type mismatch ID  =  {ctx.expr()} at line:{l}, column:{c}")

        elif str(ctx.SUB()) == "-":
            if v1[-1] == "INT":
                LLVMGenerator.sub_i32(self.llvmGenerator, v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
            if v1[-1] == "REAL":
                LLVMGenerator.sub_real(self.llvmGenerator, v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"type mismatch ID  =  {ctx.expr()} at line:{l}, column:{c}")

    def exitMultiplicationExpr(self, ctx: HelloParser.MultiplicationExprContext):
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

        if str(ctx.MUL()) == "*":
            if v1[-1] == (v2[-1]):
                if v1[-1] == "INT":
                    LLVMGenerator.mul_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    LLVMGenerator.mul_real(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        elif str(ctx.DIV()) == "/":
            if v1[-1] == (v2[1]):
                if v1[-1] == "INT":
                    LLVMGenerator.div_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[-1] == "REAL":
                    LLVMGenerator.div_real(self.llvmGenerator, v1[0], v2[0])
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
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (int) command at line:{l}, column:{c}")
        LLVMGenerator.fptosi(self.llvmGenerator, v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))

    def exitToreal(self, ctx: HelloParser.TorealContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (real) command at line:{l}, column:{c}")
        LLVMGenerator.sitofp(self.llvmGenerator, v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))

    def exitTostr(self, ctx:HelloParser.TostrContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            l = ctx.start.line
            c = ctx.start.column
            self.error(f"EMPTY STACK during (str) command at line:{l}, column:{c}")

        if(ctx.atom().getText() in self.variables):
            LLVMGenerator.itostr(self.llvmGenerator, ctx.atom().getText())
            print(v)
            self.stack.put((ctx.atom().getText(), "STR"))
        else:
            text = '"' +  ctx.atom().getText() + '"'
            self.stack.put((text, "STR"))

    def exitId(self, ctx: HelloParser.IdContext):
        ID = ctx.ID().getText()
        species = self.variables.get(ID)  # "ID"
        if species == "INT":
            LLVMGenerator.load_i32(self.llvmGenerator, (ID))
            self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), species))
        elif species == "REAL":
            LLVMGenerator.load_real(self.llvmGenerator, (ID))
            self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), species))
        elif (type(species) is tuple and species[-1] == "STR"):
            LLVMGenerator.load_str(self.llvmGenerator, ID, species[0])
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
                    self.error(f"variable {ID} was defined as array at line:{l}, column:{c}")
                if offSetType != "INT":
                    l = ctx.start.line
                    c = ctx.start.column
                    self.error(f"Only integer idexes are allowed at line:{l}, column:{c}")
                else:
                    if elem_type == "INT":
                        LLVMGenerator.load_array_i32(
                            self.llvmGenerator, ID, offSet, size
                        )
                    elif elem_type == "REAL":
                        LLVMGenerator.load_array_double(
                            self.llvmGenerator, ID, offSet, size
                        )
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
                LLVMGenerator.scanf_i32(self.llvmGenerator, variableId)
            elif typeName == "REAL":
                LLVMGenerator.scanf_double(self.llvmGenerator, variableId)
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
                    self.error(f"Only integer idexes are allowed at line:{l}, column:{c}")
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
                        self.llvmGenerator.store_array_i32(
                            self.llvmGenerator, ID, offSet, newValue, size
                        )
                    elif elem_type == "REAL":
                        self.llvmGenerator.store_array_i32(
                            self.llvmGenerator, ID, offSet, newValue, size
                        )
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

del HelloParser
