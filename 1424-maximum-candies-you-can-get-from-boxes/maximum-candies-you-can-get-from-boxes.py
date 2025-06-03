from collections import deque

class Solution:
    def maxCandies(self, status, candies, keys, containedBoxes, initialBoxes):
        n = len(status)
        owned = set(initialBoxes)
        queue = deque()
        visited = set()                   
        has_key = set()                    
        locked = set()                     
        total_candies = 0

        for box in initialBoxes:
            if status[box] == 1:
                queue.append(box)
            else:
                locked.add(box)

        while queue:
            box = queue.popleft()
            if box in visited:
                continue

            visited.add(box)
            total_candies += candies[box]

            for key in keys[box]:
                has_key.add(key)
                if key in locked:
                    queue.append(key)
                    locked.remove(key)

            for b in containedBoxes[box]:
                owned.add(b)
                if status[b] == 1 or b in has_key:
                    queue.append(b)
                else:
                    locked.add(b)

        return total_candies
