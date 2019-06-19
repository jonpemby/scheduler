from src.queue import AbstractQueue


class ScheduleQueue(AbstractQueue):
    def __init__(self):
        self.fifo_queue = []

    def peek(self):
        """
        Peek at the next item
        :return: any
        """
        if len(self.fifo_queue) < 1:
            raise IndexError("Queue is empty")
        return self.fifo_queue[0]

    def push(self, item):
        """
        Push a new item onto the queue
        :param item: any
        :return: any
        """
        self.fifo_queue.append(item)

    def pop(self):
        """
        Pop an item from the front of the queue
        :return: any
        """
        if len(self.fifo_queue) < 1:
            raise IndexError("Queue is empty")
        item = self.fifo_queue[0]
        self.fifo_queue = self.fifo_queue[1:]
        return item

    def repop(self):
        """
        Pops an item from the queue and re-enqueues it
        :return: any
        """
        item = self.pop()
        self.push(item)
        return item

    @staticmethod
    def from_list(items):
        """
        Build a queue from a list of initial items
        :param items: list
        :return: ScheduleQueue
        """
        queue = ScheduleQueue()
        for item in items:
            queue.push(item)
        return queue
