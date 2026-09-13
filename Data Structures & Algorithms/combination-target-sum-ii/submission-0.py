class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        
        candidates.sort()
        n = len(candidates)
        res = []

        def dfs(start_index,summ,path):

            if summ == target:
                res.append(path[:])
                return

            for i in range(start_index,n):
                #if summ + candidates[i] > target:
                    #break
                if i > 0 and i != start_index and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                dfs(i+1,summ+candidates[i],path)
                path.pop()

        dfs(0,0,[])
        return res
