class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # Floyd's tortoise and hair algorithm...
        # Phase 1: Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Phase 2: Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        # 사이클의 시작점... 즉 두 포인터가 하나를 가리킨 것.
        # 값이 같기 때문이고, 이 때 이전 포인터의 값이 nums[hare] == nums[tortoise] => 새로운 hare == tortoise 이므로 
        # 요걸 리턴하면 됨
        return hare