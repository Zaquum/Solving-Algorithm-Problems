class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        cnt = 0
        for seat, student in zip(seats, students):
            cnt += abs(seat - student)
        return cnt