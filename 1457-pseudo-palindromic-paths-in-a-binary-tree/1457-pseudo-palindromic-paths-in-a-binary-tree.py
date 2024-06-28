# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        # palindrome은 모두 짝수개이거나 1개만 홀수이면 된다.
        # val 범위가 1~9니까 hashmap 써도 될듯
        # 그러면 dfs를 돌려서...
        # leaf에 도착하면 슥 확인하면 되나? 이것도 10개가 최대니까 그냥 확인하면 되지 않을까?
        dt = collections.defaultdict(int)

        def is_pseudo_palindrome():
            odd_number_count = 0
            for i in range(1, 10):
                if dt[i] % 2 == 1:
                    odd_number_count += 1
                    if odd_number_count >= 2:
                        return False
            return True

        def dfs(node):
            dt[node.val] += 1
            count = 0

            if not node.left and not node.right: # leaf
                count = 1 if is_pseudo_palindrome() else 0
            else:
                left = dfs(node.left) if node.left else 0
                right = dfs(node.right) if node.right else 0
                count = left + right

            dt[node.val] -= 1

            return count
        
        return dfs(root)