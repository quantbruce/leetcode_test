### Better way

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in reversed(range(len(digits))):  # 倒过来读列表，3，2，1，0
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits   # 理解这一步的return很关键，return出去就不会在执行下个循环了
        digits[0] = 1     # 考虑极端情况9999
        digits.append(0)
        return digits
