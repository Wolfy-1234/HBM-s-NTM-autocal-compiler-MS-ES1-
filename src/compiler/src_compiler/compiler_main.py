
from src.compiler.src_compiler.instruction_substitution import substitute_inst







def compile(input):
    open_loops = []
    output = []
    i = 0
    for token in input:
        for loop in open_loops:
            if(loop[1] >= token.level):
                output.append(f"jmp {loop[0]}")
                open_loops.remove(loop)

        instruction = substitute_inst(token)
        if(instruction == "infloop"):
            name = f"infloop{open_loops.__len__() + 1}"
            output.append(f"dest {name}")
            open_loops.append((name, token.level))
        elif(instruction != ""):
            output.append(instruction)

        i += 1

    if(open_loops.__len__() > 0):
        for loop in reversed(open_loops):
            output.append(f"jmp {loop[0]}")

    return output