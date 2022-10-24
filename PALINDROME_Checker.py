import numpy as n


class Stack:
    def __init__(self, size):
        self.size = size
        self.top = -1
        self.data = n.chararray(self.size)

    def push(self, data):
        if self.top == self.size - 1:
            return False
        else:
            self.top += 1
            self.data[self.top] = data

    def pop(self):
        if self.top == -1:
            return False
        else:
            self.top -= 1
            return self.data[self.top + 1]

    def is_empty(self):
        if self.top == -1:
            return True
        else:
            return False


class Queue:
    def __init__(self, size):
        self.size = size
        self.rear = -1
        self.front = -1
        self.data = n.chararray(self.size)

    def enqueue(self, data):
        if self.rear == self.size - 1:
            return False
        else:
            if self.front == -1:
                self.front = 0
            self.rear += 1
            self.data[self.rear] = data

    def dequeue(self):
        if self.front == -1 or self.front > self.rear:
            return False
        else:
            self.front += 1
            return self.data[self.front - 1]


number = int(input("THE LENGTH OF THE STRING: "))
stack = Stack(number)
queue = Queue(number)

print("ENTER THE STRING: ")

for i in range(0, number):
    print(f"THE {i + 1}TH CHARACTER: ")
    char = input()
    stack.push(char)
    queue.enqueue(char)

count = 0

while not stack.is_empty():
    if stack.pop() == queue.dequeue():
        count += 1

    else:
        count = 0

if count == number:
    print("A PALINDROME")
else:
    print("NOT A PALINDROME")

