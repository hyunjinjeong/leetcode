class Solution:
    def numTeams(self, rating: List[int]) -> int:
        # 3개 고르고 단조증가하거나 단조감소해야 함
        # monotonic?
        # 1 4 3 5 2. 1 -> 1 4 -> 1 3 -> 1 3 5
        # 1 3 5 / 1 4 5. 즉 2개가 되어야 하는데 이렇게 하면 1개가 된다.
        # 그럼 monotonic 쪽은 아닌 것 같고

        # 일단 backtracking?
        # 단조증가랑 단조감소 각각 구해서 더하기
        # 이제 이걸 dp로 바꿔야 하는데

        @cache
        def get_monotonic_increasing_count(start, pick_count):
            if pick_count == 3:
                return 1
            
            count = 0
            for i in range(start + 1, len(rating)):
                if rating[i] > rating[start]:
                    count += get_monotonic_increasing_count(i, pick_count + 1)
            return count
        
        @cache
        def get_monotonic_decreasing_count(start, pick_count):
            if pick_count == 3:
                return 1
            
            count = 0
            for i in range(start + 1, len(rating)):
                if rating[i] < rating[start]:
                    count += get_monotonic_decreasing_count(i, pick_count + 1)
            return count
        
        total_count = 0
        for i in range(len(rating)):
            total_count += get_monotonic_increasing_count(i, 1) + get_monotonic_decreasing_count(i, 1)
        
        return total_count
