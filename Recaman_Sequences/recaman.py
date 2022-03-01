"""
In mathematics and computer science,
The Recamán's sequence (or Recaman's sequence)
Is a well known sequence defined by a recurrence relation,
Because its elements are related to the previous elements in a straightforward way,
They are often defined using recursion. 

Recamán's sequence (or Recaman's sequence): 
    recaman(0) = 0; 
    for n > 0, 
        if nonnegative and not already in the sequence, 
            recaman(n) = recaman(n-1) - n 
        otherwise 
            recaman(n) = recaman(n-1) + n. 

REFERENCE: https://oeis.org/A005132
"""


"""
:brief:     Recamán's sequence (or Recaman's sequence)
:param n:   int - the nth term
:return:    int - the nth term of Recamán's sequence (or Recaman's sequence)
"""
def recaman(n):
    ref, res = {0}, 0
    for i in range(1,n+1):
        res += -i if res-i>0 and res-i not in ref else i
        ref.add(res)
    return res

if __name__ == "__main__":
    print(__doc__)
    print("\n")

    TESTCASE = (
        0, 1, 3, 6, 2, 7, 13, 20, 12, 21, 
        11, 22, 10, 23, 9, 24, 8, 25, 43, 
        62, 42, 63, 41, 18, 42, 17, 43, 16, 
        44, 15, 45, 14, 46, 79, 113, 78, 114, 
        77, 39, 78, 38, 79, 37, 80, 36, 81, 
        35, 82, 34, 83, 33, 84, 32, 85, 31, 
        86, 30, 87, 29, 88, 28, 89, 27, 90, 
        26, 91, 157, 224, 156, 225, 155
    )

    print("Recaman Sequences:") 
    print('='*124)

    for row in range(7):
        for v in range(1,11):
            idx = row*10+v
            res = recaman(idx)
            print(f"|{idx:<2}. {TESTCASE[idx]:>3} == {res:>3} => {TESTCASE[idx]==res}|", end=" ")
            if not v%5:print()
    
    print('='*124)
    print("\n")