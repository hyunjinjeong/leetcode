class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        # a b c d ... 가 있으면
        # |a - a| + |b - a| + |c - a| + |d - a| ... 
        # sorted라는게 중요한거 같은데? a <= b <= c <= d ... 이니까
        # abs diff는 max(a, b) - min(a, b)
        # 정렬이 되어 있으니까... i가 있을 때 왼쪽은 nums[i] - NUM 이고 오른쪽은 NUM - nums[i]이 된다.
        # 그러면 길이를 N이라고 할 때
        # 1 2 3 4 5 6 7이 있을 때, N = 7. i가 4라고 하면 왼쪽은 4개, 오른쪽은 2개.
        # i에 대해서 왼쪽은 nums[i] * i, 오른쪽은 -(nums[i] * (N - i - 1)).
        # 그리고 왼쪽의 다른 숫자들 합은 -(nums[0] + nums[1] + ... + nums[i-1])이고 오른쪽은 nums[i+1] + nums[i+2] + ... + nums[N - 1].
        # 종합해보면 왼쪽은 nums[i] * i - sum(nums[:i]), 오른쪽은 sum(nums[i+1:]) - (nums[i] * (N - i - 1). 요걸 더하자.
        # prefix sum을 계산해서 위의 식에 집어넣으면 될 듯?
        N = len(nums)

        # prefix_sum = [0]
        # for num in nums:
        #     prefix_sum.append(prefix_sum[-1] + num)

        # res = []
        # for i, num in enumerate(nums):            
        #     left = num * i - prefix_sum[i]
        #     right = (prefix_sum[N] - prefix_sum[i + 1]) - num * (N - i - 1)
        #     res.append(left + right)
        
        # return res
            
        # 요건 memory O(1) 버전
        total_sum = sum(nums)
        left_sum = 0

        res = []
        for i, num in enumerate(nums):
            right_sum = total_sum - left_sum - num

            left = num * i - left_sum
            right = right_sum - num * (N - i - 1)
            res.append(left + right)

            left_sum += num
        
        return res