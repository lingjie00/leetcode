# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def getTargetCopy(self,
                      original: TreeNode, cloned: TreeNode,
                      target: TreeNode) -> TreeNode:
        # traversal in the original tree for target
        def inorder(o: TreeNode, c: TreeNode):
            if o:
                inorder(o.left, c.left)
                if o is target:
                    self.result = c
                inorder(o.right, c.right)

        inorder(original, cloned)
        # return the reference in cloned tree
        return self.result
