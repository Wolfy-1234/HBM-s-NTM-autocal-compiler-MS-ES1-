

from src.compiler.src_parser.parser_main import parse_file
from src.compiler.src_compiler.compiler_main import compile

def main():
    #file_name = input("Name of the file to compile: ")
    file_name = "C:\\Users\\Iacopo\\Desktop\\python\\HBM-s-NTM-autocal-compiler-MS-ES1-\\tests\\fibonacci-branching-test\\fibonacci-branching-test.C"

    input_C = ""
    with open(file_name, "r") as input_file:
        input_C = input_file.read()

    intermediate_source = parse_file(input_C)
    for x in intermediate_source:
        print(x)

    compiled_code = compile(intermediate_source)
    for x in compiled_code:
        print(x)

if(__name__ == "__main__"):
    main()