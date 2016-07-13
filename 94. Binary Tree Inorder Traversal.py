# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        res = []
        stack = [root]
        while stack:
            while root and root.left:
                stack += [root.left]
                root = root.left
            root = stack.pop()
            res += [root.val]
            if root.right:
                stack += [root.right]
            root = root.right
        return res
