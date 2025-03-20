class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        # start로 정렬하면 초반 N개는 순서대로 쓸 수 있음
        # 그 다음부터가 문제인데
        # delay를 어떤 식으로 다뤄야 할까...
        # 방마다 종료 시간을 저장하고 있어야 하나?
        # 종료 시간 중 최솟값, 방 번호도 가지고 있어야 함. 그래야 다음 meeting이 열릴 시간과 방을 구할 수 있다.
        # heap으로 저장하고 있어야 순차적으로 뽑을 수 있을 듯
        # 약간 greedy 느낌인데
        # heap이... N개가 되기 전까지는 그냥 쭉쭉 넣고
        # N개가 차면 -> 방이 꽉 찼다는 뜻
        # 1개를 pop해서 종료시간을 보고, 현재 meeting을 넣음.
        # 이 과정을 반복.
        # meeting을 넣을 때마다 방의 count를 증가시켜주고..
        meetings.sort()

        end_times, free_rooms = [], [i for i in range(n)]
        room_count = [0] * n

        for i in range(len(meetings)):
            while end_times and end_times[0][0] <= meetings[i][0]:
                end, room_number = heapq.heappop(end_times)
                heapq.heappush(free_rooms, room_number)
            
            if free_rooms:
                room_number = heapq.heappop(free_rooms)
                room_count[room_number] += 1
                heapq.heappush(end_times, (meetings[i][1], room_number))
            else:
                end, room_number = heapq.heappop(end_times)
                room_count[room_number] += 1
                heapq.heappush(end_times, (end + (meetings[i][1] - meetings[i][0]), room_number))

        res = 0
        max_count = -1
        for i, count in enumerate(room_count):
            if count > max_count:
                max_count = count
                res = i

        return res