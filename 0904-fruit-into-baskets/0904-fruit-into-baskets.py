class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # 바스켓이 2개니까.. subarray 중 distinct number가 2개 이하인 경우...
        
        res = 0
        count_map = collections.defaultdict(int)

        left = 0
        for right in range(len(fruits)):
            count_map[fruits[right]] += 1
            while len(count_map) > 2:
                count_map[fruits[left]] -= 1
                if count_map[fruits[left]] == 0:
                    del count_map[fruits[left]]
                left += 1
            res = max(res, right - left + 1)
        
        return res
                
