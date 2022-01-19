from typing import List

# Given an array, rotate the array to the right by k steps, where k is non-negative.

# Example 1

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]

# Example 2

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation:
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

# My first solution

#
# def run(nums, k):
#     left = 0
#     right = len(nums) - k
#     result = [0] * len(nums)
#     count = 0
#
#     for i in range(right, len(nums)):
#         result[count] = nums[right]
#         count += 1
#         right += 1
#
#     for i in range(left, k + 1):
#         result[count] = nums[i]
#         count += 1
#         left += 1
#
#     nums = result
#     return nums

test = [1, 2, 3, 4, 5, 6, 7]


def reverse(nums: list, start: int, end: int) -> None:
    while start < end:
        print(nums)
        # This is a Python way to swap indices without a temp variable
        # nums[start], nums[end] = nums[end], nums[start]

        # Create a temp var to hold original start value
        temp = nums[start]
        # Swap the values from start and end indices
        nums[start] = nums[end]
        nums[end] = temp
        # increment start index, decrement end index
        start += 1
        end -= 1


def rotate(nums: List[int], k: int):

    n = len(nums)
    # k % n  will return the minimum number of rotations needed, ie n = 6, k = 4 is the same as n = 6, k = 10
    #  4 % 6 = 4 and 10 % 6 = 4
    k %= n

    # 1st step reverses the entire array ie [1,2,3,4,5] -> [5,4,3,2,1]
    reverse(nums, 0, n - 1)
    # 2nd step reverses 0 -> k-1 indices ie. [5,4,3,2,1] -> [3,4,5,2,1]
    reverse(nums, 0, k - 1)
    # Last step reverses k -> n-1 indices ie [3,4,5,2,1] -> [3,4,5,1,2]
    reverse(nums, k, n - 1)

rotate(test, 3)

print(test)

