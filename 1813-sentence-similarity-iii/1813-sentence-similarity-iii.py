class Solution:
    def areSentencesSimilar(self, sentence1: str, sentence2: str) -> bool:
        # sentence 하나가 다른 하나를 감싸고 있어야 함. 즉 양쪽 끝이 같아야 한다. (혹은 한쪽)
        # prefix이거나 postfix이거나 양쪽 끝이거나. 그럼 왼쪽 오른쪽에서 세면 될 듯?
        s1, s2 = sentence1.split(" "), sentence2.split(" ")
        if len(s1) > len(s2):
            s1, s2 = s2, s1 # make sure s1 smaller
        
        s1_left, s1_right = 0, len(s1)
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                break
            s1_left += 1
        
        for i in range(len(s1)):
            if s1[len(s1) - 1 - i] != s2[len(s2) - 1 - i]:
                break    
            s1_right -= 1

        return s1_left >= s1_right
