class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = sorted(zip(position,speed),reverse=True)
        times = [(target-p)/s for p,s in cars]
        slowest =0
        fleets = 0

        for tim in times:
            if tim>slowest:
                fleets+=1
                slowest=tim
                

        return fleets