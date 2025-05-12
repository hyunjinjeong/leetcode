class Solution:
    def canConstruct(self, s: str, k: int) -> bool:
        # 실제로 palindrome을 만들 필요는 없을 것 같고... 아마 count를 이용하지 않을까
        # palindrome 가능한 조건은? 1. 알파벳 하나가 0개, 나머지 알파벳은 모두 2n개, 2. 알파벳 하나가 1개, 나머지 알파벳은 모두 2n개.
        # 일반화하면 알파벳 하나가 0-1개, 나머지 알파벳은 2n(n>=0)개.
        # 뭔가 핵심은 1개짜리 알파벳을 고르는 방법 같은데
        # 알파벳 개수가 홀수면 무조건 1개짜리에 하나는 넣어야 함
        # 그러면.. palindrome의 최솟값은 홀수인 알파벳 개수 이상. 최댓값은? count (1개씩)
        # 최솟값과 최댓값 사이에서 False인 경우가 있으려나?
        if k > len(s):
            return False
        
        counter = collections.Counter(s)
        
        odd_count = 0
        for count in counter.values():
            if count % 2 == 1:
                odd_count += 1

        return k >= odd_count
