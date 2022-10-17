class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None


class DoublyCLL:
    def __init__(self):
        self.last = None

    def insertEmpty(self, data):
        if self.last is None:
            newNode = Node(data)
            newNode.next = newNode
            newNode.prev = None
            self.last = newNode
            return self.last
        else:
            return "List is not empty"

    def insertBeg(self, data):

        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)

        else:
            newNode = Node(data)
            newNode.next = self.last
            newNode.prev = self.last
            self.last.prev = newNode
            self.last.next = newNode
            return self.last

    def insertEnd(self, data):
        newNode = Node(data)
        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)
        else:
            newNode.next = self.last.next
            newNode.prev = self.last
            self.last.next = newNode
            self.last = newNode
            return self.last

    def insertBetween(self, data, position):
        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)

        else:
            newNode = Node(data)
            temp = self.last.next
            while temp.next != self.last.next:
                if temp.data == position:
                    newNode.next = temp.next
                    newNode.prev = temp
                    temp.next.prev = newNode
                    temp.next = newNode
                    return self.last
                    if temp.next == self.last:
                        self.last = new_node
                    return self.last
                temp = temp.next
                if temp.next == self.last.next:
                    print("Position not found")

    def traverse(self):
        if self.last is None:
            print("List is empty")
            return
        else:
            temp = self.last.next
            while temp:
                print(temp.data, end=" ")
                temp = temp.next
                if temp == self.last.next:
                    break

    def delete(self, data):
        if self.last is None:
            print("List is empty")
            return
        else:
            temp = self.last.next
            while temp:
                if temp.data == data:
                    temp.prev.next = temp.next
                    temp.next.prev = temp.prev
                    return self.last
                temp = temp.next

    def current(self):
        if self.last is None:
            print("List is empty")
            return
        else:
            return self.last.prev.prev.data


DCLL = DoublyCLL()
print("Insertion Of: ", DCLL.insertEmpty(1).data, " at empty CLL is Successful")
print("Insertion Of: ", DCLL.insertBeg(2).next.data, " at beg CLL is Successful")
print("Insertion Of: ", DCLL.insertEnd(3).data, " at end CLL is Successful")
print("Insertion Of: ", DCLL.insertBetween(4, 2).next.next.data, " at position 2 is Successful")
print("Traversal of DCLL is Successful")
DCLL.traverse()
print("\n")
print("Deletion of: ", DCLL.current(), " is Successful")
DCLL.delete(DCLL.current())
print("Traversal of DCLL is Successful")
DCLL.traverse()
