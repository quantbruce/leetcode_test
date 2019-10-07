#### Michelle Way
class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 2:
            return x
        left, right = 1, x//2 # right没必要从最后一位取
        while left <= right:
            mid = left + (right-left)//2
            if mid <= x/mid:  # 这个=很重要，体会这种两边逼近的思想, 等号跟着小于走，因为一开始mid*mid是要小于x的，他是逐渐增大的，一直到等于
                left = mid + 1
            else:
                right = mid - 1
        return right # left-1也行  最后返回的时候left和right已经交叉，也即left>right
