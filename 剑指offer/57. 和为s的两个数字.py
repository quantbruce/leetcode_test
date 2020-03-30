###########我的暴力解法(只是从理论上可行，实际上会超时！！)


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i=0
        res = []
        while target-nums[i] not in nums:
            i+=1
        res.append(nums[i])
        # while len(res)<2:
        for j in range(i+1, len(nums)):
            if target-nums[j]!=res[0]:
                pass
            else:
                res.append(nums[j])
                break
        return res
        
 
 ###################双指针法解决排序数组
 class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        i, j = 0, len(nums) - 1
        while i < j:
            s = nums[i] + nums[j]
            if s > target: j -= 1
            elif s < target: i += 1
            else: return nums[i], nums[j]
        return []


链接：https://leetcode-cn.com/problems/he-wei-sde-liang-ge-shu-zi-lcof/solution/mian-shi-ti-57-he-wei-s-de-liang-ge-shu-zi-shuang-/

    
    
######滑动窗口法(最优)
def findContinuousSequence(self, target: int) -> List[List[int]]:
    i = 1 # 滑动窗口的左边界    # i, j都从1开始才对，否则例如输入15，但最终结果[[0,1,2,3,4,5],[1,2,3,4,5],[4,5,6],[7,8]]， 其中会包含0，是错误的
    j = 1 # 滑动窗口的右边界
    sum = 0 # 滑动窗口中数字的和
    res = []

    while i <= target // 2:
        if sum < target:
            # 右边界向右移动
            sum += j
            j += 1
        elif sum > target:
            # 左边界向右移动
            sum -= i
            i += 1
        else:
            # 记录结果
            arr = list(range(i, j))
            res.append(arr)
            # 左边界向右移动
            sum -= i
            i += 1

    return res

https://leetcode-cn.com/problems/he-wei-sde-lian-xu-zheng-shu-xu-lie-lcof/solution/shi-yao-shi-hua-dong-chuang-kou-yi-ji-ru-he-yong-h/
