# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Merge sort를 때려보면 될 듯?
        # merge sort는.. 합칠 때 정렬하는 방식. 나눠져있는 리스트들은 모두 정렬된 상태라고 가정하고 (왜냐면 합칠 때 정렬이 되니까)
        # 길이가 1이 될 때까지 나누고
        if not (head and head.next):
            return head
        
        mid = self.get_mid(head)
        left = self.sortList(head)
        right = self.sortList(mid)
        return self.merge(left, right)
    
    def get_mid(self, node):
        slow, fast = node, node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        mid = slow.next
        slow.next = None
        
        return mid
    
    def merge(self, left, right):
        dummy = ListNode(None)

        node = dummy
        while left and right:
            if left.val < right.val:
                node.next = left
                left = left.next
            else:
                node.next = right
                right = right.next
            node = node.next
        node.next = left or right

        return dummy.next
        