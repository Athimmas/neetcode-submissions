class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        c1 = Counter(s1)
        l = 0
        c2 = Counter()

        for r in range(len(s2)):
            c = s2[r]
            if c not in c1:
                l = r + 1
                c2.clear()
                continue

            c2.update(c)
            if(c1[c] < c2[c]):
                while c1[c] != c2[c]:
                    c2[s2[l]] -= 1
                    l += 1

            
            if r - l + 1 == len(s1):
                return True

        return False


            