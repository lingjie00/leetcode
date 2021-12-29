from typing import List
import logging

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        words = list(map(lambda x: len(x.split()), sentences))
        logging.debug(words)
        return max(words)


def main():
    sen1 = ["alice and bob love leetcode",
            "i think so too", "this is great thanks very much"]
    sol1 = Solution().mostWordsFound(sen1)
    logging.info(sol1)
    assert sol1 == 6

    sen2 = ["please wait", "continue to fight", "continue to win"]
    sol2 = Solution().mostWordsFound(sen2)
    logging.info(sol2)
    assert sol2 == 3


if __name__ == "__main__":
    main()
