class Solution:
    def findMin(self, nums: List[int]) -> int:

        start , end = 0, len(nums) - 1 
        
        if(nums[start] < nums[end]):
            return nums[start]

        while start  <  end :
            mid = (end + start ) // 2
            
            if(nums[mid] < nums[mid - 1]):
                return nums[mid]

            # right has the min 
            if nums[mid] > nums[end]:
                start = mid + 1
                
            # left has the  min 
            else:
                end = mid - 1 
                
        return nums[start]