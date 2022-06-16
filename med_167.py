from typing import List

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # using two pointer approach
        # first pointer starts from left
        # second pointer starts from right
        # if sum is smaller, advance left pointer
        # if sum if larger, advance right pointer

        left, right = 0, len(numbers) - 1

        while left <= right:

            total = numbers[left] + numbers[right]
            
            if total == target:
                return [left+1, right+1]
            elif total < target:
                left += 1
            else:
                right -= 1


if __name__ == "__main__":
    numbers = [2, 7, 11, 15]
    ans = Solution().twoSum(numbers, 9)
    print(ans)
