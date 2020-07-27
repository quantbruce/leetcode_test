########方法1 哈希表的使用

class Solution:
    def firstUniqChar(self, s: str) -> str:
        dic = {}
        for c in s:
            dic[c] = dic.get(c,0) + 1
        for c in s:
            if dic[c] == 1: return c
        return " "

#时间复杂度：O(N)
#空间复杂度：O(N)
https://leetcode-cn.com/problems/di-yi-ge-zhi-chu-xian-yi-ci-de-zi-fu-lcof/solution/mian-shi-ti-50-di-yi-ge-zhi-chu-xian-yi-ci-de-zi-3/
    

##############方法2 对方法1的优化
class Solution:
    def firstUniqChar(self, s: str) -> str:
        d = {}
        for c in s:
            d[c] = d.get(c, 0) + 1
        for k,v in d.items():
            if v==1: return k
        return " "
    
#时间复杂度：O(N)
#空间复杂度：O(N)
        
