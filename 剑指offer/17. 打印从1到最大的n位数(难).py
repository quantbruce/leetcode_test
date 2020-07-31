class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1,10**n)]

######################################这一题真是考察要点python容易掩盖，还需要继续斟酌！######################################
class Solution:
    def printNumbers(self, n: int) -> [int]:
        def dfs(x):
                if x==n:
                    s=''.join(num[self.start:])   # n−nine = start, n-nine等于几，下标就从几开始，可以这样记
                    if s!='0': res.append(int(s))
                    if n - self.start == self.nine: self.start -= 1 # 减1就是start的下标往左移。例如。099——>100时
                    return
                for i in range(10):
                    if i==9: self.nine += 1
                    num[x] = str(i)
                    dfs(x+1)
                self.nine -= 1 #回溯每跳出一层，数位减少一个，9的数目自然要减少1

        num, res = ['0']*n, []
        self.nine = 0
        self.start = n-1 # 为什么这里是n-1
        dfs(0)
        return res

#时间复杂度：O(10**n)  
#空间复杂度：O(N)
