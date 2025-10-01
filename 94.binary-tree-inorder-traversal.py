from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []

        def traverse(root: Optional[TreeNode]):
            if not root:
                return

            nonlocal res

            traverse(root.left)
            res.append(root.val)
            traverse(root.right)

        traverse(root)

        return res
