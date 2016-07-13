# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []
        stack = [root]
        res = [root.val]
        while stack:
            while root and root.left:
                stack += [root.left]
                root = root.left
                res += [root.val]
            root = stack.pop()
            if root and root.right:
                stack += [root.right]
            root = root.right
            if root:
                res += [root.val]
        return res
