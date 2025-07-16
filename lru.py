class LRU_Cache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.pages = []
        self.hits = 0
        self.misses = 0

    def access(self, page):
        hit = page in self.pages
        evicted = None
        if hit:
            self.hits += 1
            self.pages.remove(page)
            self.pages.append(page)
        else:
            self.misses += 1
            if len(self.pages) >= self.capacity:
                evicted = self.pages.pop(0)
            self.pages.append(page)
        return list(self.pages), evicted, hit

    def get_stats(self):
        return self.hits, self.misses