class Solution:
    def candy(self, ratings: List[int]) -> int:
        # 순서가 지켜져야 하니까 sorting은 안되고
        # dp인가..?
        # dp는 아닌거 같음. sub problem으로 안 나눠지는데
        # rating이 1 2 3 4 이런 식이면 candy도 1 2 3 4 이렇게 올라가야 하는구나
        # rating이 낮은 애부터 넣어주면?
        # 제일 낮은 애들은 무조건 1이고
        # 그 다음 낮은 애들은... 양 옆에 자기보다 낮은게 있으면 그거보다 +1하고 아니면 1이고
        # 이런 식으로 쭉 올라가면 될 거 같은데?
        # 이걸 어떻게 효율적으로 하지
        
        sorted_ratings = sorted([(rating, i) for i, rating in enumerate(ratings)])
        candies = [1] * len(ratings)
        
        res = 0
        for rating, i in sorted_ratings:
            left, right = 0, 0
            if i > 0 and ratings[i - 1] < rating:
                left = candies[i - 1]
            if i < len(ratings) - 1 and ratings[i + 1] < rating:
                right = candies[i + 1]
            
            candies[i] = max(left, right) + 1

        return sum(candies)