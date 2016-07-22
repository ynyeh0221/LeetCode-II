# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        if not root.left and not root.right:
            return 1
        l = self.minDepth(root.left)
        r = self.minDepth(root.right)
        if l > 0 and r > 0:
            return min(l, r) + 1
        elif l > 0 and r == 0:
            return l + 1
        else:
            return r + 1
