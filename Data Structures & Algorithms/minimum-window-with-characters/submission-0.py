class Solution:
    def minWindow(self, s: str, t: str) -> str:
        
        if t == "":
            return ""

        countS = {}
        countT = {}

        for c in t:
            countT[c] = 1 + countT.get(c,0)

        have = 0
        need = len(countT)

        l,r = 0, len(s)
        
        res,resLen = [-1,-1],float("infinity")
        

        for r in range(len(s)):
            c = s[r]

            countS[c] = countS.get(c,0) + 1
            # if character we need present we update 
            # window and update need
            if c in countT and countS[c] == countT[c]:
                have += 1
            
            while need == have:
                # remove characters from left by 
                # decrementing from dictionary
                if r - l + 1 < resLen:
                    resLen = r - l + 1
                    res = [l,r]
                
                countS[s[l]] -= 1
                if(s[l] in countT and countS[s[l]] < countT[s[l]]):
                    have -= 1
                l += 1

        l, r = res
        
        return s[l:r+1] if resLen != float("infinity") else ""