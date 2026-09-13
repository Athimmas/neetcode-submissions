class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        
        stones = [-s for s in stones]
        # put all stones in a heap
        heapq.heapify(stones)

        # while len(stones) > 2 smash them
        while len(stones) >= 2:
            print(stones)
            stone1 = heapq.heappop(stones)
            stone2 = heapq.heappop(stones)

            diff = stone1 - stone2            
            if diff != 0:
                heapq.heappush(stones,diff)

        if len(stones) == 0:
            return 0
        
        return abs(stones[0])
