from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # using two pointers
        # one points at the current number to square
        # another points at the placement of the squared
        p1, p2 = 0, 0
        array = []
        while p1 < len(nums):
            # squaring
            val = nums[p1] ** 2
            p1 += 1
            # placing
            if not array:
                array.append(val)
            else:
                # finding pointer 2 index
                while val < array[p2] and p2 >= 1:
                    p2 -= 1
                while val > array[p2] and p2 <= len(array) - 2:
                    p2 += 1
                # insert in position
                # check edge case of the last index
                if p2 == len(array) - 1 and val > array[-1]:
                    array.append(val)
                else:
                    array = array[:p2] + [val] + array[p2:]
        return array


# using the correct two pointers approach
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        # using two pointers
        # one pointer at the start
        # one pointer at the end
        start, end = 0, len(nums) - 1
        # store the results
        results = [None] * len(nums)
        resultIndex = len(nums) - 1
        while start <= end:
            if abs(nums[start]) <= abs(nums[end]):
                results[resultIndex] = nums[end] ** 2
                end -= 1
            else:
                results[resultIndex] = nums[start] ** 2
                start += 1
            resultIndex -= 1
        return results


if __name__ == "__main__":
    result = Solution().sortedSquares([-4, -1, 0, 3, 10])
    print(result)
