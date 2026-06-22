








def substitute_inst(token):
    type = token.type
    data = token.data

    match type:
        case "clockspeed":
            return f"clockspeed {data[0]}"
        case "func":
            if(data[0] != "main"):
                return "fuctions not yet supported"
            else:
                return ""
        case "varinit":
            return f"buffer {data[1]}\nsave {data[0]}"
        case "varinitexpression":
            expression = data[1:]
            i = 0
            while(i < expression.__len__()):
                if(["+", "-", "*", "/", "="].count(expression[i]) == 0 and not expression[i].isnumeric()):
                    expression[i] = f"${expression[i]}$"
                i += 1
            return f"eval {"".join(expression)}\nsave {data[0]}"
        case "expression":
            expression = data[1:]
            i = 0
            while (i < expression.__len__()):
                if (["+", "-", "*", "/", "="].count(expression[i]) == 0 and not expression[i].isnumeric()):
                    expression[i] = f"${expression[i]}$"
                i += 1
            return f"eval {"".join(expression)}\nsave {data[0]}"
        case "rorin":
            return f"listen {data[0].replace("\"","").split("%")[0]}\nsave {data[1].replace("&", "")}"
        case "rorout":
            return f"load {data[1]}\nround\nsend {data[0].replace("\"","").split("%")[0]}"
        case "infloop":
            return "infloop"
        case _:
            print(f"token type {type} at line {token.source_line} is undefined or not supported.")
            return "undefined"