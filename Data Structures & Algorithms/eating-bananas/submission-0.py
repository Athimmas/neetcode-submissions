class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # most time taken is sum array elements
        # least time taken array size

        # Try all numbers b/w 1 and most time taken and calculate?
        # Binary searching b/w 1 and the number doesnt help either 
        # since we want the least 

        l = 1
        r = max(piles)
        res = r

        while l <= r:
            mid = (l + r)//2

            time = 0
            for p in piles:
                time += math.ceil(float(p)/mid)

            if time <= h:
                res = mid
                r = mid - 1
            else:
                l = mid + 1

        return res