###岛屿连接题
###大致题意，n个岛屿, m条桥梁(m行输入)， k是每个桥梁的成本上限。T是测试数据的组数，答案要返回输出是否能够全部连接n个桥梁，返回yes or no
##有些桥梁之间没法连接。返回No的情况有二，一是成本超出上限，二是连接岛屿的桥梁数不够。

T = int(input())

for _ in range(T):
    n, m, k = list(map(int, input().strip().split(' ')))
    lines1, lines2, lines3, memo = [], [], [], set()
    for i in range(m):
        s = input() #################################################卡死在这，在这个地方脑壳短路，不知道s= input()应该放到for循环下！！！！，吸取教训，下勿要再犯！！！！！
        if s != '':
            first, second, third = list(map(str, s.strip().split(' ')))
            lines1.append(first)
            lines2.append(second)
            lines3.append(third)
    print(lines1)
    print(lines2)
    print(lines3)
    for i in range(len(lines3)):
        if int(lines3[i]) > k:  # 这个算法整体思路是有的，但是这个地方总是还返回越界报错，还没有彻底调试正确，日后细究！！！
            lines1.pop(i)
            lines2.pop(i)
            lines3.pop(i)
    print(lines1)
    print(lines2)
    print(lines3)
    for i, j in zip(lines1, lines2):
        memo.add(i)
        memo.add(j)
    for i in range(1, n + 1):
        if str(i) not in memo:
             print('No')
    print('Yes')

