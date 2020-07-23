###################方法1 递归分治
class Solution(object):
    def verifyPostorder(self, postorder):
        def recur(i, j):
            if i>=j: return True
            p = i
            while postorder[p] < postorder[j]: p+=1
            m = p
            while postorder[p] > postorder[j]: p+=1
            return p==j and recur(i, m-1) and recur(m, j-1)
        return recur(0, len(postorder)-1)
    
#时间复杂度: O(N**2)
#空间复杂度：O(N)

##########################################这种方法很费解，还没吃透。吃了一下午，后续反复肯！！！！
class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        stack, root = [], float("+inf")
        for i in range(len(postorder) - 1, -1, -1):
            if postorder[i] > root: return False
            while(stack and postorder[i] < stack[-1]):
                root = stack.pop()
            stack.append(postorder[i])
        return True


https://leetcode-cn.com/problems/er-cha-sou-suo-shu-de-hou-xu-bian-li-xu-lie-lcof/solution/mian-shi-ti-33-er-cha-sou-suo-shu-de-hou-xu-bian-6/





