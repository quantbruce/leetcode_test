class SortNums():
    def __init__(self):
        pass

    def BubbleSort(self, nums):
        for i in range(1, len(nums)):
            for j in range(len(nums) - i):
                if nums[j] > nums[j + 1]:
                    nums[j], nums[j + 1] = nums[j + 1], nums[j]
        return nums

    def SelectSort(self, nums):
        for i in range(len(nums)-1):
            min_idx = i
            for j in range(i+1, len(nums)):
                if nums[min_idx] > nums[j]:
                    min_idx = j
            if min_idx != i:
                nums[min_idx], nums[i] = nums[i], nums[min_idx]
        return nums


    def InsertSort(self, nums):
        for i in range(len(nums)):
            preidx = i - 1
            cur = nums[i]
            while preidx >= 0 and nums[preidx] >= cur:
                nums[preidx+1] = nums[preidx]
                preidx -= 1
            nums[preidx+1] = cur
        return nums


    def ShellSort(self, nums):
        gap = 1
        while gap < len(nums) // 3:
            gap = gap * 3 + 1
        while gap:
            for i in range(gap, len(nums)):
                preidx = i - gap
                cur = nums[i]
                while preidx >= 0 and nums[preidx] >= cur:
                    nums[preidx+gap] = nums[preidx]
                    preidx -= gap
                nums[preidx+gap] = cur
            gap //= 3
        return nums


    def MergeSort(self, nums):
        if len(nums) < 2:
            return nums
        middle = len(nums)//2
        left, right = nums[:middle], nums[middle:]
        return self.merge(self.MergeSort(left), self.MergeSort(right))

    def merge(self, left, right):
        res = []
        while left and right:
            if left[0] <= right[0]:
                res.append(left.pop(0))
            else:
                res.append(right.pop(0))
        while left:
            res.append(left.pop(0))
        while right:
            res.append(right.pop(0))
        return res



    def QuickSort(self, nums):
        return self.Qsort(nums, 0, len(nums)-1)

    def Qsort(self, nums, low, high):
        if low < high:
            pivot = self.Partition(nums, low, high)
            self.Qsort(nums, low, pivot-1)
            self.Qsort(nums, pivot+1, high)
        return nums

    def Partition(self, nums, low, high):
        pivot = nums[low]
        while low < high:
            while low < high and nums[high] >= pivot:
                high -= 1
            nums[low] = nums[high]
            while low < high and nums[low] <= pivot:
                low += 1
            nums[high] = nums[low]
        nums[low] = pivot
        return low




    def BuildMaxHeap(self, nums):
        for i in range(len(nums)//2, -1, -1):
            self.heapify(nums, i)

    def heapify(self, nums, i):
        left = 2 * i + 1
        right = 2 * i + 2
        largest = i
        while left < numsLen and nums[left] > nums[largest]:
            largest = left
        while right < numsLen and nums[right] > nums[largest]:
            largest = right
        if largest != i:
            self.swap(nums, i, largest)
            self.heapify(nums, largest)

    def swap(self, nums, i, j):
        nums[i], nums[j] = nums[j], nums[i]

    def HeapSort(self, nums):
        global numsLen
        numsLen = len(nums)
        self.BuildMaxHeap(nums)
        for i in range(numsLen-1, 0, -1):
            self.swap(nums, i, 0)
            numsLen -= 1
            self.heapify(nums, 0)
        return nums


    def CountSort(self, nums):
        bucketLen = max(nums) + 1
        bucket = [0] * bucketLen
        sort_idx = 0
        for i in range(len(nums)):
            bucket[nums[i]] += 1
        for j in range(bucketLen):
            while bucket[j] > 0:
                nums[sort_idx] = j
                sort_idx += 1
                bucket[j] -= 1
        return nums


    def RidxSort(self, nums):
        digit = 0
        max_digit = 1
        max_val = max(nums)

        while 10**max_digit < max_val:
            max_digit += 1

        while digit < max_digit:
            tmp = [[] for _ in range(10)]
            for i in nums:
                t = i // 10 ** digit % 10
                tmp[t].append(i)
            new_nums = []
            for bucket in tmp:
                for i in bucket:
                    new_nums.append(i)
            nums = new_nums
            digit += 1
        return nums



model = SortNums()
# nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
nums = [i for i in range(1000, -1, -1)]

import time

t1 = time.time()
print(model.BubbleSort(nums))
print('BubbleSort:', time.time()-t1)

t2 = time.time()
print(model.SelectSort(nums))
print('SelectSort:', time.time()-t2)

t3 = time.time()
print(model.InsertSort(nums))
print('InsertSort:', time.time()-t3)

t4 = time.time()
print(model.ShellSort(nums))
print('ShellSort:', time.time()-t4)

t5 = time.time()
print(model.MergeSort(nums))
print(time.time() - t5)

t6 = time.time()
print(model.QuickSort(nums))
print(time.time() - t6)

t7 = time.time()
print(model.HeapSort(nums))
print(time.time() - t7)

t8 = time.time()
print(model.CountSort(nums))
print(time.time() - t8)

t9 = time.time()
print(model.RidxSort(nums))
print(time.time() - t9)
