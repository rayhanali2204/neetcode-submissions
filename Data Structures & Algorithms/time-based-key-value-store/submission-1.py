class TimeMap:

    def __init__(self):
        # A dictionary where the key maps to a list of [value, timestamp] pairs
        self.store = {} 

    def set(self, key: str, value: str, timestamp: int) -> None:
        # If the key isn't in our dictionary yet, initialize it with an empty list
        if key not in self.store:
            self.store[key] = []
        # Append the [value, timestamp] pair to the list
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        # Step 1: Default result to an empty string if nothing is found
        res = ""
        
        # Step 2: Get the list of history pairs for this key (default to empty list if key doesn't exist)
        values = self.store.get(key, [])
        
        # Step 3: Binary Search on the history list
        l, r = 0, len(values) - 1
        while l <= r:
            mid = (l + r) // 2
            
            # If the current mid timestamp is less than or equal to our target
            if values[mid][1] <= timestamp:
                res = values[mid][0]  # This is a valid candidate! Save the value.
                l = mid + 1           # See if we can find an even larger valid timestamp to the right
            else:
                r = mid - 1           # Too big! Look to the left
                
        return res

