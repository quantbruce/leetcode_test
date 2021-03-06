class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.A, self.B = [], []


    def push(self, x: int) -> None:
        self.A.append(x)
        if not self.B or x<=self.B[-1]: # not self.B是第一次，x <= self.B[-1] 是后面那几次. 这里经常漏写了=号这种情况。记住了！！
            self.B.append(x)

    def pop(self) -> None:
        if self.A.pop() == self.B[-1]: # 不管这个if是否成立，self.A.pop()都会执行，只是成立的时候self.B.pop()才会同时执行，这个细节很重要！！！
            self.B.pop()

    def top(self) -> int:
        return self.A[-1]

    def min(self) -> int:
        return self.B[-1]
 
#时间复杂度：O(1)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/bao-han-minhan-shu-de-zhan-lcof/solution/mian-shi-ti-30-bao-han-minhan-shu-de-zhan-fu-zhu-z/
       
