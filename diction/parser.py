from ply.yacc import yacc
from diction.lexer import tokens

# Transformations:

# Simple nested
"""
    {1 { 2 { 3}}
    stub stub stub }}}
    stub stub search}}
    stub search }
    search
"""

# Multiple fields
"""
    {1 { 2a 2b}}
    stub stub}}
    stub search}
    search
"""

# Multiple nested fields
"""
    {1 { 2a 2b {3a} }}
    stub stub keys }}
    stub search}
    search
"""

"""
    Want Python representation of
    { a b { c}}
    -->
    {a: {}, b: {c: {}}
     ^   ^
    key val
    
    -- Rules
    
    key: KEY
    
    val: LBRACKET KEY RBRACKET
    
    pair: key val
        | key
        
    pairs: pair 
         | pair pairs
         
    object: LBRACKET pairs RBRACKET
    
    { a b { c}}
    { key key val}
    { pair pair }
    object
    
"""



def p_search_stub(p):
    "search : stub RBRACKET"
    p[0] = [p[1]]

def p_search_recurs(p):
    "search : stub search RBRACKET"
    p[0] = p[1] + p[2]

def p_search_base(p):
    "search : LBRACKET keys RBRACKET"
    p[0] = [p[2]]

def p_stub(p):
    "stub : LBRACKET keys"
    p[0] = [p[2]]

def p_keys(p):
    """keys : KEY
           | KEY keys"""
    p[0] = [p[1]] if len(p) == 2 else [p[1], *p[2]]


def p_error(p):
    print(f"Syntax error: {p}")

parse = yacc().parse
