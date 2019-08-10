import random

class Node(object):
    def __init__(self, data, previous = None, next = None, above = None, below = None):
        self.data = data
        self.previous = previous
        self.next = next
        self.above = above
        self.below = below

class SkipList(object):
    def __init__(self):
        self.start = Node(data = float("-inf"))
        self.start.next = Node(data = float("inf"))
        self.start.next.previous = self.start
        self.num_elements = 0
        self.height = 1
    
    def coinFlip(self):
        return random.randint(0, 1)
    
    def skipSearch(self, value, show_results = True):
        p = self.start
        while p.below != None:
            p = p.below
            while value > p.next.data:
                p = p.next
        
        if show_results:
            if p.data == value:
                print("element is found")
                return
            if p.data < value:
                print("element does not found")
                return  

        return p        
    
    def skipInsert(self, value):
        p = self.skipSearch(value)
        q = None
        i = -1
        while self.coinFlip() == 1:
            i += 1
            if i >= self.height:
                self.height += 1
                t = self.start.next
                self.start = Node(data = float("-inf"), below = self.start)
                self.start.below.above = self.start
                t.above = Node(data = float("inf"), below = t)
                self.start.next = t.above
            while p.above != None:
                p = p.previous
                p = p.above
                q = Node(data = value, previous = p, next = p.next, below = q)
            self.num_elements += 1
        return q
    
    def skipDelete(self, value):
        p = skipSearch(value, show_results = False)
        if p.data == value:
            while p.below != None:
                p.previous.next = p.next
                p = p.below
        else:
            print("Item does not found")

sl = SkipList()
sl.skipInsert(2)
sl.skipInsert(3)
sl.skipInsert(5)
sl.skipInsert(7)
sl.skipSearch(7)
sl.skipSearch(5)
sl.skipDelete(7)
