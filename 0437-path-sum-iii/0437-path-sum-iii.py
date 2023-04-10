# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
#         # 뭔가 자식 tree를 어떻게 재활용할 수 있을 것 같은디
#         # 일단 brute force 버전. 공간은 O(n) 시간은 O(n^2).
#         def dfs(node):
#             if not node:
#                 return
            
#             validate(node, 0)
#             dfs(node.left)
#             dfs(node.right)
            
#         def validate(node, curr_sum):
#             if not node:
#                 return
            
#             if curr_sum + node.val == targetSum:
#                 self.ans += 1
            
#             validate(node.left, curr_sum + node.val)
#             validate(node.right, curr_sum + node.val)
            
#         self.ans = 0
#         dfs(root)
#         return self.ans

        # 다음으론 개선된 버전.. two sum 아이디어 활용.. 공간 O(N) 시간 O(N)
        def dfs(node, curr_sum):
            if not node:
                return
            
            new_sum = curr_sum + node.val
            if new_sum == targetSum:
                self.ans += 1
            # 예를 들어 1->2->3 상황에서 curr_sum 3, node.val 3이고 target이 3이라면 3이 cache에 있는지 찾는 거.
            self.ans += self.count[new_sum - targetSum]
            
            self.count[new_sum] += 1
            
            dfs(node.left, new_sum)
            dfs(node.right, new_sum)
            # backtracking. 현재 node에서 벗어나면 count 하나 빼줌.
            self.count[new_sum] -= 1
        
        self.ans = 0
        self.count = collections.defaultdict(int)
        dfs(root, 0)
        return self.ans