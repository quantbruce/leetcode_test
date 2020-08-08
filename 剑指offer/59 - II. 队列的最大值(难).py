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

#############两个list的变体版本
class MaxQueue:

    def __init__(self):
        self.queue = []
        self.max_stack = []  # 本质也是在维护一个单调递减的栈

    def max_value(self) -> int:
        return self.max_stack[0] if self.max_stack else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)
        while self.max_stack and self.max_stack[-1] < value:
            self.max_stack.pop()
        self.max_stack.append(value)

    def pop_front(self) -> int:
        if not self.queue: return -1
        ans = self.queue.pop(0)
        if self.max_stack[0] == ans:
            self.max_stack.pop(0)
        return ans

https://leetcode-cn.com/problems/dui-lie-de-zui-da-zhi-lcof/solution/ru-he-jie-jue-o1-fu-za-du-de-api-she-ji-ti-by-z1m/
    
