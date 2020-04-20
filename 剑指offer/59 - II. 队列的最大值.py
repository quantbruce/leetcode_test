"""
执行用时 :
284 ms
, 在所有 Python3 提交中击败了
62.24%
的用户
内存消耗 :
17.3 MB
, 在所有 Python3 提交中击败了
100.00%
的用户
"""

class MaxQueue:

    def __init__(self):
        self.queue = collections.deque()

    def max_value(self) -> int:
        return max(self.queue) if self.queue else -1

    def push_back(self, value: int) -> None:
        self.queue.append(value)

    def pop_front(self) -> int:
        return self.queue.popleft() if self.queue else -1
