
from src.compiler.src_parser.token_switch import identify_token




class token:
    def __init__(self, type = "", level = 0, data = [], source_line = 0):
        self.type = type
        self.level = level
        self.data = data
        self.source_line = source_line

    def __repr__(self):
        return f"\"type: {self.type}, level: {self.level}, data: {self.data}, sourceline: {self.source_line}\""

def tokenize(input: str) -> str:
    input = "".join(input)

    instruction_list = []

    running_string = ""
    for character in input:
        if([" ", "(", ")", ";", "{", "}", ","].count(character) == 1):
            if(running_string != ""):
                instruction_list.append(running_string)
            if(character != " "):
                instruction_list.append(character)
            running_string = ""
        else:
            running_string += character

    token_list = []
    current_level = 0
    current_token = token()
    i = 0
    instruction_start_index = 0
    for instruction in instruction_list:
        if(([";", "{", "}"].count(instruction_list[i - 1]) == 1 or i == 0) and [";", "{", "}"].count(instruction) == 0):
            current_token.source_line = instruction
        elif(([";", "{", "}"].count(instruction_list[i - 2]) == 1 or i == 1) and [";", "{", "}"].count(instruction) == 0):
            current_token.level = current_level
            if(["int", "while"].count(instruction) == 1):
                current_token.type = identify_token(instruction, current_token.source_line, third_char= instruction_list[i + 2], instruction_list= instruction_list, current_index= i)
            elif(instruction_list.__len__() > i + 1 and instruction_list[i + 1] == "="):
                current_token.type = identify_token(instruction, current_token.source_line, second_char= instruction_list[i + 1])
                current_token.data.append(instruction)
            else:
                current_token.type = identify_token(instruction, current_token.source_line)

        elif([";", "{", "}"].count(instruction) == 1):
            if(current_token.type != ""):
                token_list.append(current_token)
            current_token = token()
            current_token.data = []

            match instruction:
                case "{":
                    current_level += 1
                case "}":
                    current_level -= 1
                case _:
                    pass

        else:
            if(["(", ")", "=", ","].count(instruction) == 0):
                current_token.data.append(instruction)
        i += 1
    return token_list