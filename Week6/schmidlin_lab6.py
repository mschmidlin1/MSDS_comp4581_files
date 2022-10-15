

class MyHashtable(object):
    def __init__(self, size): # Creates an empty hashtable
        self.size = size
        self.table = [None] * self.size
        self.status = ['empty'] * self.size
    def __str__(self): # for print
        return str(self.table)

    def hash(self, string):
        return ord(string[0]) % self.size

    def insert(self, elem): # Adds an element into the hashtable
        hash = self.hash(elem)
        for i in range(hash, self.size):
                if self.status[i] in ['empty', 'deleted']:
                    self.table[i]=elem
                    self.status[i]='filled'
                    return True
        for i in range(0, hash):
                if self.status[i] in ['empty', 'deleted']:
                    self.table[i]=elem
                    self.status[i]='filled'
                    return True
        raise("Not enough positions in hash table.")

    def member(self, elem): # Returns if element exists in hashtable
        hash = self.hash(elem)
        for i in range(hash, self.size):
                if self.status[i] == 'empty':
                    return False
                if self.table[i]==elem:
                    return True
        for i in range(0, hash):
                if self.status[i] == 'empty':
                    return False
                if self.table[i]==elem:
                    return True     
        raise("WHATTT")
    def delete(self, elem): # Removes an element from the hashtable
        hash = self.hash(elem)

        for i in range(hash, self.size):
                if self.status[i] == 'empty':
                    return False
                if self.table[i]==elem:
                    self.table[i]=None
                    self.status[i]='deleted'
                    return True
        for i in range(0, hash):
                if self.status[i] == 'empty':
                    return False
                if self.table[i]==elem:
                    self.table[i]=None
                    self.status[i]='deleted'
                    return True  
        raise("WHATTT")









def main():
    pass







if __name__=="__main__":
    main()