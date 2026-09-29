class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # first sort the cars based on position to the 
        time = [0] * len(position)
        for i in range(len(position)):
            time[i] = (target - position[i]) / speed[i]
        
        # now sort based on position in reverse
        cars = [(position[i], time[i]) for i in range(len(position))]
        cars.sort(reverse=True)
        # print(cars)
        
        # if there is a lower time, it joins a fleet with the car behind it
        # so if there is a non increasing order we combine into one fleet
        fleets = len(position)
        last_time = 0
        for i in range(len(cars)):
            p, t = cars[i]
            if t == 0:
                last_time = t
                continue
            elif t <= last_time:
                fleets -= 1
            else:
                last_time = t
            
                
        return fleets
        