
import pytest
import math
from collections import defaultdict

def countTriplets_my(arr, r):
    if r == 1:
        num_1 = len([a for a in arr if a == 1])
        return int((math.factorial(num_1) / (math.factorial(num_1 - 3))))

    num_to_indices = {}
    relevant = []
    for index, e in enumerate(arr):
        e = round(log(e, r), 10)
        if not e.is_integer():
            continue
        int_e = int(e)
        relevant.append((index, int_e))
        num_to_indices.setdefault(int_e, []).append(index)

    num_tripples = 0
    for index, e in relevant:
        e_1_indices = num_to_indices.get(e + 1)
        e_2_indices = num_to_indices.get(e + 2)
        if not e_1_indices or not e_2_indices:
            continue
        for e1_index in (i for i in e_1_indices if i > index):
            num_tripples += len([i for i in e_2_indices if i > e1_index])
    return num_tripples


def countTriplets(arr, r):
    i_wait_for_second = defaultdict(int)
    i_wait_for_third = defaultdict(int)
    count = 0
    for e in arr:
        count += i_wait_for_third[e]
        i_wait_for_third[e * r] += i_wait_for_second[e]
        i_wait_for_second[e * r] += 1
    return count

def test_simple():
    assert 1 == countTriplets([1, 2, 4], 2)


def test_two():
    assert 2 == countTriplets([1, 2, 4, 8], 2)


def test_site():
    assert 6 == countTriplets([1, 3, 9, 9, 27, 81], 3)
    assert 4 == countTriplets([1, 5, 5, 25, 125], 5)


def test_unordered():
    assert 0 == countTriplets([1, 9, 3], 3)
    assert 0 == countTriplets([9, 1, 3], 3)
    assert 3 == countTriplets([5, 1, 5, 25, 125], 5)


def test_big():
    s = None
    import os 
    dir_path = os.path.dirname(os.path.realpath(__file__))
    with open(os.path.join(dir_path,'t11.txt'), 'r') as f:
        s = f.read()
    l = [int(e.strip()) for e in s.split(' ')]
    assert 1667018988625 == countTriplets(l, 1)