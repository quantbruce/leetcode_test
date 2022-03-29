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
            i = i - j + 2 # 看成是(i-j+1) + 1
            j = 1
    if j >= len(t):
        return i - len(t)
    else:
        return 0

s = 'brucemichealjordan'
t = 'jordan'

print(Brute_Force(s, t))

#时间复杂度：O((n-m)*m + m) 其中m是模式长度，n是主串长度. 当m<<n时候，O(n*m)
#空间复杂度：O(1)


#### 写成这样是等价的
def Brute_Force(s, t):
    i, j = 0, 0
    while i < len(s) and j < len(t):
        if s[i] == t[j]:
            i += 1
            j += 1
        else:
            i = i - j + 1
            j = 0

    if j >= len(t):
        return i - len(t)
    else:
        return 0
    
    
    
    
    
    
    
    
    
    
