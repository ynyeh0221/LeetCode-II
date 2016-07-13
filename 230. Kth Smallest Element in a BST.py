# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def kthSmallest(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: int
        """
        self.k = k
        return self.find(0, root)
        
    def find(self, res, root):
        if not root:
            return res
        res = self.find(res, root.left)
        self.k -= 1
        if self.k == 0:
            return root.val
        res = self.find(res, root.right)
        return res
