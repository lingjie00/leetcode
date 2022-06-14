class Solution:
    def minPartitions(self, n: str) -> int:
        # actually, it is as simple as finding the max
        # integer among the values
        return int(max(list(n)))
