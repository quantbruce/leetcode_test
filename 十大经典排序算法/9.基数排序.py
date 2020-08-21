def RadixSort(nums):
    digit = 0
    max_digit = 1
    max_val = max(nums)

    while 10**max_digit < max_val: # 注意是10**max_digit
        max_digit = max_digit + 1

    while digit < max_digit:
        temp = [[] for _ in range(10)] # 用[]模拟桶
        for i in nums:
            t = i // 10 ** digit % 10
            temp[t].append(i)

        new_nums = []
        for bucket in temp:
            for i in bucket:
                new_nums.append(i)
        nums = new_nums
        digit += 1
    return nums

nums = [81, 94, 11, 96, 12, 35, 17, 95, 28, 58, 41, 75, 15]
print(RadixSort(nums))
