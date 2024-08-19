# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, n: int) -> List[Optional[TreeNode]]:
        # dfs로 내려가면서 현재 갯수가 n개면 리턴하고
        # n개보다 크면 종료, n개보다 작으면 자식 2개 생성하면 되나?
        # 일단 갯수가 짝수개면 full이 안 되니까 거르고...
        # 분할정복을 적용할 수 있음
        @cache
        def make_full_binary(k):
            if k % 2 == 0:
                return []
            if k == 1:
                return [TreeNode(0)]

            # [1, 2, 3] [a, b, c]
            # 1 a, 1 b, 1 c
            # 2 a, 2 b, 2 c
            # 3 a, 3 b, 3 c
            
            # k == 5면?
            # 일단 본인이 있고... 왼쪽에 뭐가 붙을 수도 있고 오른쪽에 뭐가 붙을수도 있음

            # 7도 마찬가지고... 
            # 1. 왼쪽은 leaf, 오른쪽은 dfs
            # 2. 왼쪽은 dfs, 오른쪽이 leaf
            # 3. 둘 다 dfs
            # 이 세 가지 경우가 있을 듯?

            # 7이면.. 자식은 총 6이고 그러면 3 3도 되고, 1 5도 되고, 5 1 도 되고
            # 그냥 이런 식이네. 9면 자식이 총 8이니까 1 7, 3 5, 5 3, 7 1 이렇게.

            # 아 근데 이걸 여러개를 어떻게 적용하지? 그건 고민해보자.
            # 배열을 리턴하고, 배열을 다 돌면서 만들면 될 듯!
            res = []

            left, right = 1, k - 2
            while left < k:
                print(k, left, right)

                lefts, rights = make_full_binary(left), make_full_binary(right)
                for left_child in lefts:
                    for right_child in rights:
                        root = TreeNode(0)
                        root.left = left_child
                        root.right = right_child

                        res.append(root)

                left += 2
                right -= 2
            
            return res
        
        return make_full_binary(n)