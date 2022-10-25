class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class SinglyCLL:
    def __init__(self):
        self.last = None

    def insertEmpty(self, data):
        if self.last is None:
            new_node = Node(data)
            new_node.next = new_node
            self.last = new_node
            return self.last

        else:
            return "List is not empty"

    def insertBegin(self, data):
        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)

        else:
            new_node = Node(data)
            new_node.next = self.last.next
            self.last.next = new_node
            return self.last

    def insertEnd(self, data):
        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)

        else:
            new_node = Node(data)
            new_node.next = self.last.next
            self.last.next = new_node
            self.last = new_node
            return self.last

    def insertBetween(self, data, position):
        if self.last is None:
            print("List is empty, Insertion Will Happen Thou")
            self.insertEmpty(data)

        else:
            new_node = Node(data)
            temp = self.last.next
            while temp.next != self.last.next:
                if temp.data == position:
                    new_node.next = temp.next
                    temp.next = new_node
                    return self.last
                    if temp == self.last:
                        self.last = new_node
                    return self.last
                temp = temp.next
                if temp == self.last.next:
                    print("Position not found")

    def traverse(self):
        if self.last is None:
            print("List is empty")
            return

        else:
            temp = self.last.next
            while temp.next != self.last.next:
                print(temp.data)
                temp = temp.next
            print(temp.data)


    def delete(self, data):
        if self.last is None:
            print("List is empty")
            return

        else:
            temp = self.last.next
            while temp.next != self.last.next:
                if temp.data == data:
                    temp.next = temp.next.next
                    return self.last
                temp = temp.next
                if temp == self.last.next:
                    print("Data not found")



CLL = SinglyCLL()
CLL.insertEmpty(1)
print("Insertion Of: ", CLL.last.data, " at empty CLL is Successful")
CLL.insertBegin(2)
print("Insertion Of: ", CLL.last.next.data, " at begin CLL is Successful")
CLL.insertEnd(3)
print("Insertion Of: ", CLL.last.data, " at end CLL is Successful")
CLL.insertBetween(4, 2)
print("Insertion Of: ", CLL.last.next.next.data, " after 2 is Successful")
print("\nTraversal of CLL: ")
CLL.traverse()
CLL.delete(1)
print("\nTraversal of CLL after deletion of The Top Node: ")
CLL.traverse()
