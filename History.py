# connect 4 database of past games for learning

# from collections import defaultdict
import cPickle as pickle

class History:
    
    def __init__(self):
        self.data = {} # struct: data[keyString] = (# wins, # played)
        self.queue = []
    
    def __str__(self):
        return str(self.data)
        
    def add(self, keyString):
       self.queue.append(keyString)
    
    def file(self, win):
        # if stage n was "win", then n-1 is "lose", and n-2 is "win" ...
        for item in reversed(self.queue):
            try:
                self.data[item] = (win*1+self.data[item][0],1+self.data[item][1])
            except KeyError:
                self.data[item] = (win*1, 1)
            win = not win
        self.queue = []
    
    def exists(self, keyString):
        return keyString in self.data
    
    def getWinProb(self, keyString):
        return self.data[keyString][0]/float(self.data[keyString][1])
        
    def getCount(self, keyString):
        return self.data[keyString][1]
        
    def load(self):
        self = pickle.load( open( "database.p", "rb" ) )
        
    def save(self):
        pickle.dump(self, open( "database.p", "wb" ) )