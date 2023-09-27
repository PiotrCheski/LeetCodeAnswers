class linkedList:
    def __init__(self, val=0, nxt=None):
        self.val = val
        self.nxt = nxt

def printLinkedList(head):
    curr = head
    while curr != None:
        print(curr.val)
        curr = curr.nxt

a1 = linkedList(1)
a2 = linkedList(2)
a3 = linkedList(3)

a1.nxt = a2
a2.nxt = a3

printLinkedList(a1)
