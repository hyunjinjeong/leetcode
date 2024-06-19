class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        # 뭔가 정렬을 하거나 해시맵에 담는 절차가 필요할 것 같은디
        # ?? 최대 2명만 탈 수 있다는 제약이 있구나..
        people.sort()
        
        left, right = 0, len(people) - 1
        ans = 0
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1
            
            ans += 1
        
        return ans