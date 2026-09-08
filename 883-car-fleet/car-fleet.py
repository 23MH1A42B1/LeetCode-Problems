class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []

        for i in range(len(position)):
            time = (target - position[i]) / speed[i]
            cars.append([position[i], time])

        cars.sort(reverse=True)

        fleets = 0
        last_time = 0

        for position, time in cars:

            if time > last_time:
                fleets += 1
                last_time = time

        return fleets