# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

def isBadVersion(version: int) -> bool:
    return True


class Solution:
    def firstBadVersion(self, n: int) -> int:
        # using binary search
        # find the version where current version is good
        # but the next version is bad
        left, right = 0, n
        while left <= right:
            pivot = left + (right - left) // 2
            # if current version is bad version
            # continue search to the left
            if isBadVersion(pivot):
                right = pivot - 1
            # if current version is good version
            # and the next version is bad version
            # then we have the next version as what we want
            elif isBadVersion(pivot + 1):
                return pivot + 1
            # else continue search to the right
            else:
                left = pivot + 1
