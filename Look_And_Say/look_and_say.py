"""
:brief: describe the previous term start from data
:param data: string number to start look and say
:param maxlen: int number to repeating look and say
:return:    A list of look and say sequence
"""
def look_and_say(data='1', maxlen=5):
    res = [data]
    for _ in range(maxlen):
        ref, chk, cnt = "", res[-1][0], 0
        for c in res[-1]:
            if c!=chk:ref, chk, cnt = ref+f"{cnt}{chk}", c, 0
            cnt += 1
        res.append(ref+f"{cnt}{chk}")
    return res[1:]