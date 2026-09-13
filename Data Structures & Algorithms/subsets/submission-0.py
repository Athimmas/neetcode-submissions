class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        n = len(nums)
        ret = []

        def f(s,i):
            
            if i == n:
                ret.append(s.copy())
                return
                
            s.append(nums[i])
            f(s,i+1)
            s.pop()
            f(s,i+1)


        f([],0)
        return ret
