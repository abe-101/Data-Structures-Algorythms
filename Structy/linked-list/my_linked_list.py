class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class MyLinkedList:

    def __init__(self):
        self.head = None
        

    def get(self, index: int) -> int:
        current = self.head
        count = 0
        while current is not None:
            if count == index:
                return current.val
            current = current.next
            count += 1
        return -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if self.head == None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.head == None:
            self.head = temp
        else:
            current = self.head
            while current.next is not None:
                current = current.next
            current.next = temp

        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            current = self.head
            count = 0
            while current is not None:
                if count == index -1:
                    temp = current.next
                    current.next = Node(val)
                    current.next.next = temp
                count += 1
                current = current.next

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        else:
            current = self.head
            count = 0
            prev = None
            while current is not None:
                if index == count:
                    prev.next = current.next
                    break
                prev = current
                current = current.next
                count += 1


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)
