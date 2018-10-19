import math

def index(s_list, element):
    first = 0
    last = len(s_list) - 1
    while first <= last:
        mid = (first + last) // 2
        mid_val = s_list[mid]
        if element == mid_val:
            return mid
        if element > s_list[mid]:
            first = mid + 1
            continue
        last = mid - 1
    return first