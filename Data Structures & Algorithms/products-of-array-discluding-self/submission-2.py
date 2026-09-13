class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        n = len(nums)

        output = [1] * n

        prefix = 1
        for i in range(1,n):
            output[i] = nums[i-1] * prefix
            prefix = output[i]

        postfix = 1
        for i in range(n-1,-1,-1):
            output[i] = postfix * output[i]
            postfix = postfix * nums[i]

        return output