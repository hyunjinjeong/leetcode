class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:
        # 합이 같은 k개의 subset. 일단 합이 k로 나누어지는지 확인해야할 듯
        total_sum = sum(nums)
        if total_sum % k != 0:
            return False
        
        # 그 다음엔... target이 있고 k개의 subset 각각의 합이 target이 되어야 함.
        target = total_sum // k

        # backtracking으로 모든 경우를 하나씩 다 확인하는 건가?
        visited = set()
        nums.sort(reverse=True)
        
        def dfs(start, count, curr_sum):
            if count == k:
                return True
            
            if curr_sum == target:
                return dfs(0, count + 1, 0)
            
            for i in range(start, len(nums)):
                if i > 0 and not i - 1 in visited and nums[i] == nums[i - 1]:
                    continue
                if i in visited or curr_sum + nums[i] > target:
                    continue

                visited.add(i)
                if dfs(i + 1, count, curr_sum + nums[i]):
                    return True
                visited.remove(i)
            
            return False

        return dfs(0, 1, 0)