class Solution:
    def missingNumber(self, nums: List[int]) -> int:
#         # 1. 일단 naive한 방법... 정렬한 다음에 이렇게 비교하면 된당. 공간은 O(1) 시간은 O(nlogn)
#           binary search 쓰면 탐색 속도는 빨라지지만 정렬 때문에 결국 big-o는 차이 없음
#         nums.sort()
        
#         for i in range(len(nums)):
#             if i != nums[i]:
#                 return i
        
#         return len(nums)
    
#         # 2. Follow-up으로 O(1) 공간과 O(n) 시간 복잡도로 해결해야 함.
#         # 일단 O(n) 공간 O(n) 시간은 set 써서 이런 식으로 된당.
#         s = set([i for i in range(len(nums)+1)])
#         s2 = set(nums)
        
#         # 원소 한개만 남았을 거
#         diff = s - s2
        
#         return list(diff)[0]

#         # 3. SUM을 사용하는 방법이 있네 ;;
#         total_sum = sum(range(len(nums)+1)) # 아니면 n*n+1//2 요거 써도 됨
#         for num in nums:
#             total_sum -= num # 아니면 걍 sum(nums) 빼도 되고...
        
#         # 그럼 이제 total_sum이 없는 숫자가 됨
#         return total_sum
#         
        # 목적인 bit manipulation으로 오면 XOR을 사용하면 된다!
        result = len(nums) # range 범위에서 마지막 숫자를 도달 못하기 때문에 요걸로 초기화.
        for i, num in enumerate(nums):
            # 이렇게 하면 i는 0, 1, ..., nums-1까지고 num은 0, ..., len(nums) 까지에 하나 빠진 값.
            # 즉 하나 빠진 값 제외하고는 다 XOR을 2번씩 수행, i^i = 0이 되어버리고 하나 남는건 i^0 = i
            # 따라서 빠진 값이 나오게 됨.
            result ^= i
            result ^= num
            # 0 1 2 3에서 1이 빠져있다고 하면.. nums는 0 2 3.
            # 3^0^1^2^3^0^2^3 => 0^0^1^2^2^3^3 == 1. 이런 식으로.. 
            # 3이 빠져 있으면 3^0^1^2^0^1^2 => 0^0^1^1^2^2^3 == 3.
        return result