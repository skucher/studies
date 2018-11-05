
import pytest
from collections import defaultdict

def checkMagazine(magazine, note):
    d_magazine = defaultdict(int)
    for w in magazine:
        d_magazine[w] += 1
    
    for w in note:
        if d_magazine[w] == 0:
            return 'No'
        d_magazine[w] -= 1
    return 'Yes'

def test_simple():
    magazine = 'two times three is not four'.split(' ')
    note = 'two times two is four'.split(' ')
    assert 'No' == checkMagazine(magazine, note)