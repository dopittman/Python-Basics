# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> int:

# Sets the bad version and returns if a version is bad or not
def isBadVersion(version):
    if version < 1:
        return False
    else:
        return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # n = number of total versions
        left_pointer = 0
        right_pointer = n

        while left_pointer < right_pointer:
            mid_idx = (left_pointer + right_pointer) // 2

            # if bad version equals mid_idx then we know all to the right are bad as well
            if isBadVersion(mid_idx):
                # we now move right pointer to mid_idx and run the while loop again
                right_pointer = mid_idx
            else:
                # if mid_ix is not bad then we know all to the left are good and set the left_pointer to mid_idx + 1
                left_pointer = mid_idx + 1
        #  We return the left_pointer as it will equal the bad version once the loop is finished
        return left_pointer


test = Solution()
print(test.firstBadVersion(9))