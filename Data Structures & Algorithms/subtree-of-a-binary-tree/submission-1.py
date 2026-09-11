# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        
        # If subRoot is empty, it is always a subtree
        if subRoot is None:
            return True
        
        # If root is empty but subRoot isn't
        if root is None:
            return False
        
        # Check if the trees are identical starting at these nodes
        if self.sameTree(root, subRoot):
            return True
        
        # Search in the left and right subtrees
        return (
            self.isSubtree(root.left, subRoot) or
            self.isSubtree(root.right, subRoot)
        )

    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        
        if p is None or q is None:
            return False
        
        if p.val != q.val:
            return False
        
        return (
            self.sameTree(p.left, q.left) and
            self.sameTree(p.right, q.right)
        )
        
        
        
        