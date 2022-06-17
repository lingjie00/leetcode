class Solution:
    def reverseWords(self, s: str) -> str:
        # p1 stays at the start of the word
        # p2 points to the end of the word
        result = ""
        p1, p2 = 0, 0
        while p1 < len(s):

            # start reversing if
            # p2 points to a blank
            # p2 points to the end of the word
            if s[p2] == " " or p2 == len(s) - 1:

                space = p2

                if s[space] == " ":
                    p2 -= 1

                while p1 <= p2:

                    result += f"{s[p2]}"

                    p2 -= 1

                if s[space] == " ":
                    result += " "
                p1 = space + 1
                # p2 will always add 1
                p2 = space

            p2 += 1

        return result

class Solution:
    # alternatively, store the reverse in the string itself
    # but does not reduce the space complexity
    def reverseWords(self, s: str) -> str:
        # p1 stays at the start of the word
        # p2 points to the end of the word
        sLen = len(s)
        p1, p2 = 0, 0
        while p1 < sLen:

            # start reversing if
            # p2 points to a blank
            # p2 points to the end of the word
            if s[p2] == " " or p2 == sLen - 1:

                space = p2

                if s[space] == " ":
                    p2 -= 1

                while p1 <= p2:

                    s += f"{s[p2]}"

                    p2 -= 1

                if s[space] == " ":
                    s += " "
                p1 = space + 1
                # p2 will always add 1
                p2 = space

            p2 += 1

        return s[sLen:]

if __name__ == "__main__":
    s = "Let's take LeetCode contest"
    print(f"{s=}")
    result = Solution().reverseWords(s)
    print(f"{result=}")
