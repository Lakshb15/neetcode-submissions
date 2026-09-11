# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        inMap = {val: idx for idx, val in enumerate(inorder)}
        q = collections.deque(preorder)
        
        def build(start, end):
            if start > end:
                return 

            root = q.popleft()

            node = TreeNode(root)

            root_idx = inMap[root]

            node.left = build(start, root_idx - 1)
            node.right = build(root_idx + 1, end)

            return node
        return build(0, len(preorder) - 1)