import pytest
from diction.functions import graphql, traverse

simple_dict = {"key": "value", "bool": False, "num": 1}

simple_list = [1, 2, 3]

nested_dict = {"key": simple_dict, "key2": simple_list}

nested_list = [[nested_dict], {"key": nested_dict}]


# Fetching

def test_invalid_type():
    for invalid in ['', False, 1, object()]:
        with pytest.raises(TypeError):
            graphql(invalid, '')


def test_null_query():
    assert graphql(simple_dict, '') == {}
    assert graphql(simple_list, '') == []


def test_invalid_query():
    assert graphql(simple_dict, 'bad graphQL') == {}


def test_empty_dict():
    assert graphql(simple_dict, '{}') == simple_dict


def test_dict():
    assert graphql(simple_dict, '{key}') == {"key": "value"}
    assert graphql(simple_dict, '{bool}') == {"bool": False}
    assert graphql(simple_dict, '{num}') == {"num": 1}


def test_nested_dict():
    assert graphql(nested_dict, '{}') == nested_dict
    assert graphql(nested_dict, '{key}') == {"key": simple_dict}
    assert graphql(nested_dict, '{key {key}}') == {"key": {"key": "value"}}
    assert graphql(nested_dict, '{key {bool}}') == {"key": {"bool": False}}


# GraphQL doesn't use index search, but this test can be used for
#  a custom query / xpath / css selector function.
#  For more query ideas, ask ChatGPT: "what other query languages are like xpath and css selectors?"

def test_empty_list():
    assert graphql(simple_list, '[]') == simple_list

def test_nested_list():
    assert graphql(nested_list, '[]') == nested_list
    assert graphql(nested_list, '[0]') == [nested_dict]  # Not sure if index search should be allowed
    assert graphql(nested_list, '[0 [0]]') == nested_dict  # Not sure if index search should be allowed
    assert graphql(nested_list, '[0 [0 {key}]]') == simple_dict  # Not sure if index search should be allowed

    assert graphql(nested_list, '[{key}]') == {"key": nested_dict}


# Internal function testing

def test_traverse():
    dct = {'a': {'b': 'c'}, 'd': 'e', 'f': 'g'}
    cmd = {'a': {'b': {}}, 'd': {}}
    out = {'a': {'b': 'c'}, 'd': 'e'}
    assert dict(traverse(dct, cmd)) == out
