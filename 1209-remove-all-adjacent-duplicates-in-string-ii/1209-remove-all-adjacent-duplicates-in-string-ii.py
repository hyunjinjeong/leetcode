class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = [] # (char, count)
        
        for c in s:
            # 일단 스택에 넣고
            if stack and stack[-1][0] == c:
                stack.append((c, stack[-1][1] + 1))
            else:
                stack.append((c, 1))
            
            # k개가 겹쳐 있으면 빼기
            if stack and stack[-1][1] == k:
                for _ in range(k):
                    stack.pop()
        
        return "".join([pair[0] for pair in stack])
            
            
            