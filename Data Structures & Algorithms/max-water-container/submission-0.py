class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        l = 0
        r = len(heights) - 1

        max_area = 0

        while r > l:
            cur = (r-l) * min(heights[r],heights[l])
            
            if cur > max_area:
                max_area = cur

            
            if(heights[r] > heights[l]):
                l+=1
            else:
                r-=1

        return max_area