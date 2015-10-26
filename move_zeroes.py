def move_zeroes(nums):
    """Given a list, move all 0's to the end while maintaining the
    order of non-zero elements. Modifies the list in place.
    """
    for i in nums:
        if i == 0:
            nums.remove(i)
            nums.append(0)
