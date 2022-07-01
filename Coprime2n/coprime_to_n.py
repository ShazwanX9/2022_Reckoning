"""
In mathematics, two integers a and b are coprime, 
relatively prime or mutually prime if the only 
positive integer that is a divisor of both of them is 1.
"""

from math import gcd

"""
:brief:     list all the coprime of n
:param n:   int - the lookup value
:return:    int - the coprime list upto nth
"""
def coprimes(n:int):return [v for v in range(n) if gcd(n,v)==1]

if __name__ == "__main__":
    print(__doc__, "\n")
    print("Testing for " + __file__)

    first_ten = (
        [],
        [0],
        [1],
        [1, 2],
        [1, 3],
        [1, 2, 3, 4],
        [1, 5],
        [1, 2, 3, 4, 5, 6],
        [1, 3, 5, 7],
        [1, 2, 4, 5, 7, 8],
    )

    for i in range(10):
        assert coprimes(i)==first_ten[i], "Something's wrong, I can feel it"
    print("All 10 test is successfull")

    assert coprimes(100) == [
        1, 3, 7, 9, 11, 
        13, 17, 19, 21, 
        23, 27, 29, 31, 
        33, 37, 39, 41, 
        43, 47, 49, 51, 
        53, 57, 59, 61, 
        63, 67, 69, 71, 
        73, 77, 79, 81, 
        83, 87, 89, 91, 
        93, 97, 99
    ]
    print("Big Number Successfull")