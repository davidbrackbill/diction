"""
Things to possibly conform to:
JSON Spec https://www.rfc-editor.org/rfc/rfc7159.txt
GraphQL Spec https://spec.graphql.org/October2021/

Allows querying of nested dictionaries and lists using a DSL similar to GraphQL

See https://graphql.org/learn/queries/ for ways to use this library.

I plan to implement:
(1) Fields
(2) Arguments
(3) Aliases
---
Then will implement:
(4) Fragments
(6) Variables
(9) Inline fragments
---
Will not implement:
(5) Operation names
(8) Mutations
(7) Directives


Goals:
    To be a subset of valid GraphQL
    To be nearing the performance of an imperative approach using keys and indices,
     meaning 1-10x the computation speed.
"""

from typing import Dict, List, Any
from diction.parser import parse

JSONLike = Dict | List
JSONMaybe = JSONLike | Any


def diction(data: JSONLike, query: str) -> JSONMaybe:
    if not isinstance(data, JSONLike):
        raise TypeError(f'Type `{type(data)}` is not in the parseable types (dict, list)')

    layers = parse(query)
    if layers is None:
        # Return empty container
        return type(data)()

    body = data

    # body = {'i' : {'1': [{'3': '3'}, '4'], '2': '2'} }
    # layers = [['i'], ['1']]
    # for each element in outer_list, get object
    # for each object, subset using inner list

    {k: subset(layer) for layer in layers}
    for layer in layers:
        lyr = {k: layer[k] for k in ('l', 'm', 'n')}
        for key in layer:

            # Merge key access w/ another
            body = body[key]

    return body

def subset(d: dict, keys: [str]):
    return {k: d[k] for k in keys}

def merge()
