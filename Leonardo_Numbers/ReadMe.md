# The Leonardo numbers

___
    A sequence of numbers given by the recurrence

    Definition:
        L(0) = 1 || 0
        L(1) = 1 || 0
        L(x) = L(x - 1) + L(x - 2) + 1

    Generalization:
        L(x) = L(x - 1) + L(x - 2) + a
___

    Required:
        :param n:   int range of number sequence
        :L0:        int leonardo starting number
        :L1:        int leonardo second number
        :return:    A list of leonardo numbers

    Example:
        leonardo_numbers(10, 3, 7, 4) => [ 3, 7, 14, 25, 43, 72, 119, 195, 318, 517 ]

## DISCLAIMER!
    no guarantee of completeness, accuracy, timeliness or 
    of the results obtained from the use of this information

### For more information:
	Visit [Wikipedia](https://en.wikipedia.org/wiki/Leonardo_number)