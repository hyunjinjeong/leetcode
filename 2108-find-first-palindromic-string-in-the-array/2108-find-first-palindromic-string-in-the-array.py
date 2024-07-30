class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        # ? 그냥 찾으면 되는거 아닌감

        def is_palindrome(word):
            left, right = 0, len(word) - 1
            while left < right:
                left_char, right_char = word[left], word[right]
                if left_char != right_char:
                    return False
                left += 1
                right -= 1
            return True
        
        for word in words:
            if is_palindrome(word):
                return word
        
        return ""