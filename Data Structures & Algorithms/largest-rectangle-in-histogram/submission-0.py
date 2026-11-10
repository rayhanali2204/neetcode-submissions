class Solution:

    def largestRectangleArea(self, heights: list[int]) -> int:
        maxArea = 0
        stack = []  # pairs: [index, height]

        for i, h in enumerate(heights):
            start = i
            # If the current height is SHORTER than the top of the stack,
            # it means the top of the stack cannot extend any further right.
            while stack and stack[-1][1] > h:
                index, height = stack.pop()
                # Calculate the area of the bar we just popped
                # Width = (current index) - (the index where that bar started)
                maxArea = max(maxArea, height * (i - index))
                # The current shorter bar can extend backward to this popped index!
                start = index

            # Push the current height, using the furthest backward start index
            stack.append([start, h])

        # After the loop, some bars might still be left in the stack.
        # These are bars that successfully extended all the way to the very end of the histogram.
        for index, height in stack:
            maxArea = max(maxArea, height * (len(heights) - index))

        return maxArea
