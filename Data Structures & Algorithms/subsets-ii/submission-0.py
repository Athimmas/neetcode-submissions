class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        
        nums.sort()
        res = []
        n =len(nums)

        def dfs(start_index,path):

            if start_index == len(nums):
                res.append(path[:])
                return

            path.append(nums[start_index])
            dfs(start_index+1,path)
            path.pop()

            while start_index + 1 < n and nums[start_index+1] == nums[start_index]:
                start_index += 1

            dfs(start_index+1,path)

        dfs(0,[])
        return res