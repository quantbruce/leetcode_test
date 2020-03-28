########################计数排序法
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        nums = [0] * 10000
        for a in arr:
            nums[a]+=1
        output=[]
        i = 0
        while len(output)<k:
            if nums[i]>0:
                for _ in range(nums[i]):
                    output.append(i)
            i+=1
        return output[:k]
        
        https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/bu-pai-xu-bu-long-guo-lu-qi-miao-sha-88-by-libins/
