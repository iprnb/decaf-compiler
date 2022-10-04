import sys

from parser import LLOneParser
from tokenizer import Tokenizer
from utils import convert_tokens

if __name__ == '__main__':
    input_file_address = sys.argv[1]
    decaf_code = open(input_file_address).read()

    decaf_tokenizer = Tokenizer(decaf_code)
    tokens, symbols_table = decaf_tokenizer.run()

    ll_one_parser = LLOneParser(" ".join(convert_tokens(tokens, symbols_table)))
    abstract_syntax_tree_string = ll_one_parser.get_ast_string()

    tokens_file = open("source_tokens.txt", "w")
    symbols_table_file = open("source_symbols_table.txt", "w")
    abstract_syntax_tree_file = open("sample_code.txt", "w")
    tokens_string = "\n".join(["\t".join(list(map(str, tokens[i]))) for i in range(len(tokens))])
    tokens_file.write(tokens_string)
    symbols_table_string = "\n".join([str(i + 1) + "\t" + s for i, s in enumerate(symbols_table)])
    symbols_table_file.write(symbols_table_string)
    abstract_syntax_tree_file.write(abstract_syntax_tree_string)
