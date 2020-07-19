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
    
时间复杂度 O(N)： 遍历使用 O(N) ，每轮添加（修改）字符操作使用 O(1)；
空间复杂度 O(N)： Python 新建的 list 和 Java 新建的 StringBuilder 都使用了线性大小的额外空间。

https://leetcode-cn.com/problems/ti-huan-kong-ge-lcof/solution/mian-shi-ti-05-ti-huan-kong-ge-ji-jian-qing-xi-tu-/

        
