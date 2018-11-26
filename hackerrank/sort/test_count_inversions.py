def merge(a1, a2):
    swaps, i, j, result, m, n = 0, 0, 0, [], len(a1), len(a2)
    ra = result.append
    while i < m and j < n:
        if a1[i] <= a2[j]:
            ra(a1[i])
            i += 1
        else:
            ra(a2[j])
            j += 1
            swaps += m - i
    result += a1[i:]
    result += a2[j:]    
    return swaps, result
    
def msort(arr):
    n = len(arr)
    mid = n // 2
    if n > 1:
        left_swaps, left_result = msort(arr[:mid])
        right_swaps, right_result = msort(arr[mid:])
        m_swaps, result = merge(left_result, right_result)
        return m_swaps + left_swaps + right_swaps, result
    return 0, arr

def countInversions(arr):
    return msort(arr)[0]

'''
    def _count_rec(arr, start, end, tmp):
    if end <= start:
        return 0
    mid = int((start + end) / 2)
    left_inv =  _count_rec(arr, start, mid, tmp)
    right_inv =  _count_rec(arr, mid + 1, end, tmp)
    curr_inv = _merge(arr, start, end, tmp)
    return left_inv + right_inv + curr_inv


    def _merge(arr, start, end, tmp):
        if start >= end:
            return 0
        mid = (start + end) // 2
        left_p = start
        right_p = mid + 1
        invs = 0
        tmp_index = start
        while(left_p <= mid and right_p <= end):
            if(arr[left_p] <= arr[right_p]):           
                elem = arr[left_p]
                left_p += 1 
            else:       
                elem = arr[right_p]
                right_p += 1
                invs += (mid - left_p) + 1
            tmp[tmp_index] = elem
            tmp_index += 1

        while left_p <= mid:
            tmp[tmp_index] = arr[left_p]
            left_p += 1
            tmp_index += 1

        while right_p <= end:
            tmp[tmp_index] = arr[right_p]
            right_p += 1
            tmp_index += 1

        arr[start:end+1] = tmp[start:end+1]             

        return invs

    def countInversions(arr):
        tmp = [-1] * len(arr)
        return _count_rec(arr, 0, len(arr) - 1, tmp)
'''

def test_no_inv():
    assert 0 == countInversions([])
    assert 0 == countInversions([1,2,3])

def test_single_inv():
    assert 1 == countInversions([2,1,3])

def test_site1_inv():
    assert 4 == countInversions([2, 1, 3, 1, 2])


def test_site2_inv():
    assert 6 == countInversions([7, 5, 3, 1])