class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        # 정렬한 다음 앞뒤에서 하나씩 뽑기? 이게 반례가 있으려나
        skill.sort()

        l, r = 0, len(skill) - 1
        skill_sum = -1

        res = 0
        while l < r:
            lo, hi = skill[l], skill[r]
            if skill_sum == -1:
                skill_sum = lo + hi
            if lo + hi != skill_sum:
                return -1
            
            res += lo * hi
            l += 1
            r -= 1
        
        return res
