class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        freq = defaultdict(int)

        for num in nums:
            freq[num] += 1
        
        return heapq.nlargest(k,freq,key=freq.get)