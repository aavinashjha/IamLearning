class Node:
    def __init__(self, d):
        self.data = d
        self.next = None

class LinkedList:
    def __init__(self, head=None):
        self.head = head 

    def addNode(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            mover = self.head
            while mover.next:
                mover = mover.next
            mover.next = node

    def __str__(self):
        mover = self.head
        ret = []
        while mover:
            ret.append(str(mover.data))
            mover = mover.next
        return '->'.join(ret)

    def reverse(self):
        p, c, h = None, self.head, None
        while c:
            n = c.next
            c.next = p
            p, c = c, n
            h = p 
        return LinkedList(p)

ll = LinkedList()
ll.addNode(1)
ll.addNode(2)
ll.addNode(3)
ll.addNode(4)
ll.addNode(5)
print(ll)
rll = ll.reverse()
print(rll)
