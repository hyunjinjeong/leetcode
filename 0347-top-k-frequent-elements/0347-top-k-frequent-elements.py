class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [tup[0] for tup in collections.Counter(nums).most_common(k)]