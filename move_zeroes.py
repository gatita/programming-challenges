def move_zeroes(nums):
    count = nums.count(0)
    for i in nums:
        if i == 0:
            nums.remove(i)
    nums += count * [0]
