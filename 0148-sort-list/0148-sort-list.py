# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        # 간단한 방법을 생각해보면
        # 한번 돌아서 array에 저장 후 sort -> 그 다음에 array를 다시 ll로 만들어 주기
        # 시간은 O(nlogn), 공간은 O(n)
        arr = []
        node = head
        while node:
            arr.append(node.val)
            node = node.next
        
        arr.sort()
        
        dummy = ListNode()
        node = dummy
        for item in arr:
            node.next = ListNode(item)
            node = node.next
        
        return dummy.next