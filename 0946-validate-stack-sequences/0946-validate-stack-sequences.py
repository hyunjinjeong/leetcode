class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        # 이건 그냥 시뮬레이션을 해보면 되지 않을까?
        N = len(pushed)
        
        stack = []
        
        push_index, pop_index = 0, 0
        while push_index < N:
            stack.append(pushed[push_index])
            push_index += 1
            while stack and stack[-1] == popped[pop_index]:
                stack.pop()
                pop_index += 1
        
        return len(stack) == 0