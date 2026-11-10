class Solution:
    def trap(self, height: List[int]) -> int:
        if not height:
            return 0
            
        l, r = 0, len(height) - 1
        left_max, right_max = height[l], height[r]
        total_water = 0
        
        while l < r:
            # Always process the side with the shorter bounding wall
            if left_max < right_max:
                l += 1
                # Update the tallest wall seen on the left so far
                left_max = max(left_max, height[l])
                # Water trapped is the water level minus the bar height
                total_water += left_max - height[l]
            else:
                r -= 1
                # Update the tallest wall seen on the right so far
                right_max = max(right_max, height[r])
                # Water trapped is the water level minus the bar height
                total_water += right_max - height[r]
                
        return total_water