def maximumToys(prices, k):
    sorted_prices = sorted(prices)
    toys_price = 0
    num_toys = 0
    for price in sorted_prices:
        with_this_toy = toys_price + price
        if with_this_toy > k:
            break
        toys_price = with_this_toy
        num_toys += 1
    return num_toys

def test_some_of_toys_sort():
    assert 2 == maximumToys([3, 2, 1], 3)

def test_some_of_toys():
    assert 2 == maximumToys([1, 2,3], 3)


def test_one_toy():
    assert 1 == maximumToys([1], 1)


def test_no_toys():
    assert 0 == maximumToys([1], 0)
