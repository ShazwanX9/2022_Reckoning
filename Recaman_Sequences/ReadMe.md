# Recaman sequences

___
In mathematics and computer science,
The Recamán's sequence (or Recaman's sequence)
Is a well known sequence defined by a recurrence relation,
Because its elements are related to the previous elements in a straightforward way,
They are often defined using recursion. 

Recamán's sequence (or Recaman's sequence): 
    if nonnegative and not already in the sequence, 
        a(0) = 0; for n > 0, a(n) = a(n-1) - n 
    otherwise 
        a(n) = a(n-1) + n. 
___

    Required:
        :param n:   -> int  - the nth term
        :return:    -> int  - the nth term of Recamán's sequence (or Recaman's sequence)

    Example:
        recaman(37) => 37
        recaman(63) => 90

## DISCLAIMER!
    no guarantee of completeness, accuracy, timeliness or 
    of the results obtained from the use of this information

### For more information:
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Recam%C3%A1n%27s_sequence)