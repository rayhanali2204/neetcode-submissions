class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        A, B = nums1, nums2
        total = len(A) + len(B)
        half = (total + 1) // 2 # Total elements needed on the left
        
        # Always run binary search on the smaller array to guarantee O(log(min(A,B)))
        if len(B) < len(A):
            A, B = B, A
            
        l, r = 0, len(A) - 1
        while True:
            # i is the cut index for A, j is the cut index for B
            i = (l + r) // 2
            j = half - i - 2
            
            # Get the boundary values (handle out-of-bounds with infinity)
            Aleft = A[i] if i >= 0 else float("-inf")
            Aright = A[i + 1] if (i + 1) < len(A) else float("inf")
            Bleft = B[j] if j >= 0 else float("-inf")
            Bright = B[j + 1] if (j + 1) < len(B) else float("inf")
            
            # Check if the partition is correct
            if Aleft <= Bright and Bleft <= Aright:
                # Odd total elements: median is the maximum of the left halves
                if total % 2:
                    return max(Aleft, Bleft)
                # Even total elements: average of the two middle edges
                return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
                
            elif Aleft > Bright:
                # Too many elements from A on the left, move A's cut left
                r = i - 1
            else:
                # Too few elements from A on the left, move A's cut right
                l = i + 1
