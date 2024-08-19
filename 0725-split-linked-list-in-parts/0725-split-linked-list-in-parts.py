# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        # 두 번 돌면 전체 갯수를 센 다음에 하나씩 나누면 될 듯?
        # 1-pass가 있으려나? -> 이건 나중에 생각하고
        # 일단 나누는 방법은.. k >= count면 앞에서부터 하나씩 채우면 됨
        # k < count면...
        # 앞에서부터 count % k 개만큼은 count // k + 1, 나머지는 count // k면 되려나?
        # 이건 k >= count일 때도 적용 가능할 듯? k:5, count:3이면 3%5 = 3, 3 // 5 = 0.
        # 5 5라고 해도 0, 1
        res = [ListNode(None) for _ in range(k)]

        node = head
        total_count = 0
        while node:
            total_count += 1
            node = node.next
        
        each_item = total_count // k
        extra_item_count = total_count % k

        original = head
        i = 0
            
        for i, dummy_node in enumerate(res):
            node = dummy_node
            curr = 0
            while curr < each_item:
                node.next = ListNode(original.val)
                node = node.next
                original = original.next
                curr += 1

            if i < extra_item_count:
                print(original)
                node.next = ListNode(original.val)
                node = node.next
                original = original.next
            
            res[i] = dummy_node.next
        
        return res