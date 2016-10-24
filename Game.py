from CFBoard import *
from History import *
import sys
import random
import time

# to play the game, type "Game().new()" into the command prompt

class Game:
    
    def __init__(self):
        self.board = CFBoard()
        self.maxDepth = 5 # actual total depth is +2
        self.compFirst = False
        self.data = History()
        self.data.load()
        self.ticks = 0
        self.time = 0
    
    def new(self,compFirst = False):
        self.compFirst = compFirst
        print self.board
        if compFirst == True:
            col = self.getCompMove()
            print '\nComputer plays column '+str(col)+'.'
            self.board.play(col,False)
            print self.board
        while True: # game loop
            # player's turn
            col = self.getInput()
            self.board.play(col,True)
            print self.board
            if self.board.hashedWinCheck(1):
                print '\nPlayer wins!'
                sys.exit()
            # computer's turn
            self.time = time.time()
            col = self.getCompMove()
            self.time = time.time() - self.time
            print '\nComputer plays column '+str(col)+'.'
            print 'Ticks: '+str(self.ticks)+', Time: '+str(round(self.time,2))+', T/s: '+str(round(self.ticks/self.time))
            self.ticks = 0
            self.board.play(col,False)
            print self.board
            if self.board.hashedWinCheck(2):
                print '\nComputer wins!'
                sys.exit()
        
    def getInput(self):
        playerInput = raw_input('Player move (X). Column: ')
        if playerInput.lower() in ['exit','quit','stop']:
            sys.exit()
        elif playerInput in str([0,1,2,3,4,5,6]):
            playerInput = int(playerInput)
            if self.board[0][playerInput] != 0:
                print 'That column is full. Please choose another.'
                return self.getInput()
            return playerInput
        print 'Unexpected input. Please input again.'
        return self.getInput()
    
    
    def playOptions(self):
        enum = []
        for i in range(len(self.board[0])):
            if self.board[0][i] == 0:
                enum.append(i)
        return enum
    
    
    def getCompMove(self):
        value = {}
        for move in self.playOptions():
            self.board.play(move, False)
            value[move] = self.value(False,0)
            self.board.erase(move)
        testOutput = ""
        for key in value:
            testOutput += str(key)+": "+str(round(value[key],2))+" "
        print testOutput
        return min(value, key=value.get)
    
    
    def deepValue(self, maxToMove):
        # how well have we done from this position in the past?
        # should we rely on that data?
        if compFirst:
            keyString = self.getKeyString(2)
        else:
            keyString = self.getKeyString(1)
        if self.data.exists(keyString):
            value = (self.data.getWinProb(keyString) - 0.5)*100
            if maxToMove: # if this is a good position, then return positive value
                return value
            else:
                return -value
        return 0
        
        
    def value(self, maxToMove, depth):
        self.ticks += 1
        # maxToMove? => max just played
        # terminal position? 
        # position can only be (non-depth) terminal if previous player made winning move
        lastToPlay = maxToMove*1 + 1 # this and
        if self.board.hashedWinCheck(lastToPlay):
            return (100-depth)*(3-2*lastToPlay) # this is really ugly
        elif depth > self.maxDepth:
            return random.random()*2 - 1 # self.board.positionValue()
            
        options = []
        for move in self.playOptions(): # opponent's response options
            self.board.play(move, not maxToMove)
            options.append( self.value(not maxToMove, depth + 1) )
            self.board.erase(move)
            
        if maxToMove:
            return min(options) # opponent is min; he chooses lowest value
        else:
            return max(options)