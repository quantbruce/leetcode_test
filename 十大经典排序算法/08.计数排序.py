def countingSort(nums):
    bucketLen = max(nums) + 1
    bucket = [0] * bucketLen
    sort_idx = 0
    for i in range(len(nums)):
       # if not bucket[nums[i]]:  这两行代码是冗余的，可以不要
        #    bucket[nums[i]] = 0
        bucket[nums[i]] += 1
    for j in range(bucketLen): # 因为bucketLen在这里作为区间右端点(上限), 娶不到, 所以上面要加1
        while bucket[j] > 0:
            nums[sort_idx] = j
            sort_idx += 1      # 这个算法排序没用到比较，排序原理的精髓在于利用了索引天然的有序性
            bucket[j] -= 1
    return nums

nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(countingSort(nums))
