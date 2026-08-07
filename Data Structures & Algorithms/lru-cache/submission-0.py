class Node:
    def __init__(self,key:int=None,val:int=None):
        self.key=key
        self.val=val
        self.prev=None
        self.next=None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.head = Node()
        self.tail = Node()
        self.head.next=self.tail
        self.tail.prev=self.head

    def _insert(self,newNode):
        prev=self.head.next

        # node reset
        newNode.next=self.head.next
        newNode.prev=self.head

        # head and tail reset to node
        self.head.next.prev=newNode
        self.head.next=newNode

        
    def _remove(self,node:Node):
        prev=node.prev
        nxt=node.next

        prev.next=nxt
        nxt.prev=prev

    def get(self, key: int) -> int:
        if key in self.cache:
            node=self.cache[key]
            self._remove(node)
            self._insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self._remove(self.cache[key])
        node=Node(key,value)
        self._insert(node)
        self.cache[key]=node
        
        if len(self.cache)>self.capacity:
            lru=self.tail.prev
            self._remove(lru)
            del self.cache[lru.key]


        
        
