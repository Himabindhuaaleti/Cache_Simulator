class FIFO_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.queue = []
        self.hits = 0
        self.misses = 0

    def access(self, page):
        hit = page in self.queue
        evicted = None
        if hit:
            self.hits += 1
        else:
            self.misses += 1
            if len(self.queue) >= self.capacity:
                evicted = self.queue.pop(0)
            self.queue.append(page)
        return list(self.queue), evicted, hit

    def get_stats(self):
        return self.hits, self.misses
