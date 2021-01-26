# Class that implements a hash table and handles collisions via prob
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [None for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        # If item does not exists, just return
        if self.arr[h] is None:
            return
        prob_range = self.get_prob_range(h)
        for prob_index in prob_range:
            element = self.arr[prob_range]
            # If it is neither on the next lookup
            if element is None:
                return
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        if self.arr[h] is None:
            self.arr[h] = (key, value)
        else:
            new_h = self.find_slot(key, h)
            self.arr[new_h] = (key, value)

    def __delitem__(self, key):
        h = self.get_hash(key)
        if self.arr[h] is not None and self.arr[h][0] == key:
            self.arr[h] = None
        else:
            prob_range = self.get_prob_range(h)
            for prob_index in prob_range:
                if self.arr[prob_index] is not None:
                    if self.arr[prob_index][0] == key:
                        self.arr[prob_index] = None
                        break

    def get_prob_range(self, index):
        # *range function returns a list of numbers in range(x,y), return joins both ranges results
        return [*range(index, len(self.arr))] + [*range(0, index)]

    def find_slot(self, key, index):
        prob_range = self.get_prob_range(index)
        for prob_index in prob_range:
            if self.arr[prob_index] is None:
                return prob_index
            if self.arr[prob_index][0] == key:
                return prob_index
        raise Exception("Hashmap full")

    def print(self):
        for i in range(self.MAX):
            print(self.arr[i])


t = HashTable()
t["march 6"] = 20
t["march 17"] = 88
t["march 17"] = 29
t["nov 1"] = 1
del t["march 17"]
del t["nov 1"]
t["May 22"] = 4
t["april 4"] = 91
t["april 3"] = 234234
t["march 17"] = 29
t["nov 1"] = 1
t.print()
