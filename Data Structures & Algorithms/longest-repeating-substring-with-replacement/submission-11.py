class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        
        maxf = 0
        l = 0
        res = 0
        count = {}

        for r,c in enumerate(s):
            count[c] = count.get(c,0) + 1

            maxf = max(maxf,count[c])

            if r - l + 1 - maxf <= k:
                res = max(res,r - l + 1)
            else:
                count[s[l]] -= 1
                l += 1

        return res