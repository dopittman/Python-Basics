# Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]

# Example 2

# Input: nums = [0]
# Output: [0]

# My First Solution:
# Runtime: 176 ms, faster than 59.98% of Python3 online submissions for Move Zeroes.
# Memory Usage: 15.3 MB, less than 91.04% of Python3 online submissions for Move Zeroes.

test = [0, 11, 0, 3, 12]

def run(list):
    left = 0
    n = len(list)
    num_of_zeros = 0

    # i works a the right pointer
    for i in range(n):
        if list[i] != 0:
            list[left] = list[i]
            left += 1
        elif list[i] == 0:
            num_of_zeros += 1

    for i in range(n - num_of_zeros, n, 1):
        list[i] = 0

    return list


# an optimal python solution
# Has same runtime as mine technically but contains one less loop and less code
def move_zeroes(nums):
    slow = 0
    for fast in range(len(nums)):
        if nums[fast] != 0 and nums[slow] == 0:
            nums[slow], nums[fast] = nums[fast], nums[slow]

        # wait while we find a non-zero element to
        # swap with you
        if nums[slow] != 0:
            slow += 1
    return nums


print(run(test))
