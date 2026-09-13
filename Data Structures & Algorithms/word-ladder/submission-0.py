class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        
        adjGraph = {}
        for word in wordList:
            for i in range(len(word)):
                transform = word[0:i] + '*' + word[i+1:]
                adjGraph.setdefault(transform,[]).append(word)

        
        q = deque([(beginWord,1)])
        visited = set([beginWord])

        while q:

            word,distance = q.popleft()

            if word == endWord:
                return distance

            for i in range(len(word)):
                transform = word[0:i] + '*' + word[i+1:]

                for neighbour in adjGraph.get(transform,[]):
                    if neighbour in visited:
                        continue
                    
                    visited.add(neighbour)
                    q.append([neighbour,distance + 1])

        return 0