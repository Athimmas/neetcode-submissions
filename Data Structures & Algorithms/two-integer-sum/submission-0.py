class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        hashmap = {}

        for idx,num in enumerate(nums):
            toFind = target - num

            if(toFind in hashmap):
                return [hashmap[toFind],idx]

            else:
                hashmap[num] = idx
