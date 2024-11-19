class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # So the capital is increased only. capital[i] is just a condition to start the i-th project.
        # I guess greedy works:
        # For the current capital K, we should choose a task with the maximum profit where capital[i] <= K
        # First I need to sort the two arrays in order of (capital, profit)
        # Then use max heap to find the task with the maximum profit.
        # Do it for k times.
        curr_capital = w

        sorted_projects = sorted(zip(capital, profits))
        max_heap = []

        i = 0
        for _ in range(k):
            # Add valid projects to the heap
            while i < len(profits) and sorted_projects[i][0] <= curr_capital:
                heapq.heappush(max_heap, -sorted_projects[i][1])
                i += 1

            if not max_heap:
                break
            
            curr_capital += -heapq.heappop(max_heap)
        
        return curr_capital