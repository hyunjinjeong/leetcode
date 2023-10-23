class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1 # 처음에 1을 더해야 하니

        ans = collections.deque()
        for i in range(len(digits) - 1, -1, -1):
            curr = digits[i] + carry
            if curr == 10:
                carry = 1
                ans.appendleft(0)
            else:
                carry = 0
                ans.appendleft(curr)
        
        if carry:
            ans.appendleft(1)
        
        return ans