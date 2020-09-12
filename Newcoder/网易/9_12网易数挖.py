### 缺点：暴露了对时间掌握的不好，后面留下给问答题的时间太少了。。。20分来不及做了。
### 这是自己对考试时间分配的失误，而不是技术性原因。应该值得好好反思，好好总结，下午再犯！！！牢记!





#####计算有多少个樱桃，二叉树树桩结构。
#这题全部AC, 而且效率还不错。值得鼓舞

m, n = list(map(int, input().strip().split(' ')))
lines1, lines2, lines3 = [], [], []
for _ in range(n):
    s = input()
    if s != '':
        first, second, third = list(map(str, s.strip().split(' ')))
        lines1.append(first)
        lines2.append(second)
        lines3.append(third)

def helper(n, lines1, lines2, lines3):
    cnt = 0
    for i in range(n-1):
        if lines1[i] == lines1[i+1]:
            if lines2[i] == 'left' and lines2[i+1] == 'right':
                if (lines3[i] not in lines1) and (lines3[i+1] not in lines1):
                    cnt += 1
                    i += 1
    return cnt

print(helper(n, lines1, lines2, lines3))



#########这题只通过了10%的测试案例；还有些边界条件没有考虑周全。。害
##题目是要求，包含a, b, c, x, y, z字符个数为偶数个的最长的字符串长度是多少？

s = input()
lines = list(s)
dic = {'a': 0, 'b': 0, 'c': 0, 'x': 0, 'y': 0, 'z': 0}
for i in lines:
    if i not in ('a', 'b', 'c', 'x', 'y', 'z'):
        continue
    else:
        dic[i] = dic.get(i, 0) + 1

print(dic)

def helper(dic):
    first, last = 0, 0
    max_key, max_val = '#', 0
    for t in sorted(dic.items(), key=lambda x: x[1], reverse=True):
        if t[1] % 2 == 0:
            max_key, max_val = t
           # print(max_key, max_val)
            break
    for i in range(len(s)):
        if s[i] == max_key:
            first = i
            break
    for j in range(len(s)-1, -1, -1):
        if s[j] == max_key:
            last = j
            break
    return last - first + 1

print(helper(dic))



#########这题是求回文子串的个数
###我按照中心点拓展的方式计算，算出的回文子串的个数偏多了。。时间来不及，所以没有调试代码，AC了


s = input()

def helper(s):
    res = 0
    if s != '':
        for center in range(2*len(s)-1):
            left = center // 2
            right = left + center % 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left -= 1
                right += 1
    return res

print(helper(s))





