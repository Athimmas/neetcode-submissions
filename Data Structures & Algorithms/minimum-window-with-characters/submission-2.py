class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if len(t) > len(s):
            return ""

        window = {}
        countT = {}
    

        for c in t:
            countT[c] = countT.get(c,0) + 1

        l = 0
        need = len(countT)
        have = 0
        reslen = float("infinity")
        res = [-1,-1]


        for r in range(len(s)):
            c = s[r]
            
            window[c] = window.get(c,0) + 1

            if c in countT and window[c] == countT[c]:
                have += 1

            while need == have:
                if r - l + 1 < reslen:
                    reslen = r - l + 1
                    res = [l,r]

                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have -= 1
                l += 1
            
        l,r = res
        return s[l:r+1] if reslen != float("infinity") else ""
