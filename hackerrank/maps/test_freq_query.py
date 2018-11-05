from collections import defaultdict

INSERT  = 1
DELETE = 2
CHECK = 3

def update_freqs(prev_freq, freq_to_num, new_freq, num_to_freq, number):
    if prev_freq:
        freq_to_num[prev_freq] -= 1 #extract from num to freq
    new_freq = max(new_freq, 0)
    num_to_freq[number] = new_freq
    if new_freq:
        freq_to_num[new_freq] += 1


def freqQuery(queries):
    res = []
    freq_to_num = defaultdict(int)
    num_to_freq = defaultdict(int)
    for op, number in queries:
        if op == CHECK:
            res.append(1 if freq_to_num[number] > 0 else 0)
            continue
        if op == INSERT:
            prev_freq = num_to_freq[number]
            new_freq = prev_freq + 1
            update_freqs(prev_freq, freq_to_num, new_freq, num_to_freq, number)
            continue
        if op == DELETE:
            prev_freq = num_to_freq[number]
            new_freq = prev_freq - 1            
            update_freqs(prev_freq, freq_to_num, new_freq, num_to_freq, number)
            
    return res


def test_remove_than_add():
    res = freqQuery([
        (2, 2),
        (1, 2),
        (3, 1)
    ])
    assert 1 == res[0]

def test_remove():
    res = freqQuery([
        (1, 2),
        (2, 2),
        (3, 1)
    ])
    assert 0 == res[0]


def test_insert_two():
    res = freqQuery([
        (1, 2),
        (1, 2),
        (3, 2),
        (1, 3),
        (3, 1)
    ])
    assert 1 == res[0]
    assert 1 == res[1]


def test_single_check():
    res = freqQuery([
        (3, 2)
    ])
    assert 1 == len(res)
    assert 0 == res[0]

def test_empty():
    assert 0 == len(freqQuery([
        (1, 3)
    ]))
