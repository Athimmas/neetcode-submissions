class TimeMap:

    def __init__(self):
        self.Map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.Map[key].append([timestamp,value])

    def get(self, key: str, timestamp: int) -> str:
        List = self.Map.get(key,[])

        l = 0
        r = len(List) - 1
        res = ""

        while l <= r:
            mid = (l+r) // 2
            
            if timestamp < List[mid][0]:
                r = mid - 1
            else:
                res = List[mid][1]
                l = mid + 1

         
        return res
            
