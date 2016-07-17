class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.count = 1

class Solution(object):
    def countSmaller(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        res = [0]
        root = TreeNode(nums[len(nums) - 1])
        for i in xrange(len(nums)-2, -1, -1):
            res += [self.insert(root, nums[i])];
        return res[::-1]
    
    def insert(self, root, x):
        count = 0
        while True:
            if x <= root.val:
                root.count += 1
                if not root.left:
                    root.left = TreeNode(x)           
                    break
                else:
                    root = root.left
            else:
                count += root.count
                if not root.right:
                    root.right = TreeNode(x)           
                    break
                else:
                    root = root.right
        return count
