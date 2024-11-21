class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #         # 2. prefix sum + suffix sum 활용
#         # answer[i] = prefix_sum[i-1] * suffix_sum[i+1] 로 정리 가능!
#         # 공간 O(N) 시간 O(N)
#         prefix_sum = [nums[0]] * len(nums)
#         for i in range(1, len(nums)):
#             prefix_sum[i] = prefix_sum[i-1] * nums[i]
        
#         suffix_sum = [nums[len(nums)-1]] * len(nums)
#         for i in range(len(nums)-2, -1, -1):
#             suffix_sum[i] = suffix_sum[i+1] * nums[i]
        
#         answer = [suffix_sum[1]]
#         for i in range(1, len(nums)-1):
#             answer.append(prefix_sum[i-1] * suffix_sum[i+1])
#         answer.append(prefix_sum[len(nums)-2])
        
#         return answer
        
        # 3. Follow-up 조건인 공간 O(1)을 만족해야 한다..
        # prefix_sum과 suffix_sum을 저장해두지 않고 그때그때 계산..
        # 처음엔 prefix_sum 계산하는 것처럼 하고 그 다음에 suffix_sum 계산하면서 곱함.
        ans, suffix_product = [1] * len(nums), 1
        
        for i in range(1, len(nums)):
            ans[i] = ans[i-1] * nums[i-1]
            
        for i in range(len(nums)-1, -1, -1):
            ans[i] *= suffix_product
            suffix_product *= nums[i]
            
        return ans