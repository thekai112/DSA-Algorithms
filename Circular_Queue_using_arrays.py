import numpy as np


class CQueueA:
    def __init__(self, Size):
        self.size = Size
        self.queue = np.arange(Size)
        self.front = -1
        self.rear = -1
        print(f"Queue of size {self.size} has been created")

    def isEmpty(self):
        if self.front == self.rear == -1:
            return True
        else:
            return False

    def isFull(self):
        if (self.rear + 1) % self.size == self.front:
            return True
        else:
            return False

    def enqueue(self, Data):
        if self.isFull():
            print(" Queue is Full\n")

        elif self.isEmpty():
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
            print(f"{data} has been added to the queue")
        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = data
            print(f"{data} has been added to the queue")

    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"{self.queue[self.front]} has been removed from the queue")
            print(f"THE QUEUE AFTER THE DEQUEUE OF {self.queue[self.front]}: ")
            self.front = (self.front + 1) % self.size
            np.delete(self.queue, self.front)

    def peek(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(f"The front element is {self.queue[self.front]}")

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            i = self.front
            for i in range(self.front, self.rear + 1):
                print(self.queue[i], end=" ")
                i = (i + 1) % self.size
            print()


print("ENTER THE ARRAY SIZE: ")
size = int(input())
CQ = CQueueA(size)
print(f"IS THE QUEUE EMPTY? : {CQ.isEmpty()}")
for i in range(size):
    print("ENTER THE DATA: ")
    data = int(input())
    CQ.enqueue(data)
print("\n")
print("THE QUEUE: ")
CQ.display()
print("\n")
CQ.dequeue()
print("\n")
CQ.display()
print("\n")
CQ.peek()
print("\n")
print(f"IS THE QUEUE FULL? : {CQ.isFull()}")
