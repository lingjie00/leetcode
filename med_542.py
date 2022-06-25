from typing import List


# a challenge here is the minimum distance is order
# dependent. But iterating through the whole matrix twice
# will exceed the time limit (alternatively exceeding the
# memory limit if we initialise the stack with the whole
# matrix)
# solution: adding all the zeros to queue first
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        # keeping a stack
        # starting from coordinate x, y = 0, 0
        stack = []
        maxY, maxX = len(mat), len(mat[0])
        result = []
        for i in range(maxY):
            result += [[None] * maxX]

        for y in range(maxY):
            for x in range(maxX):
                if mat[y][x] == 0:
                    result[y][x] = 0
                    stack.append((x, y))

        while stack:
            x, y = stack.pop(0)

            # compute distance
            dist = float("inf")
            if mat[y][x] == 0:
                dist = 0

            if x > 0:
                if result[y][x-1] is not None:
                    dist = min(dist, result[y][x-1] + 1)
                else:
                    stack.append((x-1, y))

            if x < maxX - 1:
                if result[y][x+1] is not None:
                    dist = min(dist, result[y][x+1] + 1)
                else:
                    stack.append((x+1, y))

            if y > 0:
                if result[y-1][x] is not None:
                    dist = min(dist, result[y-1][x] + 1)
                else:
                    stack.append((x, y-1))

            if y < maxY - 1:
                if result[y+1][x] is not None:
                    dist = min(dist, result[y+1][x] + 1)
                else:
                    stack.append((x, y+1))

            if dist != float("inf") and dist != 0:
                result[y][x] = dist
            elif result[y][x] is None:
                stack.append((x, y))

        return result


if __name__ == "__main__":
    mat = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
    result = Solution().updateMatrix(mat)
    print(f"{mat=}, {result=}")

    mat = [[0, 0, 0], [0, 1, 0], [1, 1, 1]]
    result = Solution().updateMatrix(mat)
    print(f"{mat=}, {result=}")
