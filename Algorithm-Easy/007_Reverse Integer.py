class Solution:
    def reverse(self, x):
        num = 0
        a = abs(x)
        while(a != 0):
            pop = a % 10
            num = num * 10 + pop
            a = int(a / 10)
        if x > 0 and num < 2147483647:
            return num
        elif x < 0 and num <= 2147483647:
            return -num
        else:
            return 0

if __name__ == '__main__':
    print(Solution().reverse(123))
