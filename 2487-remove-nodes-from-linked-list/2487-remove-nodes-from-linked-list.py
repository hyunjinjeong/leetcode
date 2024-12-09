# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # N이 있을 때, N.val보다 큰 값을 가진 노드가 오른쪽에 있으면 해당 노드를 삭제.
        # 그러면 원패스로는 일단 불가능함. 왜냐면 오른쪽 노드를 알 수가 없다.
        # two pass로는? 추가 공간을 쓰면 쉽..나?
        # monotonic stack을 써서 구성할 수 있겠는데
        # stack = []

        # node = head
        # while node:
        #     while stack and stack[-1] < node.val:
        #         stack.pop()
        #     stack.append(node.val)
        #     node = node.next

        # dummy = ListNode()
        # node = dummy
        # for val in stack:
        #     node.next = ListNode(val)
        #     node = node.next
        
        # return dummy.next

        # reverse하는 방법이 있구나
        def reverse(head_node):
            prev, node = None, head_node
            while node:
                tmp_next = node.next
                node.next = prev
                prev = node
                node = tmp_next
            return prev
        
        reversed_head = reverse(head)
        
        node = reversed_head
        curr_max = node.val
        while node and node.next:
            if node.next.val >= curr_max:
                curr_max = node.next.val
                node = node.next
            else:
                node.next = node.next.next

        return reverse(reversed_head)