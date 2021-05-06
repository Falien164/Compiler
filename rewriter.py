# Generated from Hello.g4 by ANTLR 4.9.2
from antlr4 import *
from antlr_lib.HelloParser import HelloParser
from antlr_lib.HelloListener import HelloListener
from generate import LLVMGenerator
from util import eprint

# This class defines a complete listener for a parse tree produced by HelloParser.
import sys
import queue

# Przerobic assign by LOAD i wczytywac ze zmiennej

### dodaj przypisywanie stringa do zmiennej
### popraw operacje matematyczne na zmiennych  (load)
### operacje z nawiasami
### obsluga nieistniejacych zmiennych
### poprawić obsługę błędów w arytmetyce
class RewriteHelloListener(HelloListener):
    def __init__(self):
        self.stack = queue.LifoQueue()  # (value, type)
        self.variables = {}  # dict    [variable, type]
        self.llvmGenerator = LLVMGenerator()
        self.line = 0

    def error(self, msg):
        eprint("Error in line " + str(self.line) + ": " + msg)
        sys.exit(0)

    # Exit a parse tree produced by HelloParser#start.
    def exitStart(self, ctx: HelloParser.StartContext):
        print(LLVMGenerator.generate(self.llvmGenerator))
        eprint(self.variables)
        eprint("Na stosie zostalo:")
        for i in range(0, self.stack.qsize()):
            eprint(self.stack.get())

    # Exit a parse tree produced by HelloParser#block.
    def exitBlock(self, ctx: HelloParser.BlockContext):
        self.line += 1

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
            elif species == "STR":
                LLVMGenerator.printf_str(self.llvmGenerator, ID)

        elif not self.stack.empty():
            v = self.stack.get_nowait()
            eprint(v)
            if v[1] == "INT":
                LLVMGenerator.printf_undefined_i32(self.llvmGenerator, v[0])
            if v[1] == "REAL":
                LLVMGenerator.printf_undefined_real(self.llvmGenerator, v[0])
            elif v[-1] == "STR":
                value = v[0]
                value = value[:-1]
                value = value[1:]
                LLVMGenerator.printf_undefined_str(self.llvmGenerator, value)
        else:
            eprint(ctx.getRuleIndex())
            self.error("unknown variable " + ID)

    # Exit a parse tree produced by HelloParser#assign.
    def exitAssign(self, ctx: HelloParser.AssignContext):
        ID = ctx.ID().getText()
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + ID)
        if ID not in self.variables:  # for int and real not for string
            if v[1] == "INT":
                LLVMGenerator.declare_i32(self.llvmGenerator, ID)
            if v[1] == "REAL":
                LLVMGenerator.declare_real(self.llvmGenerator, ID)
        self.variables[ID] = v[1]
        if v[1] == "INT":
            LLVMGenerator.assign_i32(self.llvmGenerator, ID, v[0])
        if v[1] == "REAL":
            LLVMGenerator.assign_real(self.llvmGenerator, ID, v[0])
        # if(v[1]=="STR"):
        #     value = v[0][:-1]
        #     LLVMGenerator.assign_str(self.llvmGenerator,ID, value)

    # Exit a parse tree produced by HelloParser#additiveExpr.
    def exitAdditiveExpr(self, ctx: HelloParser.AdditiveExprContext):
        if not self.stack.empty():
            v1 = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + ctx.expr1().getText())
        if not self.stack.empty():
            v2 = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + ctx.expr1().getText())

        if str(ctx.ADD()) == "+":
            if v1[1] == (v2[1]):
                if v1[1] == "INT":
                    LLVMGenerator.add_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[1] == "REAL":
                    LLVMGenerator.add_real(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
                if v1[-1] == "STR":
                    concrete_string = '"' + (v2[0] + v1[0]).replace('"', "") + '"'
                    name = "@.str" + (str(self.llvmGenerator.reg - 1))
                    # LLVMGenerator.load_str(self.llvmGenerator, name, concrete_string[:-1])
                    self.stack.put((concrete_string, name, "STR"))
        elif str(ctx.SUB()) == "-":
            if v1[1] == "INT":
                LLVMGenerator.sub_i32(self.llvmGenerator, v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
            if v1[1] == "REAL":
                LLVMGenerator.sub_real(self.llvmGenerator, v1[0], v2[0])
                self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        else:
            self.error(ctx.getStart().getLine(), "add type mismatch")

    # Exit a parse tree produced by HelloParser#multiplicationExpr.
    def exitMultiplicationExpr(self, ctx: HelloParser.MultiplicationExprContext):
        if not self.stack.empty():
            v1 = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + "multiplicationExpr 1")
        if not self.stack.empty():
            v2 = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + "multiplicationExpr 2")

        if str(ctx.MUL()) == "*":
            if v1[1] == (v2[1]):
                if v1[1] == "INT":
                    LLVMGenerator.mul_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[1] == "REAL":
                    LLVMGenerator.mul_real(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        elif str(ctx.DIV()) == "/":
            if v1[1] == (v2[1]):
                if v1[1] == "INT":
                    LLVMGenerator.div_i32(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))
                if v1[1] == "REAL":
                    LLVMGenerator.div_real(self.llvmGenerator, v1[0], v2[0])
                    self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))
        else:
            self.error(str(self.line) + " type mismatch")

    # Exit a parse tree produced by HelloParser#int.
    def exitInt(self, ctx: HelloParser.IntContext):
        self.stack.put((ctx.INT().getText(), "INT"))

    # Exit a parse tree produced by HelloParser#real.
    def exitReal(self, ctx: HelloParser.RealContext):
        self.stack.put((ctx.REAL().getText(), "REAL"))

    # Exit a parse tree produced by HelloParser#toint.
    def exitToint(self, ctx: HelloParser.TointContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + ID)
        LLVMGenerator.fptosi(self.llvmGenerator, v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "INT"))

    # Exit a parse tree produced by HelloParser#toreal.
    def exitToreal(self, ctx: HelloParser.TorealContext):
        if not self.stack.empty():
            v = self.stack.get_nowait()
        else:
            self.error("EMPTY STACK with ID = " + ID)
        LLVMGenerator.sitofp(self.llvmGenerator, v[0])
        self.stack.put(("%" + str(self.llvmGenerator.reg - 1), "REAL"))

    # Exit a parse tree produced by HelloParser#string.
    def exitString(self, ctx: HelloParser.StringContext):
        # ID = ctx.STRING().getText()
        # self.variables[ID] = "STR"
        self.stack.put((ctx.STRING().getText(), "STR"))

    # Exit a parse tree produced by HelloParser#id.
    def exitId(self, ctx: HelloParser.IdContext):
        ID = ctx.ID().getText()
        species = self.variables.get(ID)  # "ID"
        eprint(species)
        eprint(ID)
        if species == "INT":
            LLVMGenerator.load_i32(self.llvmGenerator, (ID))
        if species == "REAL":
            LLVMGenerator.load_real(self.llvmGenerator, (ID))
        self.stack.put(("%" + (str(self.llvmGenerator.reg - 1)), species))

    # # Exit a parse tree produced by HelloParser#scanf.
    def exitScanf(self, ctx: HelloParser.ScanfContext):
        ID = ctx.ID().getText()
        if ID not in self.variables:
            self.error(f"VARIABLE : {ID} not declared but used")
        else:
            variable = self.variables[ID]
            typeName = variable
            variableId = ID
            eprint(ID)
            eprint(variableId)
            if typeName == "INT":
                LLVMGenerator.scanf_i32(self.llvmGenerator, variableId)
            elif typeName == "REAL":
                LLVMGenerator.scanf_double(self.llvmGenerator, variableId)
            else:
                self.error(f"variable {variable}")
                raise NotImplementedError

    def exitArray(self, ctx: HelloParser.ArrayContext):
        # pop one element
        # check it's type
        # save it as type
        # allocate qsize elements of type
        #
        for i in range(0, self.stack.qsize()):
            eprint(self.stack.get())


del HelloParser
