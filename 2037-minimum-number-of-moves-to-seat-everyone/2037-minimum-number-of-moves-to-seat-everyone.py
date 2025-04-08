class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()

        diff = 0
        for i in range(len(seats)):
            seat, student = seats[i], students[i]
            diff += abs(seat - student)
        return diff