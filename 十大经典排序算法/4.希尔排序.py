def ShellSort(nums):
    gap = 1
    while gap < len(nums)/3: 
        gap = gap * 3 + 1  # 代码中的3可以改，一起改
    while gap > 0:
        for i in range(gap, len(nums)):
            temp = nums[i]
            j = i - gap
            while j >= 0 and nums[j] > temp:
                nums[j + gap] = nums[j]
                j -= gap
            nums[j + gap] = temp
        gap = gap//3
    return nums


nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(ShellSort(nums))
