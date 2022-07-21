# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def find_path(node, target, path):
            nonlocal result
            if node == target:
                result = path.copy()
                return 1
            if node.left:
                v = find_path(node.left, target, path + [node.left])
                if v:
                    return 1
            if node.right:
                v = find_path(node.right, target, path + [node.right])
                if v:
                    return 1
                
            return 0
        
        result = []
        find_path(root, p, [root])
        path1 = result.copy()
        
        result = []
        find_path(root, q, [root])
        path2 = result.copy()
        
        lca = None
        for u, v in range(path1, path2):
            if u != v:
                break
            lca = u
        return lca
            
        
         