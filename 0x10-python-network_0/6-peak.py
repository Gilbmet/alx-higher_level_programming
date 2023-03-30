#!/usr/bin/python3

def find_peak(list_of_integers):
    """
    Finds a peak in a list of unsorted integers using binary search.
    """
    n = len(list_of_integers)
    if n == 0:
        return None
    if n == 1:
        return list_of_integers[0]
    if n == 2:
        return max(list_of_integers)
    left = 0
    right = n - 1
    while left <= right:
        mid = (left + right) // 2
        if (mid == 0 or list_of_integers[mid - 1] <= list_of_integers[mid]) and \
                (mid == n - 1 or list_of_integers[mid + 1] <= list_of_integers[mid]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            right = mid - 1
        else:
            left = mid + 1
