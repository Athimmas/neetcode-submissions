class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        output = []
        nums.sort()

        for i,a in enumerate(nums):

            if(a > 0):
                break

            if i > 0 and a == nums[i-1]:
                continue

            l = i + 1
            r = len(nums) - 1

            while l < r:
                three_sum = nums[l] + nums[r] + a
                
                if three_sum == 0:
                    output.append([nums[l],nums[r],a])
                    l+=1
                    r-=1
                    while nums[l] == nums[l-1] and l < r:
                        l+=1
                elif three_sum > 0:
                    r-=1
                elif three_sum < 0:
                    l+=1
                
        return output