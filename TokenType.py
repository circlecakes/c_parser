from enum import Enum


class TokenBase(Enum):
    COMMENT_ML  = 'comment_ml'
    COMMENT_SL  = 'comment_sl'
    PREPROCESSOR = 'preprocessor'
    LITERAL     = 'literal'
    WORD        = 'unresolved_word'
    IDENTIFIER  = 'identifier'
    KEYWORD     = 'keyword'
    OPERATOR    = 'operator'
    DELIM       = 'delim'



class TokenType(Enum):
    ERROR            = 'error'
    COMMENT_SL       = 'comment_sl'
    COMMENT_ML       = 'comment_ml'
    PREPROCESSOR     = 'preprocessor'
    KEYWORD_SPECIAL  = 'keyword_special'
    KEYWORD_INT      = 'keyword_int'
    KEYWORD_FLOAT    = 'keyword_float'
    KEYWORD_CHAR     = 'keyword_char'
    KEYWORD_IF       = 'keyword_if'
    KEYWORD_ELSE     = 'keyword_else'
    KEYWORD_WHILE    = 'keyword_while'
    KEYWORD_FOR      = 'keyword_for'
    KEYWORD_RETURN   = 'keyword_return'
    KEYWORD_VOID     = 'keyword_void'
    KEYWORD_BREAK    = 'keyword_break'
    KEYWORD_CONTINUE = 'keyword_continue'
    KEYWORD_STRUCT   = 'keyword_struct'
    KEYWORD_TYPEDEF  = 'keyword_typedef'
    KEYWORD_CONST    = 'keyword_const'
    KEYWORD_STATIC   = 'keyword_static'
    IDENTIFIER       = 'identifier'
    LITERAL_SPECIAL  = 'literal_special'
    LITERAL_INT      = 'literal_int'
    LITERAL_FLOAT    = 'literal_float'
    LITERAL_CHAR     = 'literal_char'
    LITERAL_STRING   = 'literal_string'
    OPERATOR_SPECIAL = 'operator_special'
    OPERATOR_UNARY   = 'operator_unary'
    OPERATOR_ARITHMETIC = 'operator_arithmetic'
    OPERATOR_RELATIONAL = 'operator_relational'
    OPERATOR_LOGICAL = 'operator_logical'
    OPERATOR_BITWISE = 'operator_bitwise'
    OPERATOR_ASSIGNMENT = 'operator_assignment'
    OPERATOR_TERNARY = 'operator_ternary'
    DELIM_SPECIAL    = 'delim_special'
    DELIM_LPAREN     = 'delim_lparen'
    DELIM_RPAREN     = 'delim_rparen'
    DELIM_LBRACE     = 'delim_lbrace'
    DELIM_RBRACE     = 'delim_rbrace'
    DELIM_LBRACKET   = 'delim_lbracket'
    DELIM_RBRACKET   = 'delim_rbracket'
    DELIM_SEMICOLON  = 'delim_semicolon'
    DELIM_COMMA      = 'delim_comma'

    @classmethod
    def from_value(cls, value):
        for member in cls:
            if member.value == value:
                return member
        raise ValueError(f"{value} is not a valid {cls.__name__}")


class Operators:
    # Make sure to include struct_deref (->) and elipsis at some point
    _mapping = {
            '&': 'operator_special',
            ':': 'operator_special',
            '*': 'operator_special',
            '=': 'operator_assignment',
            '+=': 'operator_assignment',
            '-=': 'operator_assignment',
            '*=': 'operator_assignment',
            '/=': 'operator_assignment',
            '+': 'operator_arithmetic',
            '-': 'operator_arithmetic',
            # '*': 'operator_arithmetic',
            '/': 'operator_arithmetic',
            '%': 'operator_arithmetic',
            '==': 'operator_relational',
            '!=': 'operator_relational',
            '<': 'operator_relational',
            '<=': 'operator_relational',
            '>': 'operator_relational',
            '>=': 'operator_relational',
            '&&': 'operator_logical',
            '||': 'operator_logical',
            '!': 'operator_logical',
            '?': 'operator_ternary',
            ':': 'operator_ternary',
            'sizeof': 'operator_unary',
            # ':': 'operator_unary',
            '*': 'operator_unary',
            # '&': 'operator_unary',
            # '&': 'operator_bitwise',
            '|': 'operator_bitwise',
            '^': 'operator_bitwise',
            '~': 'operator_bitwise',
            '<<': 'operator_bitwise',
            '>>': 'operator_bitwise'
    }
    _reverse_mapping = {v: k for k, v in _mapping.items()}

    @classmethod
    def to_name(cls, symbol):
        return cls._mapping.get(symbol, f"Unknown symbol: {symbol}")

    @classmethod
    def to_symbol(cls, name):
        return cls._reverse_mapping.get(name, f"Unknown name: {name}")

    @classmethod
    def all_symbols(cls):
        return list(cls._mapping.keys())

    @classmethod
    def all_names(cls):
        return list(cls._mapping.values())


