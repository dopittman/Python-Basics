# Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order,
# find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1]
# and numbers[index2] where 1 <= index1 < index2 <= numbers.length

# Example 1
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

# Example 3
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

test1 = [2,7,11,15]
test2 = [2,3,4]
test3 = [-1,0]


# Runtime: 64 ms, faster than 76.30%

def run(nums, target):
    left = 0
    right = len(nums) -1

    while left < right:
        total_value = nums[left] + nums[right]

        if total_value == target:
            # +1 due to the answer required being the index + 1
            return left + 1, right + 1
        #  if total value is higher than the target, reduce the right index by 1
        if total_value > target:
            right -= 1
        #  if total value is lower than the target, increase the left index by 1
        else:
            left += 1

    return(-1,-1)


print(run(test1, 9))