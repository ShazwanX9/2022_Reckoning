"""
    Maximal number of regions obtained
    by joining n points around a circle
    by straight lines.

    Also number of regions in 4-space
    formed by n-1 hyperplanes.

First six points:
    1 -> 1
    2 -> 2
    3 -> 4
    4 -> 8
    5 -> 16
    6 -> 31
    .... ...
"""

"""
:brief:     get maximal number of regions obtained
:param n:   int - number of points around a circle
:return:    int - result in value
"""
def region_in_circle(n):
    return n*(n*(n*(n-6)+23)-18)//24+1

"""
:brief:     get maximal number of regions obtained
:param n:   int - number of points around a circle
:return:    int - result in value
"""
def region_in_circle_ii(n):
    return n*~-n*(n*n-5*n+18)//24+1

if __name__ == "__main__":
    print(__doc__)
    print("\n")

    from random import randrange

    print("Maximal number of regions obtained:") 
    print('='*124)

    for i in range(20):
        test = int(randrange(124))
        print(f"\tTest for number: {test}")
        i, ii = region_in_circle(test), region_in_circle_ii(test)
        print("\t", i, ii, i==ii)
        print()

    print('='*124)
    print("\n")