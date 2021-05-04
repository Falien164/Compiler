class LLVMGenerator:
    def __init__(self):
        self.header_text = ""
        self.main_text = ""
        self.reg = 1

    @staticmethod
    def printf_i32(self, id):
        self.load_i32(self, id)
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpi, i32 0, i32 0), i32 %"
            + str(self.reg - 1)
            + ")\n"
        )
        self.reg += 1

    @staticmethod
    def printf_undefined_i32(self, id):
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpi, i32 0, i32 0), i32 "
            + id
            + ")\n"
        )
        self.reg += 1

    @staticmethod
    def printf_real(self, id):
        self.load_real(self, id)
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpd, i32 0, i32 0), double %"
            + str(self.reg - 1)
            + ")\n"
        )
        self.reg += 1

    @staticmethod
    def printf_undefined_real(self, id):
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds ([4 x i8], [4 x i8]*  @strpd, i32 0, i32 0), double "
            + id
            + ")\n"
        )
        self.reg += 1

    @staticmethod
    def printf_str(self, id):
        # matched_lines = [line for line in self.main_text.split('\n') if "@"+id in line]
        # print(matched_lines)
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds (["
            + str(len(id))
            + " x i8], ["
            + str(len(id))
            + " x i8]* @"
            + id
            + ", i32 0, i32 0))\n"
        )
        self.reg += 1

    @staticmethod
    def printf_undefined_str(self, id):
        self.header_text += (
            "@.str"
            + str(self.reg)
            + " = private unnamed_addr constant ["
            + str(len(id) + 2)
            + ' x i8] c"'
            + id
            + '\\0A\\00"\n'
        )  # +2 bo dodajemy dwa znaki
        self.main_text += (
            "%"
            + str(self.reg)
            + " = call i32 (i8*, ...) @printf(i8* getelementptr inbounds (["
            + str(len(id) + 2)
            + " x i8], ["
            + str(len(id) + 2)
            + " x i8]* @.str"
            + str(self.reg)
            + ", i32 0, i32 0))\n"
        )
        self.reg += 1

    @staticmethod
    def scanf_i32(self, id):
        self.main_text += f"%{self.req} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpi, i32 0, i32 0), i32* %{id})\n"
        self.req += 1

    def scanf_double(self, id):
        self.main_text += f"%{self.req} = call i32 (i8*, ...) @__isoc99_scanf(i8* getelementptr inbounds ([4 x i8], [4 x i8]* @strpd, i32 0, i32 0), double* %{id})\n"
        self.req += 1

    @staticmethod
    def declare_i32(self, id):
        self.main_text += f"%{id} = alloca i32\n"

    @staticmethod
    def declare_real(self, id):
        self.main_text += f"%{id} = alloca double\n"

    @staticmethod
    def assign_i32(self, id, value):
        self.main_text += f"store i32 {value}, i32* %{id}\n"

    @staticmethod
    def assign_real(self, id, value):
        self.main_text += f"store double {value}, double* %{id}\n"

    # @staticmethod
    # def assign_str(self, id, value):
    #     self.header_text += "@"+id+" = private unnamed_addr constant ["+str(len(value)+1)+" x i8] c"+value+"\\0A\\00\"\n"
    #     self.main_text += "%" +str(self.reg)+"= bitcast ["+str(len(value)+1)+"x i8]* @"+id+" to i8*\n"
    #     self.reg+=1

    @staticmethod
    def load_i32(self, id):
        self.main_text += "%" + str(self.reg) + " = load i32, i32* %" + id + "\n"
        self.reg += 1

    @staticmethod
    def load_real(self, id):
        self.main_text += "%" + str(self.reg) + " = load double, double* %" + id + "\n"
        self.reg += 1

    @staticmethod
    def add_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = add i32 " + val1 + ", " + val2 + "\n"
        )
        self.reg += 1

    @staticmethod
    def add_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fadd double " + val1 + ", " + val2 + "\n"
        )
        self.reg += 1

    @staticmethod
    def sub_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = sub i32 " + val2 + ", " + val1 + "\n"
        )
        self.reg += 1

    @staticmethod
    def sub_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fsub double " + val2 + ", " + val1 + "\n"
        )
        self.reg += 1

    @staticmethod
    def mul_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = mul i32 " + val1 + ", " + val2 + "\n"
        )
        self.reg += 1

    @staticmethod
    def mul_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fmul double " + val1 + ", " + val2 + "\n"
        )
        self.reg += 1

    @staticmethod
    def div_i32(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = sdiv i32 " + val2 + ", " + val1 + "\n"
        )
        self.reg += 1

    @staticmethod
    def div_real(self, val1, val2):
        self.main_text += (
            "%" + str(self.reg) + " = fdiv double " + val2 + ", " + val1 + "\n"
        )
        self.reg += 1

    @staticmethod
    def sitofp(self, id):
        self.main_text += f"%{self.reg} = sitofp i32 {id} to double\n"
        self.reg += 1

    @staticmethod
    def fptosi(self, id):
        self.main_text += f"%{self.reg} = fptosi double {id} to i32\n"
        self.reg += 1

    @staticmethod
    def generate(self):
        text = ""
        text += "declare i32 @printf(i8*, ...)\n"
        text += "declare i32 @__isoc99_scanf(i8*, ...)\n"
        text += '@strpi = constant [4 x i8] c"%d\\0A\\00"\n'
        text += '@strpd = constant [4 x i8] c"%f\\0A\\00"\n'
        text += '@strs = constant [3 x i8] c"%d\\00"\n'
        text += self.header_text
        text += "define i32 @main() nounwind{\n"
        text += self.main_text
        text += "ret i32 1 }\n"
        return text
