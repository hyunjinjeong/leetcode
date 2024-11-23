class UndergroundSystem:

    def __init__(self):
        # maintain sum and count for each station
        self.station_map = {}
        self.user_map = collections.defaultdict(list)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.user_map[id].append((stationName, t))

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        start_station, start_time = self.user_map[id].pop()
        if (start_station, stationName) in self.station_map:
            prev_sum, prev_count = self.station_map[(start_station, stationName)]
            self.station_map[(start_station, stationName)] = (prev_sum + t - start_time, prev_count + 1)
        else:
            self.station_map[(start_station, stationName)] = (t - start_time, 1)
        
    def getAverageTime(self, startStation: str, endStation: str) -> float:
        total, count = self.station_map[(startStation, endStation)]
        return total / count
        


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)