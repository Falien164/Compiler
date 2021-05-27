import enum
from functools import wraps
from enum import Enum
import queue
from collections.abc import Callable
from typing import Any


# maper type -> llvm type
class llvmType(Enum):
    i32 = "i32"
    double = "double"

    def __str__(self) -> str:
        return self.value


class LLVMGenerator:
    def __init__(self, mapper: Callable[[Any], llvmType]):
        self.header_text = ""
        self.main_text = ""
        self.reg: int = 1
        self.reg_stack: list[int] = []
        self.label: int = 0
        self.br = 0
        self.brstack = []
        self.mapper = mapper

    def __dec(foo):
        @wraps(foo)
        def inner(*args, **kwargs):
            val = foo(*args, **kwargs)
            args[0].reg += 1
            return val

        return inner

    def enterFunction(self):
        """Resets registry number, previous number is put on stack"""
        self.reg_stack.append(self.reg)
        # Because parameters are passed as pinters in registers 0+
        self.reg = 0

    def declare_function(self, fname: str, ret_type: Any, par_type_list: list[Any]):
        r_type = self.mapper(ret_type)
        self.main_text += f"define {r_type} @{fname}("
        for i in par_type_list[:1]:
            ty = self.mapper(i)
            self.main_text += f"{ty}"
        for i in par_type_list[1:]:
            ty = self.mapper(i)
            self.main_text += f",{ty}"
        self.main_text += ") {\n"

    def function_offset(self, offset: int):
        """it should be called once per function"""
        self.reg += offset + 1

    def ret_function(self, value, value_type: Any):
        v_t = self.mapper(value_type)
        self.main_text += f"ret {v_t} {value}\n"

    def exitFunction(self):
        if len(self.reg_stack) > 0:
            self.reg = self.reg_stack.pop()
            self.main_text += "}\n"
        else:
            raise RuntimeError(f"Attempted to pop empty reg_stack when reg {self.reg}")

    def getLabel(self):
        self.label += 1
        return f"label{self.label}"

    def emitLabel(self, label):
        self.main_text += f"{label}:\n"

    def goToLabel(self, label):
        self.main_text += f"br label %{label}\n"

    @__dec
    def printf_i32(self, id):
        self.load_i32(id)
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpi, i32 0, i32 0), i32 %"
            + str(self.reg - 1)
            + ")\n"
        )

    @__dec
    def printf_undefined_i32(self, id):
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpi, i32 0, i32 0), i32 "
            + id
            + ")\n"
        )

    @__dec
    def printf_real(self, id):
        self.load_real(id)
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]*  @strpd, i32 0, i32 0), double %"
            + str(self.reg - 1)
            + ")\n"
        )

    @__dec
    def printf_undefined_real(self, id):
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([5 x i8], [5 x i8]*  @strpd, i32 0, i32 0), double "
            + id
            + ")\n"
        )

    @__dec
    def printf_str(self):
        self.header_text += f"""@.str{self.reg} = private unnamed_addr constant [4 x i8] c"%s\\0A\\00"\n"""  # +2 bo dodajemy dwa znaki
        self.main_text += f"""%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @.str{self.reg}, i32 0, i32 0), i8* %{self.reg -1})\n"""

    @__dec
    def printf_undefined_str(self, id):
        self.header_text += f"""@.str{self.reg} = private unnamed_addr constant [{len(id)+2} x i8] c"{id}\\0A\\00"\n"""  # +2 bo dodajemy dwa znaki
        self.main_text += f"""%{self.reg} = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([{len(id)+2} x i8], [{len(id)+2} x i8]* @.str{self.reg}, i32 0, i32 0), i8* %{self.reg -1})\n"""

    @__dec
    def scanf_i32(self, id):
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32* %{id})\n"

    @__dec
    def scanf_double(self, id):
        self.main_text += f"%{self.reg} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([5 x i8], [5 x i8]* @strpd, i32 0, i32 0), double* %{id})\n"

    def declare_i32(self, id):
        self.main_text += f"%{id} = alloca i32\n"

    def declare_real(self, id):
        self.main_text += f"%{id} = alloca double\n"

    def declare_str(self, id, text):
        self.main_text += f"%{id} = alloca [{len(text)-1} x i8]\n"

    def assign_i32(self, id, value):
        self.main_text += f"store i32 {value}, i32* %{id}\n"

    def assign_real(self, id, value):
        self.main_text += f"store double {value}, double* %{id}\n"

    @__dec
    def assign_str(self, id, value):
        self.header_text += f"""@{id} = private unnamed_addr constant [{len(value)} x i8] c{value}\\00"\n"""
        self.main_text += (
            "%"
            + str(self.reg)
            + "= bitcast ["
            + str(len(value))
            + " x i8]* %"
            + id
            + " to i8*\n"
        )
        self.main_text += f"call void @llvm.memcpy.p0i8.p0i8.i64(i8* %{self.reg}, i8* getelementptr inbounds ([{len(value)} x i8], [{len(value)} x i8]* @{id}, i32 0, i32 0), i64 {len(value)}, i32 1, i1 false)\n"

    def assign_array_i32(self, id, size: int):
        ty = "i32"
        self.main_text += f"%{id} = alloca [{size} x {ty}]\n"

    def assign_array_double(self, id, size: int):
        ty = "double"
        self.main_text += f"%{id} = alloca [{size} x {ty}]\n"

    @__dec
    def store_array_i32(self, id, offset: int, value, size: int):
        ty = "i32"
        self.main_text += f"%{self.reg} = getelementptr inbounds [{size} x {ty}], [{size} x {ty}]* %{id}, i32 0, i32 {offset}\n"
        self.main_text += f"store {ty} {value}, {ty}* %{self.reg}\n"

    @__dec
    def store_array_double(self, id, offset: int, value, size: int):
        ty = "double"
        self.main_text += f"%{self.reg} = getelementptr inbounds [{size} x {ty}], [{size} x {ty}]* %{id}, i32 0, i32 {offset}\n"
        self.main_text += f"store {ty} {value}, {ty}* %{self.reg}\n"

    @__dec
    def load_i32(self, id):
        self.main_text += f"%{self.reg} = load i32, i32* %{id}\n"

    @__dec
    def load_real(self, id):
        self.main_text += f"%{self.reg} = load double, double* %{id}\n"

    @__dec
    def load_str(self, id, text1):
        self.main_text += f"%{self.reg} = getelementptr inbounds [{len(text1)-1} x i8], [{len(text1)-1} x i8]* %{id}, i32 0, i32 0\n"

    @__dec
    def load_array_i32(self, id, offset: int, size: int):
        ty = "i32"
        self.main_text += f"%{self.reg} = getelementptr inbounds [{size} x {ty}], [{size} x {ty}]* %{id}, i32 0, i32 {offset}\n"
        self.reg += 1
        self.main_text += f"%{self.reg} = load {ty}, {ty}* %{self.reg-1}\n"

    @__dec
    def load_array_double(self, id, offset: int, size: int):
        ty = "double"
        self.main_text += f"%{self.reg} = getelementptr inbounds [{size} x {ty}], [{size} x {ty}]* %{id}, i32 0, i32 {offset}\n"
        self.reg += 1
        self.main_text += f"%{self.reg} = load {ty}, {ty}* %{self.reg-1}\n"

    @__dec
    def add_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = add i32 " + val1 + ", " + val2 + "\n"
        )

    @__dec
    def add_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fadd double " + val1 + ", " + val2 + "\n"
        )

    @__dec
    def add_str(self, val1, val2):
        self.main_text += (
            f"%{self.reg} = call i8* @strcat(i8* %{self.reg-2}, i8* %{self.reg-1})\n"
        )

    @__dec
    def sub_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = sub i32 " + val2 + ", " + val1 + "\n"
        )

    @__dec
    def sub_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fsub double " + val2 + ", " + val1 + "\n"
        )

    @__dec
    def mul_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = mul i32 {val1}, {val2}\n"

    @__dec
    def mul_real(self, val1, val2):
        self.main_text += f"%{self.reg} = fmul double {val1}, {val2}\n"

    @__dec
    def div_i32(self, val1, val2):
        self.main_text += f"%{self.reg} = sdiv i32 {val2}, {val1}\n"

    @__dec
    def div_real(self, val1, val2):
        self.main_text += f"%{self.reg} = fdiv double {val2}, {val1}\n"

    @__dec
    def sitofp(self, id):
        self.main_text += f"%{self.reg} = sitofp i32 {id} to double\n"

    @__dec
    def fptosi(self, id):
        self.main_text += f"%{self.reg} = fptosi double {id} to i32\n"

    def comment(self, text):
        self.main_text += f"    ; {text} \n"

    def conditional_branch(self, condition, l_if_then, l_if_else):
        self.main_text += f"br i1 {condition}, label %{l_if_then}, label %{l_if_else}\n"

    @__dec
    def eq(self, id, value):
        self.main_text += f"%{self.reg} = icmp eq i32 {id}, {value}\n"

    @__dec
    def ne(self, id, value):
        self.main_text += f"%{self.reg} = icmp ne i32 {id}, {value}\n"

    @__dec
    def slt(self, id, value):
        self.main_text += f"%{self.reg} = icmp slt i32 {id}, {value}\n"

    @__dec
    def sle(self, id, value):
        self.main_text += f"%{self.reg} = icmp sle i32 {id}, {value}\n"

    @__dec
    def sgt(self, id, value):
        self.main_text += f"%{self.reg} = icmp sgt i32 {id}, {value}\n"

    @__dec
    def sge(self, id, value):
        self.main_text += f"%{self.reg} = icmp sge i32 {id}, {value}\n"

    @__dec
    def generate(self):
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += "declare i8* @strcat(i8*, i8*)\n"
        text += '@strpi = constant [4 x i8] c"%d\\0A\\00"\n'
        text += "declare void @llvm.memcpy.p0i8.p0i8.i64(i8* nocapture, i8* nocapture readonly, i64, i32, i1)\n"
        text += '@strpd = constant [5 x i8] c"%lf\\0A\\00"\n'
        text += '@strs = constant [3 x i8] c"%d\\00"\n'
        text += self.header_text
        # text += "define i32 @main() nounwind{\n"
        text += self.main_text
        # text += "ret i32 0 }\n"
        return text
