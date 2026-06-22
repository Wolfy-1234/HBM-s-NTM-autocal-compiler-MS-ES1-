
from src.compiler.src_compiler.instruction_substitution import substitute_inst







def compile(input):
    open_levels = []
    output = []
    i = 0
    for token in input:
        for loop in open_levels:
            if(loop[1] >= token.level):
                if(loop[0][0:2] == "if"):
                    output.append(f"dest {loop[0]}")
                else:
                    output.append(f"jmp {loop[0]}")
                open_levels.remove(loop)

        instruction = substitute_inst(token)
        if(instruction == "infloop"):
            name = f"infloop{open_levels.__len__() + 1}"
            output.append(f"dest {name}")
            open_levels.append((name, token.level))
        elif(token.type == "if"):
            name = f"if{open_levels.__len__() + 1}"
            output.append(instruction)
            output.append(f"jmpif {name + "do"}")
            output.append(f"jmp {name}")
            output.append(f"dest {name + "do"}")
            open_levels.append((name, token.level))

        elif(instruction != ""):
            output.append(instruction)

        i += 1

    if(open_levels.__len__() > 0):
        for loop in reversed(open_levels):
            output.append(f"jmp {loop[0]}")

    return output