"""
    Words are joined if the last letter of one word 
    and the first letter of another word are the same.

    Required:
        list - array of words

    Examples:
        arr = ["make", "eat", "tame"]
        word_chain(arr) => ["make", "eat", "tame"]
        is_word_chain(arr) => True

        arr = ["make", "eat", "tame", "buy"]
        word_chain(arr) => ["make", "eat", "tame"]
        is_word_chain(arr) => False
"""

from itertools import permutations 


"""
:brief:                     Longest Chain Word Formed
:param arr:                 list - the list of word to chain
:param current_chain:       list - the list of word as placeholder
:return:                    list - the list of word formed
"""
def word_chain(arr, current_chain=[]):
    res_chain = list(current_chain)
    test_chain = []

    for s in arr:
        temp_words_array = list(arr)
        temp_words_array.remove(s)

        if len(current_chain) == 0:
            test_chain = word_chain(temp_words_array, current_chain + [s])
        else:
            if s[0] == current_chain[-1][-1]:
                test_chain = word_chain(temp_words_array, current_chain + [s])

        if len(test_chain) > len(res_chain):
            res_chain = list(test_chain)
    return res_chain

"""
:brief:         Check whether Chain Word possible
:param arr:     list - the list of word to chain
:return:        bool - all the listed word can be chained
"""
def is_word_chain(arr):
    return any(all(a[-1] == b[0] for a, b in zip(seq, seq[1:])) for seq in permutations(arr))

if __name__ == "__main__":
    print(__doc__, "\n")
    print("Testing for " + __file__)

    TESTCASE = (
        (["make", "eat", "tame"], ["make", "eat", "tame"], True),
        (["make", "eat", "tame", "buy"], ["make", "eat", "tame"], False),
    )

    for test, result, bool_result in TESTCASE:
        print(test, result, word_chain(test)==result, is_word_chain(test)==bool_result)