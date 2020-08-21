def countingSort(nums):
    bucketLen = max(nums) + 1
    bucket = [0] * bucketLen
    sort_idx = 0
    for i in range(len(nums)):
        if not bucket[nums[i]]:
            bucket[nums[i]] = 0
        bucket[nums[i]] += 1
    for j in range(bucketLen):
        while bucket[j] > 0:
            nums[sort_idx] = j
            sort_idx += 1
            bucket[j] -= 1
    return nums

nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(countingSort(nums))
