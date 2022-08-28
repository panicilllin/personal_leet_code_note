class MyCircularQueue:

    def __init__(self, k: int):
        self.queue_len = k
        self.queue = []


    def enQueue(self, value: int) -> bool:
        if len(self.queue) == self.queue_len:
            return False
        else:
            self.queue.append(value)
            return True

    def deQueue(self) -> bool:
        if self.queue:
            self.queue.pop(0)
            return True
        else:
            return False


    def Front(self) -> int:
        if self.queue:
            return self.queue[0]
            return True
        else:
            return -1


    def Rear(self) -> int:
        if self.queue:
            return self.queue[-1]
            return True
        else:
            return -1


    def isEmpty(self) -> bool:
        if self.queue:
            return False
        else:
            return True


    def isFull(self) -> bool:
        if len(self.queue) == self.queue_len:
            return True
        else:
            return False



# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()

# AC