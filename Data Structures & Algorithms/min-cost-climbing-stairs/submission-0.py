class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # first, second, i, i + 1 ...
        # subproblem: min cost to take a step off a given floor
        first, second = cost[0], cost[1]
        i = 2
        while i < len(cost):
            temp = min(first, second) + cost[i]
            first = second
            second = temp
            i += 1
        
        return min (first, second)