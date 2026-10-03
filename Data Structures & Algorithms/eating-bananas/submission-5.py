class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
      # each hour you can eat k bananas
      # find the minimal k to eat all bananas under h

      # time to finish
      # time = piles[i] // k, if piles[i] % k != 0, time += 1
      # k could be in between 1 and the highest?
      min_k = 1
      lo, hi = 1, max(piles)
      while lo <= hi:
          k = lo + ((hi - lo) // 2)
          time = 0
          for p in piles:
            time += p // k
            if p % k != 0: time += 1

          if time > h:
            lo = k + 1
          else:
              min_k = k
              hi = k - 1

      return min_k        