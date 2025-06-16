class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        # 뭐지 그냥 루프 돌면 되는거 아닌가
        total_waiting = 0

        curr_time = 0
        for arrival, time in customers:
            curr_time = max(curr_time, arrival)
            curr_time += time

            total_waiting += max(0, curr_time - arrival)
        
        return total_waiting / len(customers)
