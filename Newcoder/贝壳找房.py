###字符串的匹配，考察任意一段乐谱中，几种基础乐符出现的次数。
##这题是直接Acc的，速度效率还比较高，看到自己的进步，欣慰！再接再厉！！

s = '165432313236'
s = '1654323132366323132253235323132363231323'
t = ['43231323', '53231323', '63231323'] # 几种基础音符，

def helper(s, t):
    cnt, i = 0, 0
    while i < len(s):
        if s[i] not in ('4', '5', '6'):
            i += 1
            continue
        if s[i] == '4':
            if s[i:i+8] == t[0]:
                cnt += 1
                i += 8
            else:
                i += 1
        elif s[i] == '5':
            if s[i:i+8] == t[1]:
                cnt += 1
                i += 8
            else:
                i += 1
        elif s[i] == '6':
            if s[i:i+8] == t[2]:
                cnt += 1
                i += 8
            else:
                i += 1
    return cnt

T = int(input())
for _ in range(T):
    s = input()
    if s != '':
        print(helper(s, t))
    else:
        continue
