class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        cost = [None for _ in range(amount + 1)]

        for i in range(amount + 1):
            if i == 0:
                cost[i] = 0
            else:
                cost[i] = min(
                    (1 + cost[i - coin] for coin in coins 
                    if (i - coin >= 0 and cost[i - coin] is not None)),
                    default=None
                )
        
        if cost[-1] is None: 
            return -1
        
        return cost[-1]
