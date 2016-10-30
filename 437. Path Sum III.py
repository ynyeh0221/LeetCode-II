# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: int
        """
        if not root:
            return 0
        self.res = 0
        self.dfs(root, sum, [])
        return self.res
        
    def dfs(self, root, s, path):
        if not root:
            return
        for i in xrange(len(path)):
            path[i] += root.val
        path += [root.val]
        for i in path:
            if i == s:
                self.res += 1
        self.dfs(root.left, s, path)
        self.dfs(root.right, s, path)
        path.pop()
        for i in xrange(len(path)):
            path[i] -= root.val
