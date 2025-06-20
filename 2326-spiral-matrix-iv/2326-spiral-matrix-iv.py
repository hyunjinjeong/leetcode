# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def spiralMatrix(self, m: int, n: int, head: Optional[ListNode]) -> List[List[int]]:
        mat = [[-1] * n for _ in range(m)]

        i, j = 0, 0
        if n == 1:
            di, dj = 1, 0
        else:
            di, dj = 0, 1

        top, right, bottom, left = 0, n - 1, m - 1, 0

        node = head
        while node:
            mat[i][j] = node.val

            i, j = i + di, j + dj
            node = node.next
            
            if di == 0 and dj == 1 and j == right:
                di, dj = 1, 0
                top += 1
            elif di == 1 and dj == 0 and i == bottom:
                di, dj = 0, -1
                right -= 1
            elif di == 0 and dj == -1 and j == left:
                di, dj = -1, 0
                bottom -= 1
            elif di == -1 and dj == 0 and i == top:
                di, dj = 0, 1
                left += 1
        
        return mat
