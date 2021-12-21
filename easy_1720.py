from typing import List
import logging

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def decode(self, encoded: List[int], first: int) -> List[int]:
        result = [first]
        for index, value in enumerate(encoded):
            new_value = value ^ result[index]
            logging.debug(f"{value=}; {result[index]=}; {new_value=}")
            result.append(new_value)
        return result


def main():
    inputs = (
        ([1, 2, 3], 1),
        ([6, 2, 7, 3], 4)
    )
    outputs = ([1, 0, 2, 1], [4, 2, 0, 7, 4])

    for input, output in zip(inputs, outputs):
        encoded, first = input
        sol = Solution().decode(encoded, first)
        try:
            assert sol == output
        except AssertionError:
            print(f"{input=}; {sol=}; {output=}")


if __name__ == "__main__":
    main()
