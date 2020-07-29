####################方法1 暴力法

class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()

    def max_value(self) -> int:
        return max(self.queue) if self.queue else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        return self.queue.popleft() if self.queue else -1
    

####################方法2 维护一个双端队列
###############还有多种变体版本
import queue
class MaxQueue:
    def __init__(self):
        self.queue = queue.Queue()
        self.deque = queue.deque()    

    def max_value(self) -> int:
        if self.deque: 
            return self.deque[0]
        else: 
            return -1

    def push_back(self, value: int) -> None:
        while self.deque and self.deque[-1] < value:
            self.deque.pop()
        self.deque.append(value)
        self.queue.put(value) #相当于append(),这两个方法不熟悉，要多用

    def pop_front(self) -> int:
        if not self.deque: return -1
        ans = self.queue.get() # 相当于.pop(), 这两个方法不熟悉，要多用
        if ans == self.deque[0]:
            self.deque.popleft()
        return ans
    
#都是O(1)
https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/ru-he-jie-jue-o1-fu-za-du-de-api-she-ji-ti-by-z1m/

    
    
    
    
    
    
