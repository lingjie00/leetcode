from typing import Optional


class Node:
    def __init__(self,
                 val: int = 0,
                 left: 'Node' = None,
                 right: 'Node' = None,
                 next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # using stack to store the data
        stack = [root]

        # search
        while stack:
            node = stack.pop(-1)

            if not node:
                continue

            if node.left:
                node.left.next = node.right

                stack += [node.left]

            if node.right:
                if node.next:
                    node.right.next = node.next.left

                stack += [node.right]

        return root


if __name__ == "__main__":
    root = Node(val=1,
                left=Node(2, left=Node(4), right=Node(5)),
                right=Node(3, left=Node(6), right=Node(7)))

    result = Solution().connect(root)
