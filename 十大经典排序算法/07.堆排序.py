def buildMaxHeap(nums):
    for i in range(len(nums)//2, -1, -1): # len(num)//2 就是最后一个非叶子节点，要从他开始算。因为每个叶子节点本身而言，都已经是堆了，不用调整了。
        heapify(nums, i)

def heapify(nums, i):
    left = 2 * i + 1
    right = 2 * i + 2
    largest = i
    while left < numsLen and nums[left] > nums[largest]:  
        largest = left
    while right < numsLen and nums[right] > nums[largest]:
        largest = right
    if largest != i:
        swap(nums, i, largest)
        heapify(nums, largest)

def swap(nums, i, j):
    nums[i], nums[j] = nums[j], nums[i]

def HeapSort(nums):
    global numsLen
    numsLen = len(nums)
    buildMaxHeap(nums)
    for i in range(numsLen-1, 0, -1):
        swap(nums, 0, i)
        numsLen -= 1
        heapify(nums, 0)
    return nums

nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(HeapSort(nums))


