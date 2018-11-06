import bisect

def activityNotifications(expenditure, d):
    '''
    expenditure: list of expences
    d: median window
    returns: number of notifications of 2xmedian
    '''
    window = expenditure[:d]
    for expence in range(d, len(expenditure)):
        #get median
        #if median < expence /2
        bisect.insort(window, expence)
    pass

def test_empty():
    assert 0 == activityNotifications([],0)


