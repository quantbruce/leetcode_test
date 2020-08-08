############考察了原码、反码、补码等关键概念。这题比较容易混，综合难度较高


##################################方法1  位运算法 
### 原理其实和Krahets的方法是一致的
class Solution(object):
    def add(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # (n & 0xffffffff)进行这种变换的原因是,如果存在负数则需要转换成补码的形式,正数补码是他本身
        a &= 0xffffffff#
        b &= 0xffffffff
        while b != 0:
            carry = ((a & b) << 1) & 0xffffffff#如果是负数,转换成补码形式
            a ^= b
            b = carry
        if a < 0x80000000:#如果是正数的话直接返回
            return a
        else:
            return  ~(a^0xffffffff) #是负数的话,转化成其原码


https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/pythonti-jie-er-jin-zhi-zhuan-hua-yi-ji-pythonzhua/

    
    
######################方法2 位运算法 Krahets
class Solution:
    def add(self, a: int, b: int) -> int:
        x = 0xffffffff
        a, b = a & x, b & x
        while b != 0:
            a, b = a^b, (a & b)<<1 & x
        return a if a<= 0x7fffffff else ~(a^x)
    
    
#时间复杂度：O（1）????????
#空间复杂度：O（1）???????
https://leetcode-cn.com/problems/bu-yong-jia-jian-cheng-chu-zuo-jia-fa-lcof/solution/mian-shi-ti-65-bu-yong-jia-jian-cheng-chu-zuo-ji-7/

# 0x7FFFFFFF 是long int的最大值
https://blog.csdn.net/cwj649956781/article/details/8589981
    
    
    
    
    
    
