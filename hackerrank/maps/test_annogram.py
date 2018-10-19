import pytest

def annogram(s):
    subs = set()
    count = 0
    for start in range(len(s)+1):
        for end in range(start+1,len(s)+1):
            curr_s = ''.join(sorted(s[start:end]))
            print(curr_s)
            if curr_s in subs:
                count += 1
            else:
                subs.add(curr_s)
    return count

    

def test_simple():
    res = annogram('abba')
    assert 4 == res

def test_fail():
    res = annogram('cdcd')
    assert 5 == res