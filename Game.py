from CFBoard import *
from History import *
import sys
import random
import time
import cPickle as pickle

# to play the game, type "Game().new()" into the command prompt

class Game:
    
    def __init__(self):
        self.board = CFBoard()
        self.maxDepth = 4 # actual total depth is +2
        self.compFirst = False
        self.transpositions = {}
        # self.data = History()
        self.data = pickle.load( open( "database.p", "rb" ) )
        self.ticks = 0
        self.time = 0
    
    def new(self,compFirst = False):
        self.compFirst = compFirst
        self.data.queue = []
        print self.board
        if compFirst == True:
            col = self.getCompMove()
            print '\nComputer plays column '+str(col)+'.'
            self.board.play(col,False)
            self.data.add(self.board.keyString)
            print self.board
        while True: # game loop
            # player's turn
            col = self.getInput()
            self.board.play(col,True)
            self.data.add(self.board.keyString)
            print self.board
            if self.board.hashedWinCheck(1):
                print '\nPlayer wins!'
                self.data.file()
                self.data.save()
                sys.exit()
            # computer's turn
            self.time = time.time()
            col = self.getCompMove()
            self.time = time.time() - self.time
            if self.time < 1:
                self.maxDepth += 1
            print '\nComputer plays column '+str(col)+'.'
            print 'Ticks: '+str(self.ticks)+', Time: '+str(round(self.time,2))+', T/s: '+str(round(self.ticks/self.time))
            self.ticks = 0
            self.board.play(col,False)
            self.data.add(self.board.keyString)
            print self.board
            if self.board.hashedWinCheck(2):
                print '\nComputer wins!'
                self.data.file()
                self.data.save()
                sys.exit()
    
    def playWithSelf(self, timeToRun, display = False):
        end = timeToRun + time.time()
        while time.time() < end:
            self.compVcomp(display)
            self.board = CFBoard() # clear board
            
    def compVcomp(self, display = False):
        self.compFirst = False # play
        self.data.queue = []
        if display: print self.board
        while True: # game loop
            # Comp A's turn
            col = self.getPlayerMove()
            self.board.play(col,True)
            self.data.add(self.board.keyString)
            if display: print self.board
            if self.board.hashedWinCheck(1) or self.board.tieCheck(): # QUESTIONABLE
                self.data.file()
                self.data.save()
                print 'A'
                return    
            # Comp B's turn
            self.time = time.time()
            col = self.getCompMove()
            self.time = time.time() - self.time
            if self.time < 1:
                self.maxDepth += 1
            self.board.play(col,False)
            self.data.add(self.board.keyString)
            if display: print self.board
            if self.board.hashedWinCheck(2) or self.board.tieCheck(): # QUESTIONABLE
                self.data.file()
                self.data.save()
                print 'B'
                return
        
        
        
    def getInput(self):
        playerInput = raw_input('Player move (X). Column: ')
        if playerInput.lower() in ['exit','quit','stop']:
            sys.exit()
        elif playerInput.lower() in ['hint', 'help']:
            print 'You could try column '+str(self.getPlayerMove())+'.'
        elif playerInput in str([0,1,2,3,4,5,6]):
            playerInput = int(playerInput)
            if self.board[0][playerInput] != 0:
                print 'That column is full. Please choose another.'
                return self.getInput()
            return playerInput
        print 'Unexpected input. Please input again.'
        return self.getInput()
    
    def getPlayerMove(self): # player is also comp
        value = {}
        for move in self.board.playOptions():
            self.board.play(move, True)
            value[move] = self.alphaBeta(-1000,1000,False,0) # value[move] = self.value(True,0)
            self.board.erase(move)
        #testOutput = ""
        #for key in value:
        #    testOutput += str(key)+": "+str(round(value[key],2))+" "
        #print testOutput
        return max(value, key=value.get)
    
    def getCompMove(self):
        value = {}
        for move in self.board.playOptions():
            self.board.play(move, False)
            value[move] = self.alphaBeta(-1000,1000,True,0) # value[move] = self.value(False,0)
            self.board.erase(move)
        testOutput = "SD: "+str(self.maxDepth+2)+", "
        for key in value:
            testOutput += str(key)+": "+str(round(value[key],2))+" "
        print testOutput
        return min(value, key=value.get)
    
    #def getKeyString(self):
    #    key = ""
    #    for r in range(len(self.board)-1,-1,-1):
    #        for c in range(len(self.board[0])):
    #            if not self.compFirst:
    #                key += str(self.board[r][c])
    #            else:
    #                key += str(3-self.board[r][c]) # if first player was 2, then swap 1 and 2
    #    return key        
    
    def deepValue(self, maxToMove):
        # how well have we done from this position in the past?
        # should we rely on that data?
        if self.data.exists(self.board.keyString):
            value = (self.data.getWinProb(self.board.keyString) - 0.5)*100
            if maxToMove: # if this is a good position, then return positive value
                return value
            else:
                return -value
        return random.random()*2-1 # to avoild obvious leftside bias
        
        
    def value(self, maxToMove, depth):
        self.ticks += 1
        # maxToMove? => max just played
        # terminal position? 
        # position can only be (non-depth) terminal if previous player made winning move
        lastToPlay = maxToMove*1 + 1 # this and
        if self.board.hashedWinCheck(lastToPlay):
            return (100-depth)*(3-2*lastToPlay) # this is really ugly
        if depth > self.maxDepth:
            return self.board.positionValue() # return self.deepValue(maxToMove) # random.random()*2 - 1
        if self.board.tieCheck():
            return 0
        
        options = []
        for move in self.board.playOptions(): # opponent's response options
            self.board.play(move, not maxToMove)
            options.append( self.value(not maxToMove, depth + 1) )
            self.board.erase(move)
            
        if maxToMove:
            return min(options) # opponent is min; he chooses lowest value
        else:
            return max(options)
    
    def alphaBeta(self, alpha, beta, maxToMove, depth):
        lastToPlay = maxToMove*1 + 1 # this and
        if self.board.hashedWinCheck(lastToPlay):
            return (100-depth)*(3-2*lastToPlay) # this is really ugly
        if depth > self.maxDepth:
            return self.board.positionValue() # return self.deepValue(maxToMove) # random.random()*2 - 1
        if depth == 0:
            self.transpositions = {}
        if self.board.keyString in self.transpositions:
            return self.transpositions[self.board.keyString]
        if self.board.tieCheck():
            return 0
        self.ticks += 1
        
        # note alpha & beta are renewed at each node (values not passed up)
        if maxToMove:
            v = -1000
            for move in self.board.playOptions():
                self.board.play(move, maxToMove)
                v = max(v, self.alphaBeta(alpha, beta, not maxToMove, depth + 1))
                alpha = max(alpha,v)
                self.transpositions[self.board.keyString] = v
                self.board.erase(move)
                if beta <= alpha:
                    break
            return v
        else:
            v = 1000
            for move in self.board.playOptions(): # min's response options
                self.board.play(move, maxToMove)
                v = min(v, self.alphaBeta(alpha, beta, not maxToMove, depth + 1))
                beta = min(beta,v)
                self.transpositions[self.board.keyString] = v
                self.board.erase(move)
                if beta <= alpha:
                    break
            return v