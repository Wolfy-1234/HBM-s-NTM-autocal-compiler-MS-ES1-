








def preprocess(input:str) -> str:
    text = input.split("\n")

    delete_mode = False

    line_num = 1
    i = 0
    while(i < text.__len__()):
        text[i] = text[i].strip()
        line = text[i]

        if(delete_mode):
            if(line[0:2] == "*/"):
                delete_mode = False
            del text[i]
            i -= 1

        elif(line == ""):
            del text[i]
            i -= 1

        elif(line[0:8] == "#include"):
            del text[i]
            i -= 1

        elif(line[0:2] == "//"):
            if(line[2:13] == "#clockspeed"):
                text[i] = f"{line_num} " + text[i]
                if(not line[-1] == ";"):
                    text[i] += ";"
            else:
                del text[i]
                i -= 1
        elif(line[0:2] == "/*"):
            delete_mode = True
            del text[i]
            i -= 1
        else:
            text[i] = f"{line_num} " + text[i]

        i += 1
        line_num += 1


    return text