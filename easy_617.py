from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self,
                   root1: Optional[TreeNode],
                   root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # dummy node
        dummy = TreeNode()
        # depth first search
        stack = [(dummy, "left", root1, root2)]
        while stack:
            parent, position, node1, node2 = stack.pop(-1)

            # skip if both are not nodes
            if node1 is None and node2 is None:
                continue

            # create new node
            val1 = node1.val if node1 else 0
            val2 = node2.val if node2 else 0
            newNode = TreeNode(val1+val2)
            if position == "left":
                parent.left = newNode
            else:
                parent.right = newNode

            # add to stack
            if node1 is not None or node2 is not None:
                stack += [(newNode, "left",
                           node1.left if node1 else None,
                           node2.left if node2 else None),
                          (newNode, "right",
                              node1.right if node1 else None,
                              node2.right if node2 else None)]

        return dummy.left


if __name__ == "__main__":
    root1 = TreeNode(val=1,
                     left=TreeNode(val=3, left=TreeNode(5)),
                     right=TreeNode(val=2))

    root2 = TreeNode(val=2,
                     left=TreeNode(1, right=TreeNode(4)),
                     right=TreeNode(3, right=TreeNode(7)))

    result = Solution().mergeTrees(root1, root2)

    print(result)
