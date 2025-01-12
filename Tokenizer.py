# Tokenizer.py
# Jan 3, 2025
# Jan 11, 2025 Updated, some cleanup and data veriification
# This file is still in the very early stages of development
# Break a simple c.source code file into tokens
from dataclasses import dataclass, field
from typing import Dict
import re


from TokenType import TokenType, Delimiters, Keywords, Operators
from TokenType import TokenBase
# from Parser import Parser



# C Source code file
TEST_FILE = 'j:/compiler/c_files/memmgr.c'

def main():

    # Load our test c source
    code = load_code(TEST_FILE)

    # Build Very Large Regex
    pattern = build_regex()

    # Perform regex on entire file
    match = re.findall(pattern, code, re.DOTALL)

    # Based on our regex, these groups will be filled in with their appropriate members
    match_index_to_base = {
    0: TokenBase.COMMENT_ML, 1: TokenBase.COMMENT_SL, 2: TokenBase.PREPROCESSOR,
    5: TokenBase.LITERAL, 6: TokenBase.WORD,
    7: TokenBase.OPERATOR, 8: TokenBase.DELIM}

    # Build a list of all tokens
    tokens = []
    key_gen = get_next_key()
    for e in match:
        for k, v in match_index_to_base.items():
            token = {}
            if e[k]:
                assert(token == {}) # Error multiple matches
                token = Token()
                token.Id = next(key_gen)
                token.base = v
                token.value = e[k]
            if token:
                tokens.append(token)

    # debug print
    for e in tokens:
        print(e)

    # Modifies and prints token data
    # Modification is in place, thus no return.
    modify_tokens_add_ofType_data(tokens)


    # parser = Parser(tokens)
    # ast = parser.parse()
    # print(ast)


# Used for token IDs
def get_next_key():
    key = 0
    while True:
        yield key
        key += 1

@dataclass
class Token:
    Id: Dict = field(default_factory=dict)   # Unique identifier for the token
    base: Dict = field(default_factory=dict) # Token base e.g.
    ofType: Dict = field(default_factory=dict) # Specific type (e.g., Keywords)
    value: Dict = field(default_factory=dict) # Value of the token (e.g., 'int')

    def __str__(self):
        if self.ofType:
            return f'{self.Id:3} {self.base:18} {self.ofType:18} {self.value:18}'
        else:
            return f'{self.Id:3} {self.base:18}{" "*18}{self.value:18}'

def modify_tokens_add_ofType_data(tokens):

    print('DELIMS:')
    tokens_sublist = [x for x in tokens if x.base == TokenBase.DELIM]
    for token in tokens_sublist:
        if Delimiters.to_name(token.value):
            token.ofType = Delimiters.to_name(token.value)
            print(token)

    print('KEYWORDS:')
    tokens_sublist = [x for x in tokens if x.base == TokenBase.WORD]
    for token in tokens_sublist:
        if token.value in Keywords._mapping:
            token.base = TokenBase.KEYWORD
            token.ofType = Keywords.to_name(token.value)
            print(token)

    print('IDENTIFIERS:')
    tokens_sublist = [x for x in tokens_sublist if x.base == TokenBase.WORD]
    for token in tokens_sublist:
        token.base = TokenBase.IDENTIFIER
        print(token)

    print('LITERALS:')
    tokens_sublist = [x for x in tokens if x.base == TokenBase.LITERAL]
    for token in tokens_sublist:
        print(token)

    print('OPERATORS:')
    tokens_sublist = [x for x in tokens if x.base == TokenBase.OPERATOR]
    for token in tokens_sublist:
        if token.value in Operators._mapping:
            token.ofType = Operators.to_name(token.value)
            print(token)

    print('UNRECOGNIZED OPERATORS:')
    for token in tokens_sublist:
        if token.ofType == None:
            print(token)
    else:
        print('NONE!')


# Import the c.source code, join all lines
def load_code(c_file):
    with open(c_file, 'r') as file:
        lines = file.readlines()

    return ''.join([line for line in lines])


# Build a regex that captures all tokens
def build_regex():

    ml_comment = r"/\*(?:[^\*]|\*[^\/])*\*/" # multiline comment
    comment = r"//[^\n]*"
    directives = r"\s*\#\s*(?:\w+)\b(?:[ \t]+(?:[^\n]*))?"
    numeric_literal = r"(?:0b)?[\d][.\d]?[\d]*"
    string_literal = r"\"(?:[^\"\\]|\\.)*\""
    char_literal = r"\'(?:[^\'\\]|\\.)*\'"
    bool_literal = r"true|false"
    identifier = r"[a-zA-Z_]+[a-zA-Z_\d]*"
    operators = r"[\+\-\*\/\%\=\!\<\>\&\|\^\~\?\:]+"
    delimiters = r"[\{\}\(\)\[\]\,\.\;]"
    return r"("+ml_comment+r")|("+comment+r")|("+directives+r")(\n)|(\n)|("+numeric_literal+r"|"+string_literal+r"|"+char_literal+r"|"+bool_literal+r")|("+identifier+r")|("+operators+r")|("+delimiters+r")"




if __name__ == '__main__':
    main()
