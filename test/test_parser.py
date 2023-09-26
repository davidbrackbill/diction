from diction.parser import parse


def test_fields():
    assert parse('{outer { inner }}') == {'outer': {'inner': {}}}


def test_field_width():
    assert parse('{outer { i1 i2 }}') == {'outer': {'i1': {}, 'i2': {}}}


def test_field_width2():
    assert parse('{outer { i1 i2 { j1 }}}') == {'outer': {'i1': {}, 'i2': {'j1': {}}}}

def test_field_width3():
    assert parse('{outer outer2 { i1 i2 { j1 }}}') == {'outer': {}, 'outer2': {'i1': {}, 'i2': {'j1': {}}}}

