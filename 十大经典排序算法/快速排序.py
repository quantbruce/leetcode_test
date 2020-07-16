############方法1 递归法

def QuickSort(nums):
    if len(nums) < 2: return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(QuickSort(nums))

https://www.runoob.com/python3/python-quicksort.html



############方法2 

