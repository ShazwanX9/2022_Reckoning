"""
:brief:     The Leonardo numbers are a sequence of numbers given by the recurrence
:param n:   int range of number sequence
:param L0:  int leonardo starting number
:param L1:  int leonardo second number
:return:    A list of leonardo numbers
"""
def leonardo_numbers(n, L0, L1, add) :
    res = [L0, L1]
    [res.append(res[-1]+res[-2]+add) for i in range(n-2)]
    return res

if __name__ == "__main__":
    print(__doc__)
    print("Testing for " + __file__)

    print(
    """
        input : 
            n = 10 , 
            L0 = 3 , 
            L1 = 7 , 
            add = 4 

        output : 
            [ 3, 7, 14, 25, 43, 72, 119, 195, 318, 517 ]
    """
    )
    print("\tResult:", leonardo_numbers(10, 3, 7, 4))