##李克的想法(递归思路)

def f(n, i):  # n是第n个骰子，i是骰子点数和
    if n == 1:
        if 1 <= i <= 6:
            return 1 / 6
        return 0
    else:
        return (f(n-1, i-1) + f(n-1, i-2) + f(n-1, i-3) + f(n-1, i-4) + f(n-1, i-5) + f(n-1,  i-6)) / 6

def g(n):
    ls = []
    for i in range(n, 6 * n + 1):  # 第n颗骰子的点数和范围必然落在(n, 6 * n + 1)
        ls.append(round(f(n, i), 5))
    return ls

print(g(4))


