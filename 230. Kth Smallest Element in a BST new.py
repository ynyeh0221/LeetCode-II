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
        self.res = None
        self.find(root)
        return self.res
        
    def find(self, root):
        if not root:
            return
        if not self.res:
            self.find(root.left)
            self.k -= 1
            if self.k == 0:
                self.res = root.val
                return
            self.find(root.right)
