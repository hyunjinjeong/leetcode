class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # binary search 아니면 two pointer 같은디
        # binary search로 x의 index를 찾고 k개만큼 채우는 건 two pointer로 하면 될 듯?
        
        # 1. Find the index of x using binary search
        def find_x():
            left, right = 0, len(arr)-1
            
            while left < right:
                mid = (left + right) // 2
                
                if arr[mid] < x:
                    left = mid + 1
                else:
                    right = mid

            return left
        
        # 2. Make the answer array. 아까 찾은 x의 index가 right
        right = find_x()
        left = right - 1
        print(left, right)
        
        while k:
            if left < 0:
                right += 1
            elif right >= len(arr):
                left -= 1
            else:
                num_left, num_right = arr[left], arr[right]
                if abs(num_left-x) <= abs(num_right-x):
                    left -= 1
                else:
                    right += 1      
            k -= 1
        # 여기서 left와 right를 각각 마지막에 -1, +1 한 것들은 제외해줘야 함.
        return arr[left+1:right]