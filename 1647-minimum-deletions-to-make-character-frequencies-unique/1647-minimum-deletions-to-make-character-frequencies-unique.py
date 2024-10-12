class Solution:
    def minDeletions(self, s: str) -> int:
        res = 0
        freq = collections.Counter(s)

        arr = sorted(val for val in freq.values())
        freq_set = set()
        for val in arr:
            while val and val in freq_set:
                val -= 1
                res += 1
            freq_set.add(val)
        
        return res

        # 어떤 c를 삭제해야 되려나..
        # freq는 O(1)임. 이거 정렬할 수도 있겠다.
        # 정렬하고 나서.. 그 다음부터는 brute force로 처리하면 되나?
