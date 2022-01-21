# Given an integer array nums, return true if any value appears at least
# twice in the array, and return false if every element is distinct.

# Example 1

# Input: nums = [1,2,3,1]
# Output: true


# Example 2

# Input: nums = [1,2,3,4]
# Output: false


# Example 3

# Input: nums = [1,1,1,3,3,4,3,2,4,2]
# Output: true

test = [1,2,3,4,6,7,7,5]
newtest = [4,4]
false_test = [1,2,3,4]

# My first solution: O(n) Runtime
# Adds elements to a hashmap if they are not already contained in it,
# If the element does have its value already in the hashmap return true

def run(nums):
    h_map = {}
    for i in range(len(nums)):
        if nums[i] in h_map.values():
            return True
        else:
            h_map[i] = nums[i]
    return False

# Create a python set, then compare the length of the set against the length of the original list
# a set is a list of all numbers minus any duplicates
# ie. set([1,2,3,3,4]) = [1,2,3,4]

def set_solution(nums):
    numsSet = set(nums)
    # The length of nums will be 1 more than the set if there is a duplicate value
    if len(nums) == len(numsSet):
        return False
    return True

# One Line solution, still O(n) runtime
def one_line_solution(nums):
    return len(nums) > len(set(nums))

print(one_line_solution(newtest))