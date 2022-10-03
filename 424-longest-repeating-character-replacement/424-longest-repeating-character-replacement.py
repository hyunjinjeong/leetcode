class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # 이것도 sliding window + hash table + two pointer...
        # 아.. 해법은 window 안에 특정 c의 갯수를 구해서,
        # window 길이에서 c의 갯수를 빼서 k개 이하이면 가능한 거니까 업데이트.
        # 넘으면 l은 오른쪽으로 한칸.
        answer = 0
        l = 0
        freq = collections.Counter()
        
        for r, c in enumerate(s):
            freq[c] += 1
            
            length = r - l + 1
            # 조건 만족하면 업뎃. 이 때 최댓값만 추적하면 됨.
            if length - max(freq.values()) <= k:
                answer = max(answer, length)
            # 아니면 l 오른쪽으로.
            else:
                freq[s[l]] -= 1
                l += 1
        
        return answer