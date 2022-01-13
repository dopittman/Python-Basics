from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left_pointer = 0
        right_pointer = len(nums)

        while left_pointer < right_pointer:
            mid_idx = (left_pointer + right_pointer) // 2
            mid_val = nums[mid_idx]

            if mid_val == target:
                return mid_idx
            if mid_val > target:
                right_pointer = mid_idx
            if mid_val < target:
                left_pointer = mid_idx + 1
        return -1


testList = [1, 2, 3, 4, 5, 6, 7, 8, 9]
test = Solution()

print(test.search(testList, 4))

