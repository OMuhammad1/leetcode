class Node:
    def __init__(self, key, value):
        self.key = key 
        self.value = value
        self.next = None 
        self.prev = None
    
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity 
        self.dict = {}
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail 
        self.tail.prev = self.head
    
    def _front(self, node):
        temp2 = self.head.next
        self.head.next = node
        node.prev = self.head
        node.next = temp2 
        temp2.prev = node
    
    def delete(self, node):
        node.prev.next, node.next.prev = node.next, node.prev 
        
    def get(self, key: int) -> int:
        if key in self.dict:
            node = self.dict[key]
            self.delete(node)
            self._front(node)
            return node.value
        return -1
        
    def put(self, key: int, value: int) -> None:
        if key in self.dict:
            node = self.dict[key]
            node.value = value
            self.delete(node)
            self._front( node )
            return 
        if self.capacity <= len(self.dict):
            back = self.tail.prev
            del self.dict[back.key]
            self.delete(back)
        
        newNode = Node(key, value)
        self._front(newNode)
        self.dict[key] = newNode

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)