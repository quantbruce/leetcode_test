
def BubbleSort(nums):
    """
    :param nums:list
    :return: list
    """
    for i in range(1, len(nums)):
        for j in range(0, len(nums)-i):
            if nums[j] > nums[j+1]:
                nums[j], nums[j+1] = nums[j+1], nums[j]
    return nums

#时间复杂度: O(N**2)
#空间复杂度: O(1)

nums = [6, 5, 4, 3, 2, 1]
print(BubbleSort(nums))
