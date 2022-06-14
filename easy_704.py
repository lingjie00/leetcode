from typing import List


# python solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        return -1


# algorithm solution
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1
        # binary search
        while left <= right:
            # pivot at the center
            pivot = left + (right - left) // 2
            # stop if the pivot is the target
            if nums[pivot] == target:
                return pivot
            # if target is smaller than pivot
            # search the left of the pivot
            if target < nums[pivot]:
                right = pivot - 1
            # else search right of the pivot
            else:
                left = pivot + 1
        return -1
