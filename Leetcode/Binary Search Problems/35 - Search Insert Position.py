class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left_pointer = 0
        right_pointer = len(nums) - 1

        while left_pointer <= right_pointer:
            mid_idx = (left_pointer + right_pointer) // 2
            mid_val = nums[mid_idx]

            if mid_val == target:
                return mid_idx
            if mid_val < target:
                left_pointer = mid_idx + 1
            else:
                right_pointer = mid_idx - 1
        return left_pointer