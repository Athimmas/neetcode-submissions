class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        
        time = 0
        q = deque()
        c = Counter(tasks)
        maxheap = [-cnt for cnt in c.values()]

        while q or maxheap:
            time += 1

            if maxheap:
                cnt = heapq.heappop(maxheap)
                cnt += 1
                if cnt:
                    q.append([cnt,time+n])
            else:
                time = q[0][1]

            if q and q[0][1] == time:
                heapq.heappush(maxheap,q.popleft()[0])
            

        return time