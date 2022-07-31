"""
Goldbach's conjecture is one of the oldest and best-known 
unsolved problems in number theory and all of mathematics. 
It states that every even natural number greater than 2 
is the sum of two prime numbers. 

Goldbach's conjecture: 
    if n%2, 
        return [] 
    otherwise, 
        [prime_min, prime_max]; # prime_min + prime_max = n
"""


"""
:brief:     check the number is a prime
:param n:   int  - the nth term
:return:    bool - a number is a prime
"""
def isprime(n):
    return not any(not n%v for v in range(2,int(n**0.5)+1)) and n>1

"""
:brief:     check the number is a Goldbach's conjecture
:param n:   int  - the nth term
:return:    list - a pair number of a Goldbach's conjecture
"""

def check_goldbach(n):
    if n%2: return []
    for v in range(n):
        if isprime(v) and isprime(n-v):
            return [v, n-v]
    return []

if __name__ == "__main__":
    print(__doc__)
    print("\n")

    TESTCASE = (
        [],[],[],[],[2, 2],
        [],[3, 3],[],[3, 5],[],[3, 7],
        [],[5, 7],[],[3, 11],[],[3, 13],
        [],[5, 13],[],[3, 17],[],[3, 19],
        [],[5, 19],[],[3, 23],[],[5, 23],
        [],[7, 23],[],[3, 29],[],[3, 31],
        [],[5, 31],[],[7, 31],[],[3, 37],
        [],[5, 37],[],[3, 41],[],[3, 43],
        [],[5, 43],[],[3, 47],[],[5, 47],
        [],[7, 47],[],[3, 53],[],[5, 53],
        [],[7, 53],[],[3, 59],[],[3, 61],
        [],[5, 61],[],[7, 61],[],[3, 67],
        [],[5, 67],[],[3, 71],[],[3, 73],
        [],[5, 73],[],[7, 73],[],[3, 79],
        [],[5, 79],[],[3, 83],[],[5, 83],
        [],[7, 83],[],[3, 89],[],[5, 89],
        [],[7, 89],[],[19, 79],[],[3, 97]
    )

    print("Goldbach's conjecture:") 
    print('='*124)
    print("All testcase are passed: ", all(check_goldbach(v)==TESTCASE[v] for v in range(101)))
    print('='*124)
    print("\n")