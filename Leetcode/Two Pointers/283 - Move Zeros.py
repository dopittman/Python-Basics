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

test = [0, 1, 0, 3, 12]

def run(list):
    left = 0
    right = 0
    n = len(list)
    num_of_zeros = 0

    for i in range(n):
        if list[right] != 0:
            list[left] = list[i]
            right += 1
            left += 1
        elif list[i] == 0:
            num_of_zeros += 1
            right +=1

    for i in range(n - num_of_zeros, n, 1):
        list[i] = 0

    return list

print(run(test))