class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Time complexity: O(N), space complexity: O(1)
        # 따라서 sorting도 안되고, 추가 메모리 사용도 변수 하나 정도만 됨.
        
        # 아.. a^a = 0 이라는 특성을 이용하는구나 ㄷㄷ
        # ((2^2)^(1^1)^(4^4)^(5)) => (0^0^0^5) => 5.
        xor = 0
        for num in nums:
            xor ^= num
        return xor