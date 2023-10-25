class Solution:
    def isHappy(self, n: int) -> bool:
        # happy면 언젠간 1이 되니까 참
        # 근데 아닌 경우를 찾아내야 함
        # 사이클이라는거 보면 중복된 값이 나오는지 찾으면 될 듯

        seen = set()

        def happy(num):
            result = 0
            while num:
                result += (num % 10) ** 2
                num = num // 10
            
            if result == 1:
                return True
            
            if result in seen:
                return False
            
            seen.add(result)
            return happy(result)
        
        return happy(n)