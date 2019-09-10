

class Solution():
    def isValid(self, s):
        '''
        :type s: str
        :rtype: bool
        '''
        stack = []
        look_up = {'(': ')', '{': '}', '[': ']'}
        for parenthese in s:
            if parenthese in look_up:
                stack.append(parenthese)
            elif len(stack) == 0 or look_up[stack.pop()] != parenthese: # len(stack) == 0为了排除只有'}' or "]"的情况
                return False
        return len(stack) == 0  # 这个式子是个bool值，为了排除只有一个'[' 或者 '{'的情况


if __name__ == '__main__':
    a = Solution()
    s = '[{]}'
    # s = '{[]}'
    print(a.isValid(s))
