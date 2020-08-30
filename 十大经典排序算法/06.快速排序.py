############方法1 递归法

"""
这段代码虽然短小利于理解，但是其效率很低，主要体现在以下方面：

分组基准的选取过于随便，不一定可以取到列表的中间值
空间复杂度大，使用了两个列表解析式，而且每次选取进行比较时需要遍历整个序列。
若序列长度过于小(比如只有几个元素)，快排效率就不如插入排序了。
递归影响性能，最好进行优化。
https://www.jianshu.com/p/2b2f1f79984e
"""

def QuickSort(nums):
    if len(nums) < 2: return nums
    pivot = nums[len(nums)//2]
    left = [x for x in nums if x < pivot]
    middle = [x for x in nums if x == pivot]
    right = [x for x in nums if x > pivot]
    return QuickSort(left) + middle + QuickSort(right)

#时间复杂度：?
#空间复杂度：?
nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(QuickSort(nums))

https://www.runoob.com/python3/python-quicksort.html



############方法2 C语言版本
###这种写法是和王卓老师推荐得一样，非常经典，有利于体验快排的精髓
###疑惑： 为什么 当nums=[i for i in range(1000, -1, -1)]或者更大，方法1不报错，而放法2却报错 RecursionError: maximum recursion depth exceeded in comparison ？？？？

def QuickSort(nums):
    return Qsort(nums, 0, len(nums)-1)

def Qsort(nums, low, high):
    if low < high:         # 这个地方老写错，注意是if而不是while
        pivot = Partition(nums, low, high) # pivot是每一轮最后low和high重合的下标，这个是最后才能知道的。Partition的目标就在于获得它。
        Qsort(nums, low, pivot - 1)
        Qsort(nums, pivot + 1, high)
    return nums

def Partition(nums, low, high):
    pivot = nums[low]
    while low < high:
        while low < high and nums[high] >= pivot:
            high -= 1
        nums[low] = nums[high]
        while low < high and nums[low] <= pivot:
            low += 1
        nums[high] = nums[low]
    nums[low] = pivot # 把最后那个靠中间的空，用最初的pivot填上
    return low

#时间复杂度：O(N*log(N))
#空间复杂度：O(1)
nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(QuickSort(nums))

https://www.runoob.com/python3/python-quicksort.html

    
    
    
