class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        # 원소 2개는 1번, 나머지(n-2)는 2번. 1번만 나오는 원소를 찾아라. 시간 O(N), 공간 O(1) 제한.
        # 이것도 XOR로 할 수 있나?
        # 1^1^2^2... 하면 없어지는데 문제는 1번 나오는 원소가 2개임
        # 3이랑 5랑 xor하면 
        # 011 / 101 -> 110이 된다. 이걸로 어케 알지?
        bitmask = 0
        for num in nums:
            bitmask ^= num
        
        # rightmost 1-bit diff
        diff = bitmask & (-bitmask)

        x = 0
        for num in nums:
            if num & diff:
                x ^= num
        
        return [x, bitmask^x]