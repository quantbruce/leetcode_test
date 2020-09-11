def KMP(s, p):
    nex = getNext(p)
    i = 0
    j = 0   # 分别是s和p的指针
    while i < len(s) and j < len(p):
        if j == -1 or s[i] == p[j]: # j==-1是由于j=next[j]产生
            i += 1
            j += 1
        else:
            j = nex[j] # 不用管nex[]里面是i还是j，反正都是下标，都是个数而已。nex[]里面指到哪个数，小蝌蚪找妈妈就找到哪个数。

    if j >= len(p): # j走到了末尾，说明匹配到了
        return i - len(p)
    else:
        return -1

def getNext(p):
    next = [0] * (len(p) + 1)
    next[0] = -1
    i = 0
    j = -1
    while i < len(p):  # i在这里还会自增
        if j == -1 or p[j] == p[i]:  # i相当于右指针, j相当于左指针,i>j
            i += 1
            j += 1
            next[i] = j  # j的下一个就是i,因为最开始设j=-1, i=0. i是要比j大1的  // 这样理解这行代码：在p中，下标为i的元素下一轮开始(next[])比较的下标就是j, (从j开始)
        else:
            j = next[j]  # next = [-1, 0, 0, 0......0, 0], 被赋值的next[j]都是0
    return next


# p = 'abcaabbcabcaabdab'
# print(getnext(p))

s = 'brucemichealjordan'
p = 'jordan'
print(KMP(s, p))


https://zhuanlan.zhihu.com/p/41047378
https://www.bilibili.com/video/BV1ht411R7hP
