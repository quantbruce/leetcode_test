##############感觉这题是很浪费时间的SB题，暂且只学会取巧法

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """
        try:
            float(s)
            return True
        except :
            return False


https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/solution/onpythonjie-ti-wu-fa-luo-ji-pan-duan-regexdfadeng-/
    
    
class Solution:
    def isNumber(self, s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
