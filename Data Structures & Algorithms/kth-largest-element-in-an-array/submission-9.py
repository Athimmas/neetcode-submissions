class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        def quickselect(nums,l,r,k):
            p = nums[r]
            j = l

            for i in range(l,r):
                if nums[i] <= p:
                    nums[i],nums[j] = nums[j],nums[i]
                    j += 1

            nums[j],nums[r] = nums[r],nums[j]

            if j == k:
                return nums[j]
            elif j > k:
                return quickselect(nums,l,j-1,k)
            else:
                return quickselect(nums,j+1,r,k)

        return quickselect(nums,0,len(nums) - 1,len(nums) - k)