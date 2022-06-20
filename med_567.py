import logging

# approach:
# first keep the count of the chars in s1
# starting with a window size equal to the length of s1
# check the char count in s1 that is contained in the window
# expand the window until the full s2 is contained
# while expanding, subtract the count from s1

logging.basicConfig(level=logging.DEBUG)


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        def checkSum():
            currSum = 0
            for i in range(26):
                if orCharCount[i] > 0:
                    currSum += max(0, charCount[i])
            return currSum <= 0

        # edge case
        if len(s1) > len(s2):
            return False

        # keep a frequency count of chars in s1
        charCount = [0] * 26
        for c in s1:
            index = ord(c) % ord("a")
            charCount[index] += 1

        logging.debug(f"{charCount=}")
        orCharCount = charCount.copy()
        # first sliding window
        winSize = len(s1)

        for i in range(0, winSize):
            index = ord(s2[i]) % ord("a")
            charCount[index] = charCount[index] - 1

        if checkSum():
            return True

        logging.debug(f"{orCharCount=}")
        logging.debug(f"{charCount=}")

        # remaining sliding window
        # concern about two points:
        # the starting to remove
        # the new point to add
        start, new = 0, winSize

        logging.debug(f"{new=}, {len(s2)=}")

        while new < len(s2):

            addIndex = ord(s2[start]) % ord("a")
            if orCharCount[addIndex] > 0:
                charCount[addIndex] += 1
                logging.debug(
                        f"start char={s2[start]} count={charCount[addIndex]}")

            subIndex = ord(s2[new]) % ord("a")
            charCount[subIndex] -= 1

            logging.debug(f"{(start, new)}, {s2[start], s2[new]}, {charCount}")
            start += 1
            new += 1

            if checkSum():
                logging.debug("still here")
                return True

        return False


if __name__ == "__main__":
    s1 = "ab"
    s2 = "eidbaooo"
    result = Solution().checkInclusion(s1, s2)
    logging.info(f"expected=true, {result=}")

    s1 = "ab"
    s2 = "eidboaooo"
    result = Solution().checkInclusion(s1, s2)
    logging.info(f"expected=false, {result=}")

    s1 = "adc"
    s2 = "dcda"
    result = Solution().checkInclusion(s1, s2)
    logging.info(f"expected=true, {result=}")

    s1 = "hello"
    s2 = "ooolleoooleh"
    result = Solution().checkInclusion(s1, s2)
    logging.info(f"expected=false, {result=}")
