

from src.compiler.src_parser.preprocessor import preprocess
from src.compiler.src_parser.tokenizer import tokenize





def parse_file(input: str) -> str:
    preprocessed_file = preprocess(input)
    token_list = tokenize(preprocessed_file)
    return token_list