class Solution:
    def maxProduct(self, s: str) -> int:
        # i, j, k... 등 palindrome이 되는 인덱스를 골랐을 때
        # 그 나머지에 대해서 최대 palindrome을 계산해서 곱하면 되려나? 왜냐면 N이 12임
        # backtracking 이라고 보면 될 듯
        # 그냥 subsequence 2개를 만들어놓고 두개가 palindrome인지만 보면 되는구나
        def is_palindrome(arr):
            for i in range(len(arr)):
                if arr[i] != arr[len(arr) - 1 - i]:
                    return False
            return True

        @cache
        def dfs(i, left, right):
            if i == len(s):
                if is_palindrome(left) and is_palindrome(right):
                    return len(left) * len(right)
                else:
                    return 0
            
            not_pick = dfs(i + 1, left, right)
            pick_left = dfs(i + 1, left + s[i], right)
            pick_right = dfs(i + 1, left, right + s[i])
            return max(not_pick, pick_left, pick_right)
        
        return dfs(0, '', '')