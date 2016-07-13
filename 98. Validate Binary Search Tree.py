# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        self.res = True
        self.inorder(root, [])
        return self.res
    
    def inorder(self, root, nums):
        if not root:
            return
        if self.res:
            self.inorder(root.left, nums)
            if not nums or (nums and root.val > nums[len(nums)-1]):
                nums += [root.val]
            else:
                self.res = False
            self.inorder(root.right, nums)
