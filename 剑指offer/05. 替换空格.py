class Solution:
    def replaceSpace(self, s: str) -> str:
        list_ = []
        rep = "%20"
        for i in s:
            if i != " ":
                list_.append(i)
            else:
                list_.append(rep)
        return ''.join(list_)            #### .join()函数实现list->str
    
    
 https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/
