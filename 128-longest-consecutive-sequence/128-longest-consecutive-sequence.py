class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # 그래프로 풀어야 하는데 hash table 구현이 더 쉬워 보인다.
        longest_streak = 0
        
        num_set = set(nums)
        
        for num in nums:
            # 요 if문 없으면 TLE 걸림. 1 2 3 4 5 6 7 ... 이런 케이스 생각해보면 된다
            if num - 1 in num_set:
                continue
            
            current_num = num
            current_streak = 1
            
            while current_num + 1 in num_set:
                current_num += 1
                current_streak += 1
            
            longest_streak = max(longest_streak, current_streak)
        
        return longest_streak