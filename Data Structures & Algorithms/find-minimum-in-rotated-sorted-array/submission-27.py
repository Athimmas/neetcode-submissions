class Solution:
    def findMin(self, nums: List[int]) -> int:
        start , end = 0, len(nums) - 1 
        curr_min = float("inf")
        
        if(nums[start] < nums[end]):
            return nums[start]

        while start <= end:
            mid = (start + end) // 2
            curr_min = min(nums[mid],curr_min)

            if(nums[mid] > nums[end]): 
                start = mid + 1
            else:
                end = mid - 1

        return curr_min
    