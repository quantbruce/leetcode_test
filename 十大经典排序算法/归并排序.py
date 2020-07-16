def mergeSort(nums):
    if len(nums) < 2: return nums
    middle = len(nums)//2
    left, right = nums[:middle], nums[middle:]
    return merge(mergeSort(left), mergeSort(right))

def merge(left, right):
    result = []
    while left and right:
        if left[0] <= right[0]:  # 这个地方等号有无都可以
            result.append(left.pop(0))
        else:
            result.append(right.pop(0))
    while left:
        result.append(left.pop(0))
    while right:
        result.append(right.pop(0))
    return result


nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(mergeSort(nums))
