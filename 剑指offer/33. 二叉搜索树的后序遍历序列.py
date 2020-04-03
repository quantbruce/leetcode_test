class Solution:
    def verifyPostorder(self, postorder: [int]) -> bool:
        def recur(i, j):
            if i >= j: return True
            l = i
            while postorder[l] < postorder[j]: l += 1
            m = l
            while postorder[l] > postorder[j]: l += 1
            return l == j and recur(i, m - 1) and recur(m, j - 1)

        return recur(0, len(postorder) - 1)


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





