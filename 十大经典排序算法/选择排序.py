def SelectionSort(nums):
    for i in range(len(nums)-1):
        min_idx = i
        for j in range(i+1, len(nums)):
            if nums[j] < nums[min_idx]:
                min_idx = j
        if min_idx != i:
            nums[i], nums[min_idx] = nums[min_idx], nums[i]
    return nums

#时间复杂度：O(N**2)
#空间复杂度：O(1)
nums = [6, 5, 4, 3, 2, 1]
print(SelectionSort(nums))

