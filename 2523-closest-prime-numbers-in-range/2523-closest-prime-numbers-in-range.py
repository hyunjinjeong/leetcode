class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        is_prime = [True] * (right + 1)
        is_prime[0] = is_prime[1] = False

        for num in range(2, int(math.sqrt(right)) + 1):
            if not is_prime[num]:
                continue
            
            for multiple in range(num * num, right + 1, num):
                is_prime[multiple] = False
        
        small, large = -1, -1
        prev = -1
        for num in range(left, right + 1):
            if not is_prime[num]:
                continue

            if small == -1: # first
                small = num
            elif large == -1: # second
                large = num
            elif num - prev < large - small:
                small, large = prev, num
            
            prev = num
        
        if small == -1 or large == -1:
            return [-1, -1]
        return [small, large]
