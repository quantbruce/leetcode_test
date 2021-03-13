
# inspired by 小抄 
# and https://leetcode-cn.com/problems/lru-cache/solution/shu-ju-jie-gou-fen-xi-python-ha-xi-shuang-xiang-li/


"""
执行用时：168 ms, 在所有 Python3 提交中击败了68.14%的用户
内存消耗：23.7 MB, 在所有 Python3 提交中击败了14.62%的用户
"""

class DLinkedNode:
    def __init__(self, key=None, value=None):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.map = {}
        self.head = DLinkedNode()
        self.tail = DLinkedNode()
        self.head.next = self.tail
        self.tail.prev = self.head
        
    def move_node_to_tail(self, key):
        # 把node单独抽出来
        node = self.map[key]
        node.prev.next = node.next
        node.next.prev = node.prev
        # 在把node放到双链表最后 (注意以下顺序，容易混)
        node.prev = self.tail.prev # node被赋值
        node.next = self.tail
        self.tail.prev.next = node # 用node赋值
        self.tail.prev = node

    def get(self, key: int) -> int:
        if key in self.map:
            self.move_node_to_tail(key)
        res = self.map.get(key, -1)
        if res == -1:
            return res
        else:
            return res.value

    def put(self, key: int, value: int) -> None:
        if key in self.map:
            self.map[key].value = value
            self.move_node_to_tail(key)
        else:
            if len(self.map) == self.capacity:
                # 去掉map的对应key
                self.map.pop(self.head.next.key)
                # 再删除双链表中的最(左端)久远的节点self.head
                self.head.next = self.head.next.next
                self.head.next.prev = self.head
            # 如果不在的话就插入到尾节点前
            new = DLinkedNode(key, value)
            self.map[key] = new
            new.prev = self.tail.prev
            new.next = self.tail
            self.tail.prev.next = new
            self.tail.prev = new
            

# 时间复杂度：O(1)
# 空间复杂度：O(1)





            
            
            
