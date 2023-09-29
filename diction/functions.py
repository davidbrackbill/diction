"""
Things to possibly conform to:
JSON Spec https://www.rfc-editor.org/rfc/rfc7159.txt
GraphQL Spec https://spec.graphql.org/October2021/
GraphQL query explanations: https://graphql.org/learn/queries/

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

JSONLike = dict | list
json_types = {dict, list}
JSONMaybe = JSONLike | None


def graphql(data: JSONLike, query: str) -> JSONMaybe:
    data_type = type(data)
    if data_type not in json_types:
        raise TypeError(f'Type `{type(data)}` is not in the parseable types (dict, list)')

    commands = parse(query)
    if not commands:
        # Empty query:
        #  return full container
        if type(commands) == data_type:
            return data

        # Bad query:
        #  return empty container
        return data_type()

    # Good query
    return dict(traverse(data, commands))

def traverse(d: dict, cmd: dict):
    for key, next_cmd in cmd.items():
        if not next_cmd:
            yield key, d[key]
        else:
            yield key, dict(traverse(d[key], next_cmd))