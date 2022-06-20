# keep an initial index
# while the character is not the same as the initial
# index, counter + 1
# if the character is the same as initial index,
# record the length and position, repeat for the
# next index
# time: O(n^2)
# space: O(1)

# modification:
# instead of restarting the counter, keep the window the
# same and continue the iteration instead
# time: O(n)
# space: O(1)
# However, this approach does not work because it does not
# check for the substring repetition (it only checks the
# starting and all the characters)

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        curr = 0
        counter = 1
        length = 0

        maxLength = 0
        maxStart = 0
        maxEnd = 0

        if len(s) == counter:
            return 1

        while counter < len(s):
            if length > maxLength:
                maxLength = length
                maxStart = curr
                maxEnd = counter

            if s[curr] != s[counter]:
                length += 1
            else:
                curr += 1

            counter += 1

        print(maxStart, maxEnd)
        print(s[maxStart:maxEnd])

        if maxLength == 0:
            return 1

        return maxLength


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # empty string
        if not s:
            return 0

        start = 0
        end = 0
        length = 1

        seen = {}

        while end < len(s):
            if s[end] in s[start:end]:
                start = max(start, seen[s[end]] + 1)

            length = max(length, end - start + 1)
            seen[s[end]] = end

            end += 1

        return length


if __name__ == "__main__":
    # s = "abcabcbb"
    # result = Solution().lengthOfLongestSubstring(s)
    # print(result)
    #
    # s = "bbbbb"
    # result = Solution().lengthOfLongestSubstring(s)
    # print(result)
    # s = "pwwkew"
    # result = Solution().lengthOfLongestSubstring(s)
    # print(result)
    s = "au"
    result = Solution().lengthOfLongestSubstring(s)
    print(result)
