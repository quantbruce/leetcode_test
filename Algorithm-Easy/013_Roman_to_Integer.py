#### My follow
class Solution():
    def romanToint(self, s):
        dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(s)):
            if i > 0 and dict[s[i]] > dict[s[i-1]]:
                result += dict[s[i]] - 2 * dict[s[i-1]]
            else:
                result += dict[s[i]]
        print(result)


if __name__ == '__main__':
    Solution().romanToint('MCDXXXVII')
    
    
#### Others
class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        numeral_map = {"I":1, "V":5, "X": 10, "L":50, "C":100,"D": 500, "M": 1000}
        decimal = 0
        for i in range(len(s)):
            if i > 0 and numeral_map[s[i]] > numeral_map[s[i-1]]:
                decimal += numeral_map[s[i]] - 2 * numeral_map[s[i-1]]
            else:
                decimal += numeral_map[s[i]]
        return decimal

if __name__ == '__main__':
    print(Solution().romanToInt("MCMXCIV"))
