###求矩阵相乘
###一开始没想出来，考完再进一步完善的

m, k, n = list(map(int, input().strip().split(' ')))
A = [[] for _ in range(m)]     # 矩阵的输入都搞了半天，不熟悉输入。。需要加强训练！！
for i in range(len(A)):
    A[i] = (input().strip().split(' '))[:k]
B = [[] for _ in range(k)]
for i in range(len(B)):
    B[i] = (input().strip().split(' '))[:n]

def Matrix_Multiply(A, B):
    global res
    res = [[0]*len(B[0]) for _ in range(m)] # 这种写法，要记住了！不许模棱两可！
    for i in range(0, len(A)):
        for j in range(0, len(B[0])):
            for t in range(0, k):
                res[i][j] += int(A[i][t]) * int(B[t][j]) # 这是精髓，也是考试时没有想到的！学习了
    return res

ans = Matrix_Multiply(A, B)
# print(ans)

for i in range(len(ans)):
    # print(end='\n')
    for j in range(len(ans[0])):
        if j == len(ans[0])-1:
            print(ans[i][j]) # 这里默认 end = '\n'
        else:
            print(ans[i][j], end=' ')
            
