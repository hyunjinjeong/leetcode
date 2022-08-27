class Solution:
    def search(self, nums: List[int], target: int) -> int:
        # 이런 문제는 어떻게든 binary를 사용할 방법을 찾아봐야 함..
        # 여기선 왼쪽 오른쪽 둘 중 하나는 단조 증가하는 구간이라는 사실을 이용.
        # 탈출 조건이랑 left, right 줄이는 조건도 잘 생각하기.
        left, right = 0, len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2
            num_mid, num_left, num_right = nums[mid], nums[left], nums[right]
            
            if num_mid == target:
                return mid
            
            # 왼쪽이 단조 증가하는 구간인 경우.
            # <=인 이유는? 1개, 2개 이런 걸로 테스트해보면 됨. left랑 mid랑 같아지는 경우가 있음.
            if num_left <= num_mid:
                # target이 이 구간에 있으면 오른쪽을 버린다
                if num_left <= target <= num_mid:
                    # mid - 1인 이유는 위에서 mid를 검사하기 때문에. 안전하게 버려도 됨.
                    right = mid - 1
                else: # 아니면 왼쪽을 버리고.
                    left = mid + 1
            else: # 오른쪽이 단조 증가하는 구간인 경우.
                # target이 이 구간에 있으면 왼쪽을 버린다.
                if num_mid <= target <= num_right:
                    left = mid + 1
                else: # 아니면 오른쪽을 버리고.
                    right = mid - 1
                    
        return -1