class Delimiters:
    _mapping = {
        '(': 'delim_lparen',
        ')': 'delim_rparen',
        '[': 'delim_lbrace',
        ']': 'delim_rbrace',
        '{': 'delim_lcurly',
        '}': 'delim_rcurly',
        ';': "delim_semicolon",
        '.': "delim_dot",
        ',': "delim_comma"
    }
    _reverse_mapping = {v: k for k, v in _mapping.items()}

    @classmethod
    def to_name(cls, symbol):
        return cls._mapping.get(symbol, f"Unknown symbol: {symbol}")

    @classmethod
    def to_symbol(cls, name):
        return cls._reverse_mapping.get(name, f"Unknown name: {name}")

    @classmethod
    def all_symbols(cls):
        return list(cls._mapping.keys())

    @classmethod
    def all_names(cls):
        return list(cls._mapping.values())


class Keywords:
    _mapping = {
        'int': 'keyword_int',
        'float': 'keyword_float',
        'char': 'keyword_char',
        'if': 'keyword_if',
        'else': 'keyword_else',
        'while': 'keyword_while',
        'for': 'keyword_for',
        'return': 'keyword_return',
        'void': 'keyword_void',
        'break': 'keyword_break',
        'continue': 'keyword_continue',
        'struct': 'keyword_struct',
        'typedef': 'keyword_typedef',
        'const': 'keyword_const',
        'static': 'keyword_static',
        'union': 'keyword_union',
        'sizeof': 'keyword_sizeof'}
    _reverse_mapping = {v: k for k, v in _mapping.items()}

    @classmethod
    def to_name(cls, symbol):
        return cls._mapping.get(symbol, f"Unknown symbol: {symbol}")

    @classmethod
    def to_symbol(cls, name):
        return cls._reverse_mapping.get(name, f"Unknown name: {name}")

    @classmethod
    def all_symbols(cls):
        return list(cls._mapping.keys())

    @classmethod
    def all_names(cls):
        return list(cls._mapping.values())



## Notes Section


#preprocessing-tokens:
# header-name
# identifier
# pp-number
# character-constant
# string-literal
# punctuator

# Ambiguous

#    &, *, :

# Assignment:

#     =, +=, -=, *=, /=

# Arithmetic:

#     +, -, *, /, %

# Relational:

#     ==, !=, <, <=, >, >=

# Logical:

#     &&, ||, !

# Ternary:

#     ?, :

# Unary:

#    sizeof, ?, :, *, &

# Bitwise:

#     &, |, ^, ~, <<, >>

# Full Keyword List

# auto break case char const continue
# default do double else enum extern
# float for goto if inline int long
# register restrict return short signed
# sizeof static struct switch typedef union
# unsigned void volatile while _Alignas
# _Alignof _Atomic _Bool _Complex _Generic
# _Imaginary _Noreturn _Static_assert
# _Thread_local

# Most common Keywords

# int
# float
# char
# if
# else
# while
# for
# return
# void
# break
# continue
# struct
# typedef
# const
# static

# class _Keywords(Enum):
#     KEYWORD_SPECIAL  = 'special'
#     KEYWORD_INT      = 'int'
#     KEYWORD_FLOAT    = 'float'
#     KEYWORD_CHAR     = 'char'
#     KEYWORD_IF       = 'if'
#     KEYWORD_ELSE     = 'else'
#     KEYWORD_WHILE    = 'while'
#     KEYWORD_FOR      = 'for'
#     KEYWORD_RETURN   = 'return'
#     KEYWORD_VOID     = 'void'
#     KEYWORD_BREAK    = 'break'
#     KEYWORD_CONTINUE = 'continue'
#     KEYWORD_STRUCT   = 'struct'
#     KEYWORD_TYPEDEF  = 'typedef'
#     KEYWORD_CONST    = 'const'
#     KEYWORD_STATIC   = 'static'

# DELIM_SYMBOLS = (("delim_special", ''),
#     ("delim_lparen", '('),
#     ("delim_rparen", ')'),
#     ("delim_lbrace", '['),
#     ("delim_rbrace", ']'),
#     ("delim_lbracket", '{'),
#     ("delim_rbracket", '}'),
#     ("delim_semicolon", ';'),
#     ("delim_comma", ','))

# OPERATOR_SYMBOLS = ('operator_special', ('&', ':', '*')), ('operator_assignment', ('=', '+=', '-=', '*=', '/=')), ('operator_arithmetic', ('+', '-', '*', '/', '%')), ('operator_relational', ('==', '!=', '<', '<=', '>', '>=')), ('operator_logical', ('&&', '||', '!')), ('operator_ternary', ('?', ':')), ('operator_unary', ('sizeof', ':', '*', '&')), ('operator_bitwise', ('&', '|', '^', '~', '<<', '>>'))

# KEYWORDS = ['int','float','char','if','else','while','for','return','void','break','continue','struct','typedef','const','static']

# SPECIAL = ['+', '-', '*', '/', '%', '=', '!', '<', '>', '&', '|', '^', '~','sizeof', '?', ':']
