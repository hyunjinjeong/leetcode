# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # level 별로 가장 오른쪽에 있는 노드를 보여주면 된다!
        # 그러면 어떻게.. level-order traversal 한 다음에 가장 오른쪽에 있는 걸 찾으면 되지 않을까.
        def traverse(node, level):
            if not node:
                return
            
            if len(levels) <= level:
                levels.append([])
            
            levels[level].append(node.val)
            traverse(node.right, level+1)
            traverse(node.left, level+1)
            
        levels = []
        traverse(root, 0)
        
        ans = []
        for level in levels:
            ans.append(level[0])
        
        return ans