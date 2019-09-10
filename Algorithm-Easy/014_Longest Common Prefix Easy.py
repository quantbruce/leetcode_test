class Solution():
    def longestCommonPrefix(self, strs):
        '''
        type strs: List[str]
        rtype: str
        '''
        if not strs:
            return('')   # 这里要return()才是对的，用print()会退出
        for i in range(len(strs[0])):
            for string in strs[1:]:
                if i >= len(string) or string[i] != strs[0][i]:  # 因为i是从0开始,而len(string)是从1开始
                    return(strs[0][:i])  # 所以这个i取不到，才是想要的效果。自己体会，可以画画
        return(strs[0])  # 是最开始字符串前面空了个空格的情况 strs = [" flower","flow","flight", "flip"]

if __name__ == '__main__':
    # strs = ["flower","flow","flight", "flip"]
    strs = []
    print(Solution().longestCommonPrefix(strs))
    
    
    #### Better Way
    class Solution():
    def longestCommonPrefix(self, strs):
        '''
        :param strs: list[str]
        :return: str
        '''
        result = ''
        i = 0
        while True:
            try:
                sets = set(string[i] for string in strs)  # set()只返回元素唯一的元素，重复出现的元素也只返回一次
                if len(sets) == 1:
                    result += sets.pop()
                    i += 1
                else:
                    break
            except Exception as e:
                break
        return result
    
    if __name__ == '__main__':
        strs = ["flower", "flow", "flight", "flip"]
        a = Solution()
        print(a.longestCommonPrefix(strs))

