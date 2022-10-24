class Node:
  # constructor
  def __init__(self, data = None, next = None):
    self.data = data
    self.next = next
# A Linked List class with a single head node
class LinkedList:
  def __init__(self):
    self.head = None
  # insert at the tail of the linked list
  def insert(self, data):
    newNode = Node(data)
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      current.next = newNode
    else:
      self.head = newNode
  # remove an element from the head of the linked list
  def remove(self):
    temp = self.head
    if (temp is not None):
      element = temp.data
      self.head = temp.next
      temp = None
      return element
  # dispay an element from the tail of the linked list
  def peek(self):
    if(self.head):
      current = self.head
      while(current.next):
        current = current.next
      return current.data
  # print method for the linked list
  def printLL(self):
    current = self.head
    while(current):
      print(current.data)
      current = current.next

# A queue implemented using a linked list
Queue = LinkedList()
# Enqueue 3
Queue.insert(88)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 4
Queue.insert(23)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Enqueue 5
Queue.insert(59)
# Display element at the tail
print("Element at the tail:", Queue.peek())
# Dequeue elements
print("Element dequeued:", Queue.remove())
print("Element dequeued:", Queue.remove())
print("Element dequeued:", Queue.remove())
