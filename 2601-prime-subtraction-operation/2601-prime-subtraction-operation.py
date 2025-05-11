class Solution:
    def primeSubOperation(self, nums: List[int]) -> bool:
        # 각 index는 한 번만 고를 수 있음. 각 숫자를 한 번씩만 뺄 수 있다는 말과 같음.
        # 왼쪽부터 시작해서, 자기자신을 왼쪽 숫자보다 크도록 가장 큰 prime을 구해서 빼면 되지 않을까..? 그렇게 빼고 체크하면 될 듯
        # max값까지 전체 소수를 구해두고 binary search로 찾는게 나으려나
        def get_primes(limit):
            is_prime = [True] * (limit + 1)
            is_prime[0] = is_prime[1] = False

            base = 1
            while base * base <= limit:
                base += 1
                if not is_prime[base]:
                    continue
                for num in range(2 * base, limit + 1, base):
                    is_prime[num] = False
            
            return [num for num in range(limit + 1) if is_prime[num]]

        def get_prime_index(maximum):
            lo, hi = 0, len(primes) - 1
            while lo < hi:
                mid = lo + (hi - lo) // 2
                if maximum <= primes[mid]:
                    hi = mid
                else:
                    lo = mid + 1
            
            return lo - 1 if primes[lo] > maximum else lo
        
        if len(nums) == 1:
            return True

        primes = get_primes(max(nums))
        for i in range(len(nums)):
            if nums[i] <= 2:
                continue
            if i > 0 and nums[i] - nums[i - 1] <= 2:
                continue
            
            prime_index = get_prime_index(
                nums[i] - nums[i - 1] - 1
                if i > 0
                else nums[i] - 1
            )
            nums[i] -= primes[prime_index]

        for i in range(1, len(nums)):
            if nums[i] <= nums[i - 1]:
                return False

        return True
