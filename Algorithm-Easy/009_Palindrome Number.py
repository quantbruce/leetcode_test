#### My Method

class Solution:
    def isPalindrome(self, x):
        num = x
        count = 0
        ls = list(str(x))
        for i in range(len(ls) // 2):
            if ls[i] == ls[-i-1]:
                count += 1
                if count == len(ls)//2:
                    print('True')
            elif num < 0 and ls[i] != ls[-i-1]:
                print('False')
                return
            elif len(ls) % 2 == 0:
                print('False')

if __name__ == '__main__':
    x = int(input('please input x = '))
    Solution().isPalindrome(121)
    
    
#### Other Method(better)
class Solution:
    def isPalindrome(self, x):
        '''
        :param x int:
        :return bool:
        '''
        opt_num = 0
        a = abs(x)
        while a != 0:
            temp = a % 10
            opt_num = opt_num * 10 + temp
            a //= 10

        if x >= 0 and x == opt_num:
            return True
        else:
            return False

if __name__ == '__main__':
    print(Solution().isPalindrome(0))


#########简洁高效法    
class Solution:
def isPalindrome(self, x: int) -> bool:
    return str(x)==str(x)[::-1]

# 方法4: 将int转化成str类型: 双指针 (指针的性能一直都挺高的)
# 复杂度: O(n)
def isPalindrome(x: int) -> bool:
    lst = list(str(x))
    L, R = 0, len(lst)-1
    while L <= R:
        if lst[L] != lst[R]:
            return  False
        L += 1
        R -= 1
    return True

######方法5
class Solution:
    def isPalindrome(self, x: int) -> bool:
        return True if str(x)==str(x)[::-1] else False



