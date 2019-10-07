### Best Way
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        return(bin(int(a, base=2)+ int(b, base=2))[2:])  # 就是一行代码解决！
        
### Michelle Way
class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        result, carry, val = '', 0, 0  # carry是是否要进位，只能取0或1，val是逐个字符变量，result是最后返回结果。
        for i in range(max(len(a), len(b))): #  因为不知道a,b哪个更长
            val = carry       # 如果有进位，则进位就等于变量val, 因为最后有result+str(val),
            if i < len(a):
                val += int(a[-(i+1)])  # 从右向左的加
            if i < len(b):
                val += int(b[-(i+1)])
            carry = val//2    # 精髓部分， carry控制在0，1之间， val=1,2,3分别去考虑进位与val的保留，去体会下！
            val = val%2       # 开始val能娶到0,1,2,3，取模后确保val只能取到0，1
            result += str(val)
        if carry: # 如果最左边的是1+1, 则最后拓展一位
            result += str(1)
        return(result[::-1])
        
