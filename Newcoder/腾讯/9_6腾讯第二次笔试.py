#这个解答只能通过10%的测试。。。 目前没搞懂原因

T = int(input())

def helper(n):
    arr = []
    for j in range(n):
        tmp = list(map(int, input().strip().split(' ')))[:6]
        arr.append(sorted(tmp))
    for k in range(n - 1):
        if sorted(arr[k]) == sorted(arr[k + 1]):
            return "YES"
        else:
            return "NO"

for _ in range(T):
    n = int(input())
    print(helper(n))
    
    
