class Node:
    def __init__(self, key, val):
        self.key = key 
        self.val = val 
        self.next = None

class MyHashMap:

    def __init__(self):
        self.keys = [[] for _ in range(1000)]

    def put(self, key: int, value: int) -> None:
        tempKey = key % 1000 
        arr = self.keys[tempKey]

        if not arr:
            arr.append(Node(key, value))
            return 
        
        curr = arr[0]
        while curr:
            if curr.key == key:
                curr.val = value
                return
            if not curr.next:
                break
            curr = curr.next

        curr.next = Node(key, value)

    def get(self, key: int) -> int:
        tempKey = key % 1000 
        arr = self.keys[tempKey]

        if not arr:
            return -1 
        
        curr = arr[0]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        
        return -1 

    def remove(self, key: int) -> None:
        tempKey = key % 1000 
        arr = self.keys[tempKey]

        if not arr:
            return 
        
        curr = arr[0]
        if curr.key == key:
            if curr.next:
                arr[0] = curr.next
            else:
                self.keys[tempKey] = []
            return

        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return
            curr = curr.next

