from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # using binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # check if pivot is target
            if nums[pivot] == target:
                return pivot

            # edge case:
            # when pivot is index 0 and last index
            if pivot == 0:
                if nums[pivot] > target:
                    return pivot
                else:
                    return pivot + 1

            # if target is smaller than pivot
            # continue search to left
            if nums[pivot] > target:
                right = pivot - 1
                # if target is bigger than pivot - 1
                # then target is not in nums and should be
                # insert in pivot
                if target > nums[right]:
                    return right + 1
            # if target is larger than pivot
            # continue search to right
            elif nums[pivot] < target:
                left = pivot + 1
                if left == len(nums):
                    return left
                # if target is smaller than pivot + 1
                # then target is not in nums and should be
                # insert in pivot + 1
                if target < nums[left]:
                    return left

        return -1


# simplier method: just return the left if target not found
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # using binary search
        left, right = 0, len(nums) - 1
        while left <= right:
            pivot = left + (right - left) // 2
            # check if pivot is target
            if nums[pivot] == target:
                return pivot

            # if target is smaller than pivot
            # continue search to left
            if nums[pivot] > target:
                right = pivot - 1
            # if target is larger than pivot
            # continue search to right
            elif nums[pivot] < target:
                left = pivot + 1

        return left
