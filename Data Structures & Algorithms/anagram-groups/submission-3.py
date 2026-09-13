class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # for each string hash it. 
        # hash the hashmap into hashmap of list values and return values
        Map = defaultdict(list)
        for s in strs:
            counter = [0] * 26
            for c in s:
                counter[ord(c) - ord("a")] += 1

            Map[tuple(counter)].append(s)
            
        return Map.values()