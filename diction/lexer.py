from ply.lex import lex

tokens = (
    'LBRACKET',
    'RBRACKET',
    'KEY',
)

t_LBRACKET = r'{'
t_RBRACKET = r'}'
t_KEY = r'\w+'

t_ignore = ' \t'

def t_ignore_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

lexer = lex()
