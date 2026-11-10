class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        
        while l <= r:
            # Find the midpoint
            m = (l + r) // 2
            
            # Check if the value at index m matches the target
            if nums[m] == target:
                return m
            # If mid value is too big, look in the left half
            elif nums[m] > target:
                r = m - 1
            # If mid value is too small, look in the right half
            else:
                l = m + 1
                
        return -1
