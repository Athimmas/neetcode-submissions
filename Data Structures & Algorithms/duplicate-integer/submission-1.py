class Solution(object):
    def hasDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        
        hashmap = {}

        for num in nums:
            if num in hashmap:
                return True
            
            hashmap[num] = 1

        return False
