import bisect
import math


def activityNotifications(expenditure, d) -> int:
    '''
    expenditure: list of expences
    d: median window
    returns: number of notifications of 2xmedian
    '''    
    get_median = create_get_median_func(d)
    sorted_window = sorted(expenditure[:d])
    result = 0
    for i in range(d, len(expenditure)):
        expence = expenditure[i]
        median = get_median(sorted_window)
        if expence >= 2 * median:
            result += 1
        sorted_window.pop(bisect.bisect_left(sorted_window, expenditure[i-d]))
        bisect.insort(sorted_window, expence)
    return result

def create_get_median_func(d):
    median_index = float(d) / 2.0
    if not median_index.is_integer(): # odd case
        median_index = int(math.floor(median_index))
        get_median = lambda array: array[median_index]
    else:
        int_median = int(median_index)
        below = int_median - 1
        above  = int_median
        get_median = lambda array: float(array[below]  + array[above]) / 2.0
    return get_median


from pathlib import Path

def test_2_submission():
    string = Path(r'./hackerrank/sort/fraud.test1.txt').read_text().splitlines()[0]
    arr = [int(e) for e in string.split(' ')]
    assert 633 == activityNotifications(arr, 10000)

def test_2_even_site():
    arr = [int(e) for e in "1 2 3 4 4".split(' ')]
    assert 0 == activityNotifications(arr, 4)

def test_1_odd_site():
    arr = [int(e) for e in "2 3 4 2 3 6 8 4 5".split(' ')]
    assert 2 == activityNotifications(arr, 5)

def test_odd():
    assert 1 == activityNotifications([1,1,1,2], 3)

def test_even_compex():
    assert 1 == activityNotifications([2,2,1,3,4], 4)

def test_even():
    assert 1 == activityNotifications([1,1,2], 2)

def test_empty():
    assert 0 == activityNotifications([],0)