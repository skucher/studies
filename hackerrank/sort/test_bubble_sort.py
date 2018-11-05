def swap(arr, i):
    e_i = arr[i]
    e_i1 = arr[i+1]
    if e_i <= e_i1:
        return 0
    arr[i] = e_i1
    arr[i+1] = e_i
    return 1


def sort(a):
    n = len(a)
    res = 0
    for i in range(n):
        num = sum(swap(a, j) for j in range(n-i-1))
        if not num:
            break
        res += num
    return res


def countSwaps(a):
    swaps = sort(a)
    res = swaps, a[0], a[-1]
    print(res)
    return res

def test_three_swaps():
    assert (3, 1, 3) == countSwaps([ 3, 2, 1])

def test_one_swap():
    assert (1, 1, 3) == countSwaps([2, 1, 3])

def test_no_change():
    assert (0, 1, 3) == countSwaps([1, 3])
