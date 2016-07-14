# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param {TreeNode} root
    # @return {string[]}
    def binaryTreePaths(self, root):
        res = []
        self.findpath(res, [], root)
        return res
        
    def findpath(self, res, path, root):
        if not root:
            return
        if not root.left and not root.right:
            path += [root.val]
            res += ['->'.join(str(i) for i in path)]
            path.pop()
            return
        self.findpath(res, path + [root.val], root.left)
        self.findpath(res, path + [root.val], root.right)
