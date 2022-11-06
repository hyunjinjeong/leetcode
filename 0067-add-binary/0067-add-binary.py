class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        answer = ""
        
        list_a, list_b = list(a), list(b)
        while list_a or list_b or carry:
            num_a = int(list_a.pop()) if list_a else 0
            num_b = int(list_b.pop()) if list_b else 0
            
            answer = str((num_a + num_b + carry) % 2) + answer
            carry = (num_a + num_b + carry) // 2
        
        return answer