########################计数排序法
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        nums = [0] * 10000
        for a in arr:
            nums[a]+=1
        output=[]
        i = 0
        while len(output)<k: # 这个地方默写len(output)错了
            if nums[i]>0:
                for _ in range(nums[i]):
                    output.append(i)
            i+=1
        return output[:k] # 这个地方容易漏[:k]
#时间复杂度：O(N+K)       
#空间复杂度：O(K)???
https://leetcode-cn.com/problems/zui-xiao-de-kge-shu-lcof/solution/bu-pai-xu-bu-long-guo-lu-qi-miao-sha-88-by-libins/
