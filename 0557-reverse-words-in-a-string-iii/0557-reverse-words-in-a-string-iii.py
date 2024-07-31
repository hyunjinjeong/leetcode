class Solution:
    def reverseWords(self, s: str) -> str:
        new_str = s.split(" ")

        for i in range(len(new_str)):
            new_str[i] = new_str[i][::-1]

        return " ".join(new_str)
            