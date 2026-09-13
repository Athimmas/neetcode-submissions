class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        if k == len(nums):
            return nums

        m = Counter(nums)
        print(m)
        return heapq.nlargest(k,m.keys(),key=m.get)