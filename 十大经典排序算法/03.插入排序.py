def InsertionSort(nums):
    for i in range(len(nums)):
        preIndex = i - 1
        current = nums[i]
        while preIndex >= 0 and nums[preIndex] > current: # nums[preIndex] >= current，如果这样写，插入排序是否就变得不稳定了？
            nums[preIndex+1] = nums[preIndex]
            preIndex -= 1
        nums[preIndex+1] = current
    return nums

nums = [6, 10, 43, 32, 23, 14]
print(InsertionSort(nums))


