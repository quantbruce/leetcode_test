class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1,10**n)]

######################################这一题真是考察要点python容易掩盖，还需要继续斟酌！######################################
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
                if x==n:
                    s=''.join(num[self.start:])
                    if s!='0': res.append(int(s))
                    if n - self.start == self.nine: self.start -= 1
                    return
                for i in range(10):
                    if i==9: self.nine += 1
                    num[x] = str(i)
                    dfs(x+1)
                self.nine -= 1

        num, res = ['0']*n, []
        self.nine = 0
        self.start = n-1
        dfs(0)
        return res

#时间复杂度：O(10**n)  
#空间复杂度：O(N)
