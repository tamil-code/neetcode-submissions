class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        combined = sorted(zip(position, speed), reverse=True) # process from nearest to farthest
        position_sorted,speed_sorted = zip(*combined)

        # time to reach from each pos
        time_to_reach_target = [(target-pos)/speed_sorted[i] for i,pos in enumerate(position_sorted)]
        fleet = []
        for t in time_to_reach_target:
            if not fleet:
                fleet.append(t)
                continue
            if fleet[-1]<t:
                fleet.append(t)
            else:
                # else the cars comes behind joins with the car above because it takes less than or equal to the front cars obviously it will overtake
                pass
        return len(fleet)

            
