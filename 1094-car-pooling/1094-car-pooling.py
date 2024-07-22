class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 인터벌 문제 같은데?
        # 정렬을 from을 기준으로 해야 순서대로 처리하면서 중간에 capacity가 없는 경우를 확인할 수 있다
        trips.sort(key=lambda item: item[1])
        
        # heap을 써야할 듯?
        remaining_trips = []

        for num_passengers, start, dest in trips:
            # 과거 trip이 있을 때..
            # 과거 trip의 dest가 현재 start보다 작으면? 그냥 제외하면 됨. 같을 때도.
            # 과거 trip의 dest가 현재 start보다 크면? 겹치는 구간은 capacity를 차지함..
            while remaining_trips and remaining_trips[0][0] <= start:
                trip = heapq.heappop(remaining_trips)
                capacity += trip[1]

            capacity -= num_passengers
            if capacity < 0:
                return False
            
            heapq.heappush(remaining_trips, (dest, num_passengers))

        return True