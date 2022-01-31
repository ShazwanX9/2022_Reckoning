# Hofstadter Female and Male sequences

___
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
___

    Required:
        :param n:   -> int  - the nth term
        :return:    -> int  - the nth term of Hofstadter pair

    Example:
        female_recurrences(20)
            => 13
        male_recurrences(20)
            => 12

## DISCLAIMER!
    no guarantee of completeness, accuracy, timeliness or 
    of the results obtained from the use of this information

### For more information:
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Hofstadter_sequence)
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Recurrence_relation)