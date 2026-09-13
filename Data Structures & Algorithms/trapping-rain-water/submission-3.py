class Solution:
    def trap(self, height: List[int]) -> int:
        
        l = 0
        r = len(height) - 1

        maxL = height[l]
        maxR = height[r]
        total = 0

        while l <= r:

            if maxL < maxR:
                maxL = max(height[l],maxL)
                total += maxL - height[l]
                l += 1

            else:
                maxR = max(height[r],maxR)
                total += maxR - height[r]
                r -= 1

        return total