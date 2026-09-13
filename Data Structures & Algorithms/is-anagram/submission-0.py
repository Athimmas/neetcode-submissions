class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        if(len(s) != len(t)):
            return False

        map1 = {}
        map2 = {}

        for s1,s2 in zip(s,t):
            if(s1 in map1):
                map1[s1] = map1[s1] + 1
            else:
                map1[s1] = 1

            if(s2 in map2):
                map2[s2] = map2[s2] + 1
            else:
                map2[s2] = 1

        for string in s:
            if string in map1 and string in map2:
                if(map1[string] != map2[string]):
                    return False
            else:
                return False

        return True 