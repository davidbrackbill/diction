from ply.yacc import yacc
from diction.lexer import tokens

"""See `ply` documentation at https://github.com/dabeaz/ply/blob/master/doc/ply.md"""

def p_val(p):
    "val : LBRACKET pairs RBRACKET"
    p[0] = p[2]

def p_val_empty(p):
    "val : LBRACKET RBRACKET"
    p[0] = {}

def p_pairs(p):
    """
    pairs : pair
          | pair pairs
    """
    if len(p) > 2:
        p[0] = p[1] | p[2]
    else:
        p[0] = p[1]

def p_pair(p):
    "pair : KEY val"
    p[0] = {p[1]: p[2]}

def p_pair_solo(p):
    "pair : KEY"
    p[0] = {p[1]: {}}


def p_error(p):
    print(f"Syntax error: {p}")


parse = yacc().parse
