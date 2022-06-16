from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # using two pointers
        # one pointer pointing to the current index
        # one pointer pointing to the last known 0 place
        zeroPointer = 0
        curr = 0

        while curr < len(nums):

            if nums[curr] != 0:
                nums[curr], nums[zeroPointer] =\
                        nums[zeroPointer], nums[curr]
                zeroPointer += 1

            curr += 1


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # two pointer approach
        # first pointer keeps the current index
        # second pointer keeps the index of last known 0s
        # instead of swapping, change zero to all remaining entries
        curr, zeros = 0, 0
        while curr < len(nums):
            
            if nums[curr] != 0:
                nums[zeros] = nums[curr]
                zeros += 1

            curr += 1

        # now replace the remaining index with 0s
        while zeros < len(nums):
            nums[zeros] = 0
            zeros += 1

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        # count the numer of zeros
        # append the non-zero before zeros

        numZeros = 0
        result = []

        for item in nums:
            if item == 0:
                numZeros += 1
            else:
                result.append(item)

        result += [0] * numZeros

        # combine the results
        for i in range(len(nums)):
            nums[i] = result[i]


if __name__ == "__main__":
    nums = [0, 1, 0, 3, 12]
    print(f"array: {nums}")
    Solution().moveZeroes(nums)
    print(f"result: {nums}")

    nums = [1, 0]
    print(f"array: {nums}")
    Solution().moveZeroes(nums)
    print(f"result: {nums}")

    nums = [0, 1]
    print(f"array: {nums}")
    Solution().moveZeroes(nums)
    print(f"result: {nums}")

    nums = [4, 2, 4, 0, 0, 3, 0, 5, 1, 0]
    print(f"array: {nums}")
    Solution().moveZeroes(nums)
    print(f"result: {nums}")
