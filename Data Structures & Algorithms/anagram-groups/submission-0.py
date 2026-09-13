class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for s in strs:

            l = [0] * 26
            for c in s:
                l[ord(c) - ord('a')] += 1

            hashmap[tuple(l)].append(s)

        return hashmap.values()
