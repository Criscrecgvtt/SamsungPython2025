class Deque:
    
    def __init__(self):
        self.queue = []

    def add_first(self, item):
        ''' Add an item to the front of the queue '''
        self.queue.insert(0, item)

    def remove_first(self):
        ''' Remove and return the item from the front '''
        if self.queue:
            return self.queue.pop(0)
        return None

    def add_last(self, item):
        ''' Add an item to the rear of the queue '''
        self.queue.append(item)

    def remove_last(self):
        ''' Remove and return the item from the rear '''
        if self.queue:
            return self.queue.pop()
        return None
