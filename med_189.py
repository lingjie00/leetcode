from typing import List


class Solution:
    # moving array by creating a temp array
    # time: O(n) to create array
    # space: O(n)
    def rotate(self, nums: List[int], k: int) -> None:
        # when there is no rotation
        # or the
        if k == 0 or len(nums) == 1 or k == len(nums):
            return nums
        k %= len(nums)
        tmp = nums[:-k]
        print(tmp)
        nums[:-k] = nums[-k:]
        nums[-k:] = tmp


class Solution:
    # moving array one by one
    # starting from the second last index to the last index
    # time: O(kn)
    # space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        k %= len(nums)
        for i in range(k):
            end = len(nums) - 1
            lastVal = nums[end]
            while end > 0:
                nums[end] = nums[end - 1]
                end -= 1
            nums[0] = lastVal


class Solution:
    # moving array one by one
    # differs from previous solution by moving by a jump of k
    # time: O(n)
    # space: O(1)
    def rotate(self, nums: List[int], k: int) -> None:
        k = k % len(nums)
        start, move = 0, 0
        while move < len(nums):
            # stores a temp value for next iteration
            current, val = start, nums[start]
            while True:
                # move val to k index later
                # stores the value of the index to be replaced
                nextIdx = (current + k) % len(nums)
                nums[nextIdx], val = val, nums[nextIdx]
                # following that move the next index
                current = nextIdx
                # terminate after complete iteration
                move += 1
                if current == start:
                    break
            start += 1


if __name__ == "__main__":
    array = [1, 2, 3, 4, 5, 6, 7]
    print(f"original: {array}")
    result = Solution().rotate(array, 3)
    print(array)
    # array = [-1, -100, 3, 99]
    # result = Solution().rotate(array, 2)
    # print(array)
    # array = [1]
    # print(f"original: {array}")
    # result = Solution().rotate(array, 0)
    # print(array)

    # array = [1, 2]
    # print(f"original: {array}")
    # result = Solution().rotate(array, 2)
    # print(array)
