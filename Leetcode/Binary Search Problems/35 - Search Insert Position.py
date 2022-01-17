from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # Set pointers
        low, high = 0, len(nums)
        # Set condition for while loop
        while low < high:
            # Set mid_index
            mid = (low + high) // 2
            # if target is > mid_idx value move left pointer
            if target > nums[mid]:
                low = mid + 1
            else:
                # if target is less than mid_idx value
                high = mid
        return low