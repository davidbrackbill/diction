import pytest
from diction.query import diction

simple_dict = {"key": "value", "bool": False, "num": 1}

simple_list = [1, 2, 3]

nested_dict = {"key": simple_dict, "key2": simple_list}

nested_list = [[nested_dict], {"key": nested_dict}]


# Fetching

def test_invalid_type():
    for invalid in ['', False, 1, object()]:
        with pytest.raises(TypeError):
            diction(invalid, '')


def test_null_query():
    assert diction(simple_dict, '') == {}
    assert diction(simple_list, '') == []


def test_invalid_query():
    assert diction(simple_dict, 'bad graphQL') == {}


def test_empty_dict():
    assert diction(simple_dict, '{}') == simple_dict


def test_dict():
    assert diction(simple_dict, '{key}') == {"key": "value"}
    assert diction(simple_dict, '{bool}') == {"bool": False}
    assert diction(simple_dict, '{num}') == {"num": 1}


def test_nested_dict():
    assert diction(nested_dict, '{}') == nested_dict
    assert diction(nested_dict, '{key}') == {"key": simple_dict}
    assert diction(nested_dict, '{key {key}}') == {"key": {"key": "value"}}
    assert diction(nested_dict, '{key {bool}}') == {"key": {"bool": False}}


# GraphQL doesn't use index search, but this test can be used for
#  a custom query / xpath / css selector function.
#  For more query ideas, ask ChatGPT: "what other query languages are like xpath and css selectors?"

def test_empty_list():
    assert diction(simple_list, '[]') == simple_list

def test_nested_list():
    assert diction(nested_list, '[]') == nested_list
    assert diction(nested_list, '[0]') == [nested_dict]  # Not sure if index search should be allowed
    assert diction(nested_list, '[0 [0]]') == nested_dict  # Not sure if index search should be allowed
    assert diction(nested_list, '[0 [0 {key}]]') == simple_dict  # Not sure if index search should be allowed

    assert diction(nested_list, '[{key}]') == {"key": nested_dict}

