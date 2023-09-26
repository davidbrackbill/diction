from diction.lexer import lexer

def lex(q):
    lexer.input(q)
    return str(list(lexer))


def test_fields():
    assert lex('{outer { inner }}') == (
        "[LexToken(LBRACKET,'{',1,0), "
        "LexToken(KEY,'outer',1,1), "
        "LexToken(LBRACKET,'{',1,7), "
        "LexToken(KEY,'inner',1,9), "
        "LexToken(RBRACKET,'}',1,15), "
        "LexToken(RBRACKET,'}',1,16)]"
    )


def test_field_width():
    assert lex('{outer { i1 i2 }}') == (
        "[LexToken(LBRACKET,'{',1,0), "
        "LexToken(KEY,'outer',1,1), "
        "LexToken(LBRACKET,'{',1,7), "
        "LexToken(KEY,'i1',1,9), "
        "LexToken(KEY,'i2',1,12), "
        "LexToken(RBRACKET,'}',1,15), "
        "LexToken(RBRACKET,'}',1,16)]"
    )
