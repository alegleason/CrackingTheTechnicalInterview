# Class that implements a hash table and handles collisions via linked list
class HashTable:
    def __init__(self):
        self.MAX = 10
        self.arr = [[] for i in range(self.MAX)]

    def get_hash(self, key):
        h = 0
        for char in key:
            h += ord(char)
        return h % self.MAX

    def __getitem__(self, key):
        h = self.get_hash(key)
        # what is most probable is that it only has one element
        for element in self.arr[h]:
            if element[0] == key:
                return element[1]

    def __setitem__(self, key, value):
        h = self.get_hash(key)
        found = False
        # enumerate allows us to loop over something and have an automatic counter.
        for counter, element in enumerate(self.arr[h]):
            # if the tuple exists and key matches
            if len(element) == 2 and element[0] == key:
                # updating the tuple, counter allows us to check for other occurrences
                self.arr[h][counter] = (key, value)
                found = True
                break
        if not found:
            # appending the tuple
            self.arr[h].append((key, value))

    def __delitem__(self, key):
        h = self.get_hash(key)
        # what is most probable is that it only has one element
        for counter, element in enumerate(self.arr[h]):
            if len(element) == 2 and element[0] == key:
                # updating the tuple, counter allows us to check for other occurrences
                del self.arr[h][counter]
                break

    def print(self):
        for i in range(self.MAX):
            for element in self.arr[i]:
                print(element)


import re
# You indicate on the regex what you wanna keep
regex = re.compile('[^a-zA-Z]')
t = HashTable()
with open("poem.txt", "r") as file:
    for line in file:
        # split() defaults to split by ' '
        for word in line.split():
            word = regex.sub('', word)
            if t[word] is None:
                t[word] = 1
            else:
                val = int(t[word])
                val += 1
                t[word] = val
t.print()
