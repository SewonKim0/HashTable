#linear probing
class HashTable:
    #constructor
    def __init__(self):
        #arr[pos] -> (key, val)
        self.arr = [None] * 8
        #len
        self.len = 0
        #fill
        self.fill = 0

    #add iterative(emptyFound, keyReplace), expand & rehash
    def add(self, key, val) -> None:
        #threshold 75%: expand arr
        if self.fill >= len(self.arr) * 0.75:
            #new arr
            newArr: list = [None] * (len(self.arr) * 2)
            #rehash all entries
            for entry in self.arr:
                #if empty: skip
                if entry == None:
                    continue
                (k, v) = entry
                #if tombstone: skip
                if k == None and v == None:
                    continue

                #get pos: shift until empty
                pos: int = hash(k) % len(newArr)
                while newArr[pos] != None:
                    pos = (pos + 1) % len(newArr)
                #place entry at pos
                newArr[pos] = (k, v)

            #set as self.arr
            self.arr = newArr
            #update fill
            self.fill = self.len

        #pos: shift til (empty, keyHit)
        pos: int = hash(key) % len(self.arr)
        while self.arr[pos] != None and self.arr[pos][0] != key:
            #update pos
            pos = (pos + 1) % len(self.arr)
        
        #if empty space
        if self.arr[pos] == None:
            self.arr[pos] = (key, val)
            #update len
            self.len += 1
            #update fill
            self.fill += 1
        #if key hit
        if self.arr[pos][0] == key:
            self.arr[pos] = (key, val)

    #get
    def get(self, key):
        #get pos: shift til (keyHit, empty)
        pos: int = hash(key) % len(self.arr)
        while self.arr[pos] != None and self.arr[pos][0] != key:
            pos = (pos + 1) % len(self.arr)
        
        #if not found
        if self.arr[pos] == None:
            return None
        #if found
        if self.arr[pos][0] == key:
            return self.arr[pos][1]
        
    #remove
    def remove(self, key) -> None:
        #get pos: shift til (keyHit, empty), skip tombstones
        pos: int = hash(key) % len(self.arr)
        while self.arr[pos] == (None, None) or (self.arr[pos] != None and self.arr[pos][0] != key):
            pos = (pos + 1) % len(self.arr)
        
        #if empty: error
        if self.arr[pos] == None:
            raise IndexError("Error: Entry does not exist")
        #if keyHit: replace with tombstone
        if self.arr[pos][0] == key:
            self.arr[pos] = (None, None)
            #update len
            self.len -= 1
    
    #clear
    def clear(self):
        self.arr = [None] * 8
        self.len = 0
        self.fill = 0

    #len()
    def __len__(self) -> int:
        return self.len
    
    #toString()
    def __repr__(self) -> str:
        return str(self.arr) + " Len: " + str(self.len) + " Fill: " + str(self.fill)
    
table: HashTable = HashTable()
# Methods:
    # table.add(key, val)
    # table.get(key) -> val
    # table.remove(key)
    # table.clear()
    # len(table) -> int
    # print(table) DISPLAY INTERNAL TABLE

# # TEST3: added expand, (add, get, remove, len)
# # add(atCapacity, afterCapacity)
# table.add(3, 5)
# table.add(3, 3)
# table.add(11, 11)
# table.add(0, 7)
# table.add(1, 2)
# table.add(8, 3)
# table.add(9, 1)
# table.add(7, 7)
# table.add(19, 19)
# # remove(atCapacity, afterCapacity)
# table.remove(8)
# table.remove(9)
# print(table) #[(0, 7), (1, 2), None, (3, 3), (19, 19), None, None, (7, 7), (None, None), (None, None), None, (11, 11), None, None, None, None]
# table.remove(1)
# table.remove(7)
# print(table) #[(0, 7), (None, None), None, (3, 3), (19, 19), None, None, (None, None), (None, None), (None, None), None, (11, 11), None, None, None, None]
# table.clear()
# table.add(0, 0)
# table.add(1, 1)
# table.add(3, 3)
# table.add(4, 4)
# table.add(5, 5)
# table.add(6, 6)
# table.remove(5)
# print(table) #[(0, 0), (1, 1), None, (3, 3), (4, 4), (None, None), (6, 6), None] Len: 5, Fill: 6
# table.add(2, 2)
# print(table) #[(0, 0), (1, 1), (2, 2), (3, 3), (4, 4), (None, None), (6, 6), None, None, None, None, None, None, None, None, None] Len: 6 Fill: 6

# #TEST2 (add, get, remove, clear) added tombstones
# #add (hitFirst, hitNexts, updateFirst, updateNexts)
# table.add(3, 5)
# table.add(11, 8)
# table.add(3, 7)
# table.add(11, 12)
# #remove (missFirst, missNexts, hitFirst, hitNexts)
# table.remove(3)
# table.remove(11)
# print(table) #[n, n, n, (None, None), (None, None), n, n, n]
# #add (tombstoneFirst, tombstoneMid)
# table.add(4, 7)
# print(table) #[n, n, n, (None, None), (None, None), (4, 7), n, n]
# table.add(2, 3)
# table.add(2, 2)
# table.add(10, 10)
# print(table) #[n, n, (2, 2), (None, None), (None, None), (4, 7), (10, 10), n]
# print(len(table)) #3
# table.clear()
# print(table) #[n, n, n, n, n, n, n, n]
# print(len(table)) #0
# #get (tombstoneFirst, tombstoneMid)

# #TEST1 (add, get)
# #add (hitFirst, hitNexts, updateFirst, updateNexts)
# table.add(3, 5)
# print(table) #[n, n, n, (3, 5), n, n, n, n]
# table.add(11, 8)
# print(table) #[n, n, n, (3, 5), (11, 8), n, n, n]
# table.add(3, 7)
# print(table) #[n, n, n, (3, 7), (11, 8), n, n, n]
# table.add(11, 12)
# print(table) #[n, n, n, (3, 7), (11, 12), n, n, n]
# #get (missFirst, missNexts, hitFirst, hitNexts)
# print(table.get(1)) #None
# print(table.get(19)) #None
# print(table.get(3)) #7
# print(table.get(11)) #12