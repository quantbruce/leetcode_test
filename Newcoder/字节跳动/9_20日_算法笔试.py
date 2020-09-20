####四道编程题

### 第一题回忆：
## 题目是要求输出字符串最小的循环单元，例如输入abababa, 则输出ab。如果不是个循环字符串，则就输出原字符串。

s = input().strip()

def helper(s):   # 我觉得整个大致思路是OK的，case通过最高却只有54.0%, 日后再细究吧。
    i, j = 0, 1
    while s[i] != s[j]:
        j += 1
    t = j - i
    if len(s) % t != 0:
        return s
    j += t
    i += t
    while j <= len(s):
        if s[i:j] != s[:t]:
            return s
        j += t
        i += t
    return s[:t]

print(helper(s))   


### 第二题回忆：
## 要我们构建一个简单计算器，只需要定义+ - * ^ 计算即可，

def helper(a, b, op):   # 由于不能在本地IDE调试代码，导致我很多分类的情况都没有考虑到，虽然很容易，但是代码case通过为0....
    mo = 1000000007
    if op == '+':
        if a + b < 0:
            return a + b
        else:
            return (a + b) % mo
    elif op == '-':
        if a - b < 0:
            return a - b
        else:
            return (a-b) % mo
    elif op == '*':
        if a * b >= 0:
            return ((a % mo) * (b % mo)) % mo
        else:
            return - (((abs(a) % mo) * (abs(b) % mo)) % mo)
    elif op == '^':
        if b == 0:
            return 1
        elif b > 0:
            return (a**b) % mo
        else:
            return -(a**(abs(b)))

T = int(input())
for _ in range(T):
    s = input()
    if s != '':
        tmp = s.strip().split(' ')[:3]
    # print(tmp)
        print(helper(int(tmp[0]), int(tmp[1]), tmp[2]))

print(helper(-1, -2, '+'))
# print(helper(1, 2, '+'))
# print(helper(1, 3, '-'))
# print(helper(10, -3, '*'))
# print(helper(2, -3, '^'))
# print(helper(1, 2, '+'))






