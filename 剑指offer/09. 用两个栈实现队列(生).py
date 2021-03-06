class CQueue:

    def __init__(self):
        self.A, self.B = [], []

    def appendTail(self, value: int) -> None:
        self.A.append(value)

    def deleteHead(self) -> int:
        if not self.B:
            while self.A:
                self.B.append(self.A.pop())
        return self.B.pop() if self.B else -1
    
    #时间复杂度: append() O(1), deletehead(), O(N)
    #空间复杂度：最坏O(N)
    https://leetcode-cn.com/problems/yong-liang-ge-zhan-shi-xian-dui-lie-lcof/solution/mian-shi-ti-09-yong-liang-ge-zhan-shi-xian-dui-l-2/
