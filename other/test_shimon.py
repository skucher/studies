def kill(arr):
    while len(arr) > 1:
        print(len(arr))
        print(arr)        
        i = 0
        size = len(arr)
        while i <= size:
            arr[(i+1) % size] = None
            i+=2
        arr = [e for e in arr if e is not None]
    return arr[0]


def test_simple():
    assert 73 == kill(list(range(1, 101)))