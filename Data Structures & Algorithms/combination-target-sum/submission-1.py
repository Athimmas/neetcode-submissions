class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        n =len(nums)
        res = []

        def f(i,s,cur):
            if s == target:
                res.append(cur.copy())

            if s > target:
                return

            for idx in range(i,n):
                cur.append(nums[idx])
                f(idx,s + nums[idx],cur)
                cur.pop()


        f(0,0,[])

        return res