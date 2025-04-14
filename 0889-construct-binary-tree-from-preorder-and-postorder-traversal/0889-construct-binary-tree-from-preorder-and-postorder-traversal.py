# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def constructFromPrePost(self, preorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        # preorder -> node left right
        # postorder -> left right node
        # left랑 right를 어떻게 나누지
        # pre에서 i=1이 left child, post에서 i=-2가 right child.
        # 둘이 같으면 자식이 하나밖에 없는 것. left인지 right인지는 구분 불가.
        # 만약 다르면? 같은 값을 찾아가야 할 것 같은데
        # 예시에서 pre i=1이 2, post i=-2가 3. 다르다.
        # 그럼 left는 2이고 right는 3.
        # left subtree는 pre에서 2부터 시작해서 3 전까지, post에서 2를 찾으면 거기서부터 왼쪽 쭉
        # right subtree는 pre에서 3부터 시작해서 뒤로 쭉. post에서 2 전까지.
        # 이걸 반복하면 되지 않을까?

        def build(pre, post):
            if not pre:
                return None
            
            node = TreeNode(val=pre[0])
            if len(pre) == 1:
                return node
            
            left_val, right_val = pre[1], post[-2]
            if left_val == right_val:
                node.left = build(pre[1:], post[:-1])
            else:
                node.left = build(pre[1 : pre.index(right_val)], post[ : post.index(left_val) + 1])
                node.right = build(pre[pre.index(right_val) : ], post[post.index(left_val) + 1 : -1])
            
            return node

        return build(preorder, postorder)