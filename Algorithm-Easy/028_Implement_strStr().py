class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i + len(needle)] == needle:   ## 这种写法，需要注意
                return i
        return -1

if __name__ == '__main__':
    print(Solution().strStr("hello", "lo"))
