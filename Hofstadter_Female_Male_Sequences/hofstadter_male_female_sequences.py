"""
Mutual recursion is a variation recursion.
    ```
    Two functions are called mutually recursive
    if the first function makes a recursive call
    to the second function and the second function,
    in turn, calls the first one.
    ```
This concept is used in circular dependency
which is a relation between two or more modules
which either directly or indirectly
depend on each other to function properly.

In mathematics, a Hofstadter sequence is a 
member of a family of related integer sequences 
defined by non-linear recurrence relations.

The Hofstadter Female (F) and Male (M) sequences 
are defined as follows:
    ```
    F(0) = 1; M(0) = 1;
    F(n) = n-M(F(n-1)), n>0;
    M(n) = n-F(M(n-1)), n>0;
    ```

The first few terms of these sequences are
    F: 1, 1, 2, 2, 3, 3, 4, 5, 5, 6, 6, 7, 8, 8, 9, 9, 10, 11, 11, 12, 13, ... (sequence A005378 in the OEIS)
    M: 0, 0, 1, 2, 2, 3, 4, 4, 5, 6, 6, 7, 7, 8, 9, 9, 10, 11, 11, 12, 12, ... (sequence A005379 in the OEIS)
```
"""

"""
:brief:         The Hofstadter female of recurrences
:see:           [A005378](https://oeis.org/A005378)
:param n:       int - the nth term
:return:        int - the nth term of Hofstadter female
:exceptsafe:    no-exception - return 1 if n<=0
"""
def female_recurrences(n:int)->int: return n-male_recurrences(female_recurrences(n-1)) if n>0 else 1

"""
:brief:         The Hofstadter male of recurrences
:see:           [A005379](https://oeis.org/A005379)
:param n:       int - the nth term
:return:        int - the nth term of Hofstadter male
:exceptsafe:    no-exception - return 1 if n<=0
"""
def male_recurrences(n:int)->int: return n-female_recurrences(male_recurrences(n-1)) if n>0 else 0


if __name__ == "__main__":
    print(__doc__)
    print("========================================")

    # Test from 0 - TEST_N Inclusive
    TEST_N = 20
    TEST_FN = lambda f: [print(f(v), end=", ") for v in range(TEST_N+1)]

    print("\nTest female_recurrences:", end=" ") 
    TEST_FN(female_recurrences)
    print()
    print("\nTest male_recurrences:", end="\t ")
    TEST_FN(male_recurrences)
    print()

    print("\n========================================")