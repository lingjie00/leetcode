from Typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deepestLeavesSum(self, root: Optional[TreeNode]) -> int:

        # storing the 1. depth of tree 2. sum of deepest leaves
        self.depth = 0
        self.leaveSum = 0

        # find the depth of the tree
        def depth(node: TreeNode):
            if not node:
                return 0
            leftHeight = depth(node.left)
            rightHeight = depth(node.right)
            return max(leftHeight, rightHeight) + 1

        self.depth = depth(root)

        # iterate through the tree to find the deepest leaves
        def find(node: TreeNode, curr_depth: int):
            if node:
                find(node.left, curr_depth + 1)

                if curr_depth == self.depth:
                    self.leaveSum += node.val

                find(node.right, curr_depth + 1)

        find(root, 1)

        # return the sum
        return self.leaveSum
