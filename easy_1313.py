from typing import List
import logging

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def decompressRLElist(self, nums: List[int]) -> List[int]:
        result = []
        for freq, val in zip(nums[:-1:2], nums[1::2]):
            logging.debug((freq, val))
            result += [val] * freq
        return result


def main():
    questions = ([1, 2, 3, 4], [1, 1, 2, 3])
    solutions = ([2, 4, 4, 4], [1, 3, 3])
    for num, correct in zip(questions, solutions):
        sol = Solution().decompressRLElist(num)
        try:
            assert sol == correct
            print("Right solution")
        except Exception:
            print(f"Wrong solution: {sol=}")


if __name__ == "__main__":
    main()
