import logging

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        prod, sum = 1, 0
        tail, n = n % 10, n // 10
        while tail != 0 or n != 0:
            # continue while loop until no more digits left
            logging.debug(f"{tail=}; {n=}")
            prod *= tail
            sum += tail
            tail, n = n % 10, n // 10
        logging.debug(f"{prod=}; {sum=}")
        return prod - sum


def main():
    inputs = (234, 4421)
    outputs = (15, 21)

    for questions, ans in zip(inputs, outputs):
        sol = Solution().subtractProductAndSum(questions)
        try:
            assert ans == sol
            print("Correct solution")
        except AssertionError:
            print(f"Wrong: {questions=}; {sol=}; {ans=}")


if __name__ == "__main__":
    main()
