class Solution:
    def longestPalindrome(self, s: str) -> int:
        counter = collections.Counter(s)
        
        # greedy로 되는구낭..
        # 일단 n (짝수) 혹은 n-1 (홀수) 씩은 다 들어가고, s보다 길이가 작으면 center에 1개짜리가 들어갈 수 있음
        answer = 0
        for c in counter:
            answer += (counter[c] // 2) * 2
        
        if answer < len(s):
            answer += 1
        
        return answer