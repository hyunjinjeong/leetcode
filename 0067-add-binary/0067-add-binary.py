class Solution:
    def addBinary(self, a: str, b: str) -> str:
        carry = 0
        answer = []
        
        list_a, list_b = list(a), list(b)
        while list_a or list_b or carry:
            num_a = int(list_a.pop()) if list_a else 0
            num_b = int(list_b.pop()) if list_b else 0
            
            temp_sum = num_a + num_b + carry
            answer.append(str(temp_sum % 2))
            carry = temp_sum // 2
        
        return "".join(answer[::-1]) # string concat이 O(n)이니까 시간 최적화를 위해...