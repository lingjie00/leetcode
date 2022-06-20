from typing import List


class Solution:
    def floodFill(self,
                  image: List[List[int]],
                  sr: int, sc: int, color: int) -> List[List[int]]:
        # if starting pixel is the same as color, no change
        if image[sr][sc] == color:
            return image

        # do a breath first search
        queue = []
        seen = {}
        # start from the initial pixel
        queue.append((sr, sc))
        # repeat procedure until all pixel has been changed
        while queue:
            # change the current pixel color
            sr, sc = queue.pop(0)
            currColor = image[sr][sc]
            image[sr][sc] = color
            seen[(sr, sc)] = 1

            # check 4 directions (up down left right)
            if sc + 1 < len(image[sr]):
                # right
                if image[sr][sc+1] == currColor\
                        and (sr, sc+1) not in seen:
                    queue.append((sr, sc+1))

            if sc - 1 >= 0:
                # left
                if image[sr][sc-1] == currColor\
                        and (sr, sc-1) not in seen:
                    queue.append((sr, sc-1))

            if sr + 1 < len(image):
                # down
                if image[sr + 1][sc] == currColor\
                        and (sr + 1, sc) not in seen:
                    queue.append((sr+1, sc))

            if sr - 1 >= 0:
                # up
                if image[sr-1][sc] == currColor\
                        and (sr-1, sc) not in seen:
                    queue.append((sr-1, sc))

        return image


if __name__ == "__main__":
    image = [[1, 1, 1], [1, 1, 0], [1, 0, 1]]
    print(f"{image=}")
    sr, sc, color = 1, 1, 2
    result = Solution().floodFill(image, sr, sc, color)
    print(f"sr, sc, color = {sr, sc, color}\n{result=}")
