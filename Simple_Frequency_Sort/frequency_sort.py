"""
    Sort Elements in an Array by
    Decreasing Frequency of elements.
    If two elements have the same frequency,
    Sort them by increasing value

    Required:
        list - array of number

    Examples:
        arr = [2,2,3,3,3,1,1]
        frequency_sort(arr) => [3,3,3,1,1,2,2]
"""

from collections import Counter
def frequency_sort(arr):
    return sum([[v]*f for v,f in sorted(Counter(arr).items(),key=lambda v:(-v[1],v[0]))],[])

if __name__ == "__main__":
    print(__doc__, "\n")
    print("Testing for " + __file__)

    TESTCASE = (
        ([2,2,3,3,3,1,1], [3,3,3,1,1,2,2]),
        ([2,1,3,3,3,1,1], [1,1,1,3,3,3,2]),
        ([2,2,2,3,3,1,1], [2,2,2,1,1,3,3]),
        ([2,2,4,3,3,1,1], [1,1,2,2,3,3,4]),
    )

    for test, result in TESTCASE:
        print(test, result, frequency_sort(test)==result)