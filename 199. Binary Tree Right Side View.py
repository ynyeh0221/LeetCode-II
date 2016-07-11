# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        self.res = []
        self.helper(root, 0)
        return self.res
        
    def helper(self, root, level):
        if not root:
            return
        if len(self.res) == level:
            self.res += [root.val]
        self.helper(root.right, level+1)
        self.helper(root.left, level+1)
