# Introduction

Diction lets you traverse Python dictionaries using GraphQL:

```python
from diction import graphql

nested_dict = {"key": {"key": "value", 
                       "bool": False, 
                       "num": 1
                       }, 
               "key2": "ignore"
               }

graphql(nested_dict, '{key}')
# {"key": {"key": "value", 
#          "bool": False, 
#          "num": 1}}

graphql(nested_dict, '{key {key}}')
# {"key": {"key": "value"}}
```

# GraphQL Roadmap

Currently, only fields are implemented, but I plan to add the following:
- Arguments
- Aliases
- Fragments
- Variables
- Inline fragments

Take a look at the [GraphQL queries page](https://graphql.org/learn/queries/) for more information on these features.

I will not be implementing the following:
- Operation names
- Mutations
- Directives

