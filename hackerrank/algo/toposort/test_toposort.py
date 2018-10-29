import pytest
from functools import reduce as _reduce

def toposort(d_dependencies):
    '''
    @param d_dependencies: node -> set(nodes it depends on)
    @returns : [ node ], for each i res[i] idependant from n[j] for all j < i
    '''
    if len(d_dependencies) == 0:
        return

    for k,v in d_dependencies.items():
        v.discard(k)

    extra_items_in_deps = _reduce(set.union, d_dependencies.values()) - set(d_dependencies.keys())
    # Add empty dependences where needed.
    d_dependencies.update({item:set() for item in extra_items_in_deps})

    while True:
        independant = set(
            (k for k, v in d_dependencies.items() if len(v) == 0))
        if len(independant) == 0:
            break
        yield independant
        d_dependencies = {k: (v - independant) for k, v in d_dependencies.items() if k not in independant }
    if d_dependencies:
        raise Exception('circular')

def toposort_flat(d_dependencies):
    res = []
    sort_res = toposort(d_dependencies)
    for batch in sort_res:
        res.extend(sorted(batch))
    return res    

def test_mss():
    assert ['b', 'a'] == toposort_flat({'a': {'b'}})


def test_complex():
    assert ['d', 'f', 'n', 'b', 'e', 'm', 'c', 'a'] == toposort_flat(
        {'a': {'b', 'c'}, 'b': {'d'}, 'c': {'d', 'e'}, 'e': {'f'}, 'm': {'n'}})
