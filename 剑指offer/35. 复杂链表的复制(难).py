# 浅拷贝只复制指向某个对象的指针，而不复制对象本身，新旧对象还是共享同一块内存。但深拷贝会另外创造一个一模一样的对象，新对象跟原对象不共享内存，修改新对象不会改到原对象。


###############方法1 面试官骂人法
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        return copy.deepcopy(head)


###############方法2 DFS
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        def dfs(head):
            if not head: return None
            if head in visited: # visited是用来保存已经生成的节点的，字典能代去重属性
                return visited[head]
            # 创建新结点
            copy = Node(head.val, None, None)
            visited[head] = copy    # 这一行这种映射关系总容易弄错
            copy.next = dfs(head.next)
            copy.random = dfs(head.random)
            return copy
        visited = {}
        return dfs(head)
    
#时间复杂度: O(N)
#空间复杂度: O(N)
 
    
####################方法3 BFS
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}    
        def bfs(head):
            if not head: return head
            clone = Node(head.val, None, None) # 创建新结点
            queue = collections.deque()
            queue.append(head)
            visited[head] = clone
            while queue:
                tmp = queue.pop()
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, [], [])
                    queue.append(tmp.next)  
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, [], [])
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next)
                visited[tmp].random = visited.get(tmp.random)
            return clone  ####################################??????????????????， 看清答主解释，clone是复制后的链表的头节点
        return bfs(head)
#时间复杂度：O(N)
#空间复杂度：O(N)
    
    
########我默写的方法3 BFS 
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def bfs(head):
            if not head: return head
            clone = Node(head.val, None, None)
            queue = [head]
            visited[head] = clone
            while queue:
                tmp = queue.pop(0) # pop(0)也能AC, 感觉这样更符合队列的味道
                if tmp.next and tmp.next not in visited:
                    visited[tmp.next] = Node(tmp.next.val, None, None) # 这里写成None或者[]都是可以的
                    queue.append(tmp.next)
                if tmp.random and tmp.random not in visited:
                    visited[tmp.random] = Node(tmp.random.val, None, None)
                    queue.append(tmp.random)
                visited[tmp].next = visited.get(tmp.next) #奇怪，为什么visited[tmp.next]就会报错，非空报错？ # dic = {'a':1, 'b':2, 'c':3}
                visited[tmp].random = visited.get(tmp.random) #同样，visited[tmp.random]也会报错，非空报错   # print(dic['d'])
            return clone                                                                                   # print(dic.get('b'))
        return bfs(head)
#时间复杂度：O(N)
#空间复杂度：O(N)


######################方法4 迭代
###日后细究
class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        visited = {}
        def getClonedNode(node):
            if node:
                if node in visited:
                    return visited[node]
                else:
                    visited[node] = Node(node.val,None,None)
                    return visited[node]
            return None
        
        if not head: return head
        old_node = head
        new_node = Node(old_node.val,None,None)
        visited[old_node] = new_node

        while old_node:
            new_node.random = getClonedNode(old_node.random)
            new_node.next = getClonedNode(old_node.next)
            
            old_node = old_node.next
            new_node = new_node.next
        return visited[head]


https://leetcode-cn.com/problems/fu-za-lian-biao-de-fu-zhi-lcof/solution/lian-biao-de-shen-kao-bei-by-z1m/



