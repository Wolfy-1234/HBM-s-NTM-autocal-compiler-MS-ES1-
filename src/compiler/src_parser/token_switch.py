








def identify_token(input: str, source_line, second_char = "", third_char = "", instruction_list = [str], current_index = 0) ->str:
    token = ""
    match input:
        case "//#clockspeed":
            return "clockspeed"
        case "int":
            if(third_char == "("):
                return "func"
            else:
                i = current_index + 2
                while([";", "{", "}"].count(instruction_list[i]) == 0):
                    instruction = instruction_list[i]
                    if(["+", "-", "*", "/", "="].count(instruction) == 0 and not instruction.isnumeric()):
                        return "varinitexpression"
                    i += 1
                return "varinit"
        case "scanf":
            return "rorin"
        case "printf":
            return "rorout"
        case "while":
            if(instruction_list[current_index + 2] == "true"):
                return "infloop"
            else:
                return "not supported yet"
        case "if":
            return "if"
        case _:
            if(second_char == "="):
                return "expression"
            else:
                print(f"{input} at line {source_line} is undefined or not supported, and will be ignored")
                return "undefined"