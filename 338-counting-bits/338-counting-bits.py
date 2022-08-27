class Solution:
    def countBits(self, n: int) -> List[int]:
        def get_one_count(num):
            count = 0
            while num:
                num &= num-1
                count += 1
            return count
        
        result = []
        for num in range(n+1):
            result.append(get_one_count(num))
        
        return result