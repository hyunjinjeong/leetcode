# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        # backtracking 해서 하나씩 보면 되려나?

        def is_smaller(arr1, arr2):
            if not arr2:
                return True

            i, j = 0, 0
            while i < len(arr1) and j < len(arr2):
                c1, c2 = arr1[i], arr2[j]
                if c1 < c2:
                    return True
                if c1 > c2:
                    return False
                i += 1
                j += 1
            
            return len(arr1) < len(arr2)

        def dfs(node, arr):
            arr.append(chr(ord('a') + node.val))

            if node.left and node.right:
                dfs(node.left, arr)
                dfs(node.right, arr)
            elif node.left:
                dfs(node.left, arr)
            elif node.right:
                dfs(node.right, arr)
            else:
                reversed_arr = list(reversed(arr))
                if is_smaller(reversed_arr, self.smallest):
                    self.smallest = reversed_arr[:]
            
            arr.pop()

        self.smallest = []
        dfs(root, [])
        return "".join(self.smallest)