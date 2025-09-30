from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    diameter = 0

    def dfs(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left = self.dfs(root.left)
        right = self.dfs(root.right)
        d = left + right

        self.diameter = max(self.diameter, d)

        return max(left, right) + 1

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.dfs(root)
        return self.diameter
