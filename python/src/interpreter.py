from src.logs import runtimeError, runWarning
import sys

class Interpreter:
    def __init__(self, code):
        self.data = [0] * 30000
        self.code = code

    def create_jumps_dictionary(self):
        left = []
        res = {}

        for index, command in enumerate(self.code):
            if command == '[':
                left.append(index)
            elif command == ']':
                if len(left) == 0:
                    runtimeError("mismatched parentheses at index %s" % index, "syntax")

                lbrace_index = left.pop()
                res[lbrace_index] = index
                res[index] = lbrace_index

        if len(left) > 0:
            runtimeError("mismatched parentheses at index %s" % left.pop(), "syntax")
        return res

    def run(self):
        final = ""

        jumps = self.create_jumps_dictionary()
        data = {}

        data_pointer = 0
        instruction_pointer = 0

        while instruction_pointer < len(self.code):
            command = self.code[instruction_pointer]

            if command == '>':
                data_pointer += 1
            elif command == '<':
                data_pointer -= 1
            elif command == '+':
                data[data_pointer] = (data.get(data_pointer, 0) + 1)
                if data[data_pointer] == 2 ** 8:
                    data[data_pointer] = 0
            elif command == '-':
                data[data_pointer] = (data.get(data_pointer, 0) - 1)
                if data[data_pointer] == -1:
                    data[data_pointer] = 2 ** 8 - 1
            elif command == ',':
                data[data_pointer] = ord(sys.stdin.read(1)) % 256
            elif command == '.':
                final += chr(data.get(data_pointer, 0))
            elif command == '[':
                if data.get(data_pointer, 0) == 0:
                    instruction_pointer = jumps[instruction_pointer]
            elif command == ']':
                if data.get(data_pointer, 0) != 0:
                    instruction_pointer = jumps[instruction_pointer]
            else:
                pass

            instruction_pointer += 1

        if data_pointer != 0:
            runWarning("at the end of the execution the data pointer is %s instead of 0 (possibly a compiler issue)" % str(data_pointer))

        return final