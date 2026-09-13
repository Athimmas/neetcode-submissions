class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        hashmap = defaultdict(list)

        for string in strs:
            c = [0] * 26
            for char in string:
                c[ord(char) - ord('a')] += 1

            hashmap[tuple(c)].append(string)

        return hashmap.values()