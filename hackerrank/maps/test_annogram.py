import pytest
from math import factorial

def annogram(s):
    subs = {}
    for start in range(len(s)+1):
        for end in range(start+1,len(s)+1):
            curr_s = ''.join(sorted(s[start:end]))
            subs[curr_s] = subs.setdefault(curr_s, 0) + 1
    
    def pairs_of(count):
        if count < 2: return 0
        fact = factorial(count)
        return fact / (factorial(count - 2) * 2)


    counts = (pairs_of(v) for v in subs.values())
    return sum(counts)

    

def test_simple():
    assert 4 == annogram('abba')
    assert 10 == annogram('dddd')
    assert 5 == annogram('cdcd')