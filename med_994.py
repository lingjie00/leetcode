from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        time = -1
        rottenList = set()

        if not grid:
            return -1

        maxX, maxY = len(grid[0]), len(grid)

        nonRotten = False
        for x in range(maxX):
            for y in range(maxY):
                if grid[y][x] == 2:
                    rottenList.add((x, y))
                elif grid[y][x] == 1:
                    nonRotten = True

        if not rottenList:
            return -1

        while nonRotten:

            print(f"{grid=}")
            nonRotten = False
            # 1 min later
            time += 1

            newRottenList = set()

            print(f"{rottenList}")
            for x, y in rottenList:

                if 0 < x < maxX - 1 and 0 < y < maxY - 1:
                    # able to go 4 directions
                    if grid[x][y+1] == 1:
                        newRottenList.add((x, y+1))
                    if grid[x][y-1] == 1:
                        newRottenList.add((x, y+1))
                    if grid[x+1][y] == 1:
                        newRottenList.add((x+1, y))
                    if grid[x-1][y] == 1:
                        newRottenList.add((x+1, y))
                elif x == 0:
                    if grid[x+1][y] == 1:
                        newRottenList.add((x+1, y))
                    if y == 0:
                        # only right and down
                        if grid[x][y+1] == 1:
                            newRottenList.add((x, y+1))
                    elif y == maxY - 1:
                        # only right and up
                        if grid[x][y-1] == 1:
                            newRottenList.add((x, y-1))
                elif x == maxX - 1:
                    if grid[x-1][y] == 1:
                        newRottenList.add((x-1, y))
                    if y == 0:
                        # only left and down
                        if grid[x][y+1] == 1:
                            newRottenList.add((x, y+1))
                    elif y == maxY - 1:
                        # only left and up
                        if grid[x][y-1] == 1:
                            newRottenList.add((x, y+1))

            if len(newRottenList) > 0:
                nonRotten = True

            for x, y in list(newRottenList):
                grid[x][y] = 2

            rottenList = rottenList.union(newRottenList)

        return time


if __name__ == "__main__":
    grid = [[2, 1, 1], [1, 1, 0], [0, 1, 1]]
    solution = Solution().orangesRotting(grid)
    print(solution)
