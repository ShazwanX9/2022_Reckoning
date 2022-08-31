"""
Bijective numeration is any numeral system 
in which every non-negative integer can be 
represented in exactly one way using a 
finite string of digits.

First six Bijective:
    0 -> ''
    1 -> '1'
    2 -> '2'
    3 -> '11'
    4 -> '12'
    5 -> '21'
    6 -> '22'
    .... ...
"""

"""
:brief:     convert bijective to n
:param n:   str - bijective to convert
:return:    int - result in value
"""
def bijective_to_int (bijective : str) -> int:
    return sum(int(v)*(2**i)for i,v in enumerate(bijective[::-1]))

"""
:brief:     convert n to bijective
:param n:   int - value to convert
:return:    str - result in bijective
"""
def int_to_bijective (n : int) -> str:
    return bin(n+1)[3:].replace('1', '2').replace('0', '1')

if __name__ == "__main__":
    print(__doc__)
    print("\n")

    TESTCASE = [
        {'n':0,'b':''},
        {'n':1,'b':'1'},
        {'n':3,'b':'11'},
        {'n':7,'b':'111'},
        {'n':14,'b':'222'},
        {'n':1000000,'b':'2221211112112111112'}
    ]

    print("Bijective Binary:") 
    print('='*124)

    print("Check conversion back to original:", all(bijective_to_int(int_to_bijective(v))==v for v in range(101)))
    print("Check on several testcase [bijective to int]:", all(bijective_to_int(test['b'])==test['n'] for test in TESTCASE))
    print("Check on several testcase [int to bijective]:", all(int_to_bijective(test['n'])==test['b'] for test in TESTCASE))

    print('='*124)
    print("\n")