from functools import reduce
def flatten(d: dict):
    return reduce(lambda x, y: dict(**x, **y), d)