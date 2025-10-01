from typing import Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(
        self, root: Optional[TreeNode], p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root or not p or not q:
            return None

        cur = root

        while cur:
            if max(p.val, q.val) < cur.val:
                cur = cur.left
            elif min(p.val, q.val) > cur.val:
                cur = cur.right
            else:
                return cur
