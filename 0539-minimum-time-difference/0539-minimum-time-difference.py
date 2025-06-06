class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # # HH:MM을 minutes로 변환하고
        # # 정렬해서 인접한 두 점의 차이 중 min을 구하면 될 듯? 그러면 O(nlogn)이네
        # # 아하 23:59 00:01 요런건 2분이 나와야 하는구나
        # # 그럼 M minutes가 있으면 M이랑 1440 + M 두개가 될 수 있는 거네
        # N = len(timePoints)

        # time_points_minutes = []
        # for s in timePoints:
        #     hours, minutes = s.split(":")
        #     time_points_minutes.append(int(hours) * 60 + int(minutes))

        # time_points_minutes.sort()
        
        # min_diff = float("inf")
        # for i in range(1, N):
        #     min_diff = min(min_diff, time_points_minutes[i] - time_points_minutes[i - 1])

        # # 0, n - 1 체크
        # min_diff = min(min_diff, 1440 + time_points_minutes[0] - time_points_minutes[N - 1])

        # return min_diff

        # bucket sort
        minutes_bucket = [False] * 1440
        for s in timePoints:
            hours, minutes = s.split(":")
            time = int(hours) * 60 + int(minutes)
            if minutes_bucket[time]: # same time
                return 0
            minutes_bucket[time] = True
        
        first_time, last_time = -1, -1
        prev_time = -1

        min_diff = float("inf")
        for time in range(1440):
            if not minutes_bucket[time]:
                continue
            
            if prev_time != -1:
                min_diff = min(min_diff, time - prev_time)
            
            if first_time == -1:
                first_time = time
            
            prev_time = time
            last_time = time
        
        # edge case
        min_diff = min(min_diff, 1440 + first_time - last_time)
    
        return min_diff
