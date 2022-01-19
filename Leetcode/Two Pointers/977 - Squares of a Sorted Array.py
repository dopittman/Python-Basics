
# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

# Example 1
# Input: nums = [-4,-1,0,3,10]
# Output: [0,1,9,16,100]
# Explanation: After squaring, the array becomes [16,1,0,9,100].
# After sorting, it becomes [0,1,9,16,100].

# Example 2
# Input: nums = [-7,-3,2,3,11]
# Output: [4,9,9,49,121]

test = [-13, -5, -1, 3, 6, 15]
test2 = [-4,-1,0,3,10]
test3 = [-7,-3,2,3,11]


def run(my_list):
    n = len(my_list)
    result = [0] * n
    left_pointer = 0
    right_pointer = n - 1

    for i in range(n - 1, -1, -1):
        if abs(my_list[left_pointer]) < abs(my_list[right_pointer]):
            square = my_list[right_pointer]
            result[i] = square * square
            right_pointer -= 1
        else:
            square = my_list[left_pointer]
            result[i] = square * square
            left_pointer += 1
    return result


print(run([1]))

