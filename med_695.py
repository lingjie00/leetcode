from typing import List

# proposal:
# from a given starting point, start a depth first search to
# find out the land area connecting to the starting point
# iteratively search the entire grid, skipping those
# coordinate that has been explored


class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # record coordinates that have been explored
        seen = {}
        maxSize = 0
        W, L = len(grid[0]), len(grid)

        def search(x: int, y: int) -> int:
            size = 0
            # edge case: starting guess is not island
            if grid[y][x] == 0:
                return 0
            stack = [(x, y)]
            # print(f"starting = {x, y}")
            while stack:
                x, y = stack.pop(-1)
                seen[(x, y)] = 1

                if x-1 >= 0:
                    if grid[y][x-1] != 0 and (x-1, y) not in seen:
                        seen[(x-1, y)] = 1
                        stack.append((x-1, y))

                if x+1 < W:
                    if grid[y][x+1] != 0 and (x+1, y) not in seen:
                        seen[(x+1, y)] = 1
                        stack.append((x+1, y))

                if y-1 >= 0:
                    if grid[y-1][x] != 0 and (x, y-1) not in seen:
                        seen[(x, y-1)] = 1
                        stack.append((x, y-1))

                if y+1 < L:
                    if grid[y+1][x] != 0 and (x, y+1) not in seen:
                        seen[(x, y+1)] = 1
                        stack.append((x, y+1))

                size += 1
                # print(f"{(x, y)} {size=} {stack=}")

            return size

        for y in range(len(grid)):
            for x in range(len(grid[0])):
                # only perform search on unexplored
                # coordinates
                if (x, y) not in seen:
                    size = search(x, y)
                    maxSize = max(size, maxSize)
                    # print((x, y, size, maxSize))

        return maxSize


if __name__ == "__main__":
    grid = [
        [0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
        [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    result = Solution().maxAreaOfIsland(grid)
    print(result)  # expect: 6

    grid = [
        [1, 1, 0, 0, 0],
        [1, 1, 0, 0, 0],
        [0, 0, 0, 1, 1],
        [0, 0, 0, 1, 1]]
    result = Solution().maxAreaOfIsland(grid)
    print(result)  # expect: 4
