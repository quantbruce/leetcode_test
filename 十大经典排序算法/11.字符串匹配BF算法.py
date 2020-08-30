def Brute_Force(s, t):
    """
    :param s:  str
    :param t:  str
    :return:  int
    """
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 2
            j = 1
    if j >= len(t):
        return i - len(t)
    else:
        return 0

s = 'brucemichealjordan'
t = 'jordan'

print(Brute_Force(s, t))


