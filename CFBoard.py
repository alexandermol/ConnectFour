# connect 4 game & AI

class CFBoard:
    
    def __init__(self):
        self.board = []
        self.keyString = "000000000000000000000000000000000000000000"
        self.groundLevel = [5,5,5,5,5,5,5]
        for i in range(6):
            row = []
            for i in range(7):
                row.append(0)
            self.board.append(row)
    
    def __getitem__(self,i):
        return self.board[i]
        
    def __len__(self):
        return len(self.board)
    
    def __str__(self):
        output = ""
        for row in self.board:
            for item in row:
                if item == 0:
                    output += ". "
                elif item == 1:
                    output += "X "
                elif item == 2:
                    output += "O "
            output += '\n'
        output += '-------------\n'
        for i in range(len(self.board[0])):
            output += str(i) + " "
        return output
    
    def updateKeyString(self, r, c, v):
        pos = (5-r)*7 + c
        self.keyString = self.keyString[:pos]+str(v)+self.keyString[pos+1:]
    
    def play(self, c, maxToMove):
        if maxToMove:
            v = 1
        else:
            v = 2
        if c < 0 or c > 6:
            print 'Asked to play down column '+str(c)+'. Can\'t do that.'
            return
        if self.board[0][c] != 0:
            print 'This column is full.'
            return
        r = self.groundLevel[c]
        self.board[r][c] = v
        self.updateKeyString(r,c,v)
        self.groundLevel[c] -= 1
    
    def erase(self, c):
        r = self.groundLevel[c]
        self.board[r+1][c] = 0
        self.updateKeyString(r+1,c,0)
        self.groundLevel[c] += 1
        
    def playOptions(self):
        enum = []
        for i in [3,2,4,1,5,0,6]:
            if self.board[0][i] == 0:
                enum.append(i)
        return enum
    
    def tieCheck(self):
        if self.playOptions() == []:
            return True
        return False
    
    def winCondition(self):
        h = len(self.board)
        w = len(self.board[0])
        # vertical
        for r in range(h-3):
            for c in range(w):
                sequence = ""
                for i in range(4):
                    sequence += str(self.board[r+i][c])
                if sequence == "1111":
                    return 1
                if sequence == "2222":
                    return 2
        # horizontal
        for r in range(h):
            for c in range(w-3):
                sequence = ""
                for i in range(4):
                    sequence += str(self.board[r][c+i])
                if sequence == "1111":
                    return 1
                if sequence == "2222":
                    return 2
        # diagonal \
        for r in range(h-3):
            for c in range(w-3):
                sequence = ""
                for i in range(4):
                    sequence += str(self.board[r+i][c+i])
                if sequence == "1111":
                    return 1
                if sequence == "2222":
                    return 2
        # diagonal /
        for r in range(h-3):
            for c in range(w-3):
                sequence = ""
                for i in range(4):
                    sequence += str(self.board[r+3-i][c+i])
                if sequence == "1111":
                    return 1
                if sequence == "2222":
                    return 2
    
    def hashedWinCheck(self,player):
        b = self.board
        p = player
        # vertical
        if b[0][0] == p and b[1][0] == p and b[2][0] == p and b[3][0] == p: 
            return True
        if b[0][1] == p and b[1][1] == p and b[2][1] == p and b[3][1] == p: 
            return True
        if b[0][2] == p and b[1][2] == p and b[2][2] == p and b[3][2] == p: 
            return True
        if b[0][3] == p and b[1][3] == p and b[2][3] == p and b[3][3] == p: 
            return True
        if b[0][4] == p and b[1][4] == p and b[2][4] == p and b[3][4] == p: 
            return True
        if b[0][5] == p and b[1][5] == p and b[2][5] == p and b[3][5] == p: 
            return True
        if b[0][6] == p and b[1][6] == p and b[2][6] == p and b[3][6] == p: 
            return True
        if b[1][0] == p and b[2][0] == p and b[3][0] == p and b[4][0] == p: 
            return True
        if b[1][1] == p and b[2][1] == p and b[3][1] == p and b[4][1] == p: 
            return True
        if b[1][2] == p and b[2][2] == p and b[3][2] == p and b[4][2] == p: 
            return True
        if b[1][3] == p and b[2][3] == p and b[3][3] == p and b[4][3] == p: 
            return True
        if b[1][4] == p and b[2][4] == p and b[3][4] == p and b[4][4] == p: 
            return True
        if b[1][5] == p and b[2][5] == p and b[3][5] == p and b[4][5] == p: 
            return True
        if b[1][6] == p and b[2][6] == p and b[3][6] == p and b[4][6] == p: 
            return True
        if b[2][0] == p and b[3][0] == p and b[4][0] == p and b[5][0] == p: 
            return True
        if b[2][1] == p and b[3][1] == p and b[4][1] == p and b[5][1] == p: 
            return True
        if b[2][2] == p and b[3][2] == p and b[4][2] == p and b[5][2] == p: 
            return True
        if b[2][3] == p and b[3][3] == p and b[4][3] == p and b[5][3] == p: 
            return True
        if b[2][4] == p and b[3][4] == p and b[4][4] == p and b[5][4] == p: 
            return True
        if b[2][5] == p and b[3][5] == p and b[4][5] == p and b[5][5] == p: 
            return True
        if b[2][6] == p and b[3][6] == p and b[4][6] == p and b[5][6] == p: 
            return True
        # horizontal
        if b[0][0] == p and b[0][1] == p and b[0][2] == p and b[0][3] == p: 
            return True
        if b[0][1] == p and b[0][2] == p and b[0][3] == p and b[0][4] == p: 
            return True
        if b[0][2] == p and b[0][3] == p and b[0][4] == p and b[0][5] == p: 
            return True
        if b[0][3] == p and b[0][4] == p and b[0][5] == p and b[0][6] == p: 
            return True
        if b[1][0] == p and b[1][1] == p and b[1][2] == p and b[1][3] == p: 
            return True
        if b[1][1] == p and b[1][2] == p and b[1][3] == p and b[1][4] == p: 
            return True
        if b[1][2] == p and b[1][3] == p and b[1][4] == p and b[1][5] == p: 
            return True
        if b[1][3] == p and b[1][4] == p and b[1][5] == p and b[1][6] == p: 
            return True
        if b[2][0] == p and b[2][1] == p and b[2][2] == p and b[2][3] == p: 
            return True
        if b[2][1] == p and b[2][2] == p and b[2][3] == p and b[2][4] == p: 
            return True
        if b[2][2] == p and b[2][3] == p and b[2][4] == p and b[2][5] == p: 
            return True
        if b[2][3] == p and b[2][4] == p and b[2][5] == p and b[2][6] == p: 
            return True
        if b[3][0] == p and b[3][1] == p and b[3][2] == p and b[3][3] == p: 
            return True
        if b[3][1] == p and b[3][2] == p and b[3][3] == p and b[3][4] == p: 
            return True
        if b[3][2] == p and b[3][3] == p and b[3][4] == p and b[3][5] == p: 
            return True
        if b[3][3] == p and b[3][4] == p and b[3][5] == p and b[3][6] == p: 
            return True
        if b[4][0] == p and b[4][1] == p and b[4][2] == p and b[4][3] == p: 
            return True
        if b[4][1] == p and b[4][2] == p and b[4][3] == p and b[4][4] == p: 
            return True
        if b[4][2] == p and b[4][3] == p and b[4][4] == p and b[4][5] == p: 
            return True
        if b[4][3] == p and b[4][4] == p and b[4][5] == p and b[4][6] == p: 
            return True
        if b[5][0] == p and b[5][1] == p and b[5][2] == p and b[5][3] == p: 
            return True
        if b[5][1] == p and b[5][2] == p and b[5][3] == p and b[5][4] == p: 
            return True
        if b[5][2] == p and b[5][3] == p and b[5][4] == p and b[5][5] == p: 
            return True
        if b[5][3] == p and b[5][4] == p and b[5][5] == p and b[5][6] == p: 
            return True
        # diagonal \
        if b[0][0] == p and b[1][1] == p and b[2][2] == p and b[3][3] == p: 
            return True
        if b[0][1] == p and b[1][2] == p and b[2][3] == p and b[3][4] == p: 
            return True
        if b[0][2] == p and b[1][3] == p and b[2][4] == p and b[3][5] == p: 
            return True
        if b[0][3] == p and b[1][4] == p and b[2][5] == p and b[3][6] == p: 
            return True
        if b[1][0] == p and b[2][1] == p and b[3][2] == p and b[4][3] == p: 
            return True
        if b[1][1] == p and b[2][2] == p and b[3][3] == p and b[4][4] == p: 
            return True
        if b[1][2] == p and b[2][3] == p and b[3][4] == p and b[4][5] == p: 
            return True
        if b[1][3] == p and b[2][4] == p and b[3][5] == p and b[4][6] == p: 
            return True
        if b[2][0] == p and b[3][1] == p and b[4][2] == p and b[5][3] == p: 
            return True
        if b[2][1] == p and b[3][2] == p and b[4][3] == p and b[5][4] == p: 
            return True
        if b[2][2] == p and b[3][3] == p and b[4][4] == p and b[5][5] == p: 
            return True
        if b[2][3] == p and b[3][4] == p and b[4][5] == p and b[5][6] == p: 
            return True
        # diagonal /
        if b[3][0] == p and b[2][1] == p and b[1][2] == p and b[0][3] == p: 
            return True
        if b[3][1] == p and b[2][2] == p and b[1][3] == p and b[0][4] == p: 
            return True
        if b[3][2] == p and b[2][3] == p and b[1][4] == p and b[0][5] == p: 
            return True
        if b[3][3] == p and b[2][4] == p and b[1][5] == p and b[0][6] == p: 
            return True
        if b[4][0] == p and b[3][1] == p and b[2][2] == p and b[1][3] == p: 
            return True
        if b[4][1] == p and b[3][2] == p and b[2][3] == p and b[1][4] == p: 
            return True
        if b[4][2] == p and b[3][3] == p and b[2][4] == p and b[1][5] == p: 
            return True
        if b[4][3] == p and b[3][4] == p and b[2][5] == p and b[1][6] == p: 
            return True
        if b[5][0] == p and b[4][1] == p and b[3][2] == p and b[2][3] == p: 
            return True
        if b[5][1] == p and b[4][2] == p and b[3][3] == p and b[2][4] == p: 
            return True
        if b[5][2] == p and b[4][3] == p and b[3][4] == p and b[2][5] == p: 
            return True
        if b[5][3] == p and b[4][4] == p and b[3][5] == p and b[2][6] == p: 
            return True
        
        return False
        
        
    # ==============================================================================
    def positionValue(self):
        scoreMax = self.hashedPositionPoints(True)
        scoreMin = self.hashedPositionPoints(False)
        return scoreMax - scoreMin
    
    def hashedPositionPoints(self, maxToPlay):
        # heuristic score calculation
        b = self.board
        if maxToPlay:
            p = 1
            o = 2
        else:
            p = 2
            o = 1
        score = 0
        
        # vertical
        if b[0][0] != o and b[1][0] != o and b[2][0] != o and b[3][0] != o and (b[0][0] == p or b[1][0] == p or b[2][0] == p or b[3][0] == p): 
            score += 1
        if b[0][1] != o and b[1][1] != o and b[2][1] != o and b[3][1] != o and (b[0][1] == p or b[1][1] == p or b[2][1] == p or b[3][1] == p): 
            score += 1
        if b[0][2] != o and b[1][2] != o and b[2][2] != o and b[3][2] != o and (b[0][2] == p or b[1][2] == p or b[2][2] == p or b[3][2] == p): 
            score += 1
        if b[0][3] != o and b[1][3] != o and b[2][3] != o and b[3][3] != o and (b[0][3] == p or b[1][3] == p or b[2][3] == p or b[3][3] == p): 
            score += 1
        if b[0][4] != o and b[1][4] != o and b[2][4] != o and b[3][4] != o and (b[0][4] == p or b[1][4] == p or b[2][4] == p or b[3][4] == p): 
            score += 1
        if b[0][5] != o and b[1][5] != o and b[2][5] != o and b[3][5] != o and (b[0][5] == p or b[1][5] == p or b[2][5] == p or b[3][5] == p): 
            score += 1
        if b[0][6] != o and b[1][6] != o and b[2][6] != o and b[3][6] != o and (b[0][6] == p or b[1][6] == p or b[2][6] == p or b[3][6] == p): 
            score += 1
        if b[1][0] != o and b[2][0] != o and b[3][0] != o and b[4][0] != o and (b[1][0] == p or b[2][0] == p or b[3][0] == p or b[4][0] == p): 
            score += 1
        if b[1][1] != o and b[2][1] != o and b[3][1] != o and b[4][1] != o and (b[1][1] == p or b[2][1] == p or b[3][1] == p or b[4][1] == p): 
            score += 1
        if b[1][2] != o and b[2][2] != o and b[3][2] != o and b[4][2] != o and (b[1][2] == p or b[2][2] == p or b[3][2] == p or b[4][2] == p): 
            score += 1
        if b[1][3] != o and b[2][3] != o and b[3][3] != o and b[4][3] != o and (b[1][3] == p or b[2][3] == p or b[3][3] == p or b[4][3] == p): 
            score += 1
        if b[1][4] != o and b[2][4] != o and b[3][4] != o and b[4][4] != o and (b[1][4] == p or b[2][4] == p or b[3][4] == p or b[4][4] == p): 
            score += 1
        if b[1][5] != o and b[2][5] != o and b[3][5] != o and b[4][5] != o and (b[1][5] == p or b[2][5] == p or b[3][5] == p or b[4][5] == p): 
            score += 1
        if b[1][6] != o and b[2][6] != o and b[3][6] != o and b[4][6] != o and (b[1][6] == p or b[2][6] == p or b[3][6] == p or b[4][6] == p): 
            score += 1
        if b[2][0] != o and b[3][0] != o and b[4][0] != o and b[5][0] != o and (b[2][0] == p or b[3][0] == p or b[4][0] == p or b[5][0] == p): 
            score += 1
        if b[2][1] != o and b[3][1] != o and b[4][1] != o and b[5][1] != o and (b[2][1] == p or b[3][1] == p or b[4][1] == p or b[5][1] == p): 
            score += 1
        if b[2][2] != o and b[3][2] != o and b[4][2] != o and b[5][2] != o and (b[2][2] == p or b[3][2] == p or b[4][2] == p or b[5][2] == p): 
            score += 1
        if b[2][3] != o and b[3][3] != o and b[4][3] != o and b[5][3] != o and (b[2][3] == p or b[3][3] == p or b[4][3] == p or b[5][3] == p): 
            score += 1
        if b[2][4] != o and b[3][4] != o and b[4][4] != o and b[5][4] != o and (b[2][4] == p or b[3][4] == p or b[4][4] == p or b[5][4] == p): 
            score += 1
        if b[2][5] != o and b[3][5] != o and b[4][5] != o and b[5][5] != o and (b[2][5] == p or b[3][5] == p or b[4][5] == p or b[5][5] == p): 
            score += 1
        if b[2][6] != o and b[3][6] != o and b[4][6] != o and b[5][6] != o and (b[2][6] == p or b[3][6] == p or b[4][6] == p or b[5][6] == p): 
            score += 1
        # horizontal
        if b[0][0] != o and b[0][1] != o and b[0][2] != o and b[0][3] != o and (b[0][0] == p or b[0][1] == p or b[0][2] == p or b[0][3] == p): 
            score += 1
        if b[0][1] != o and b[0][2] != o and b[0][3] != o and b[0][4] != o and (b[0][1] == p or b[0][2] == p or b[0][3] == p or b[0][4] == p): 
            score += 1
        if b[0][2] != o and b[0][3] != o and b[0][4] != o and b[0][5] != o and (b[0][2] == p or b[0][3] == p or b[0][4] == p or b[0][5] == p): 
            score += 1
        if b[0][3] != o and b[0][4] != o and b[0][5] != o and b[0][6] != o and (b[0][3] == p or b[0][4] == p or b[0][5] == p or b[0][6] == p): 
            score += 1
        if b[1][0] != o and b[1][1] != o and b[1][2] != o and b[1][3] != o and (b[1][0] == p or b[1][1] == p or b[1][2] == p or b[1][3] == p): 
            score += 1
        if b[1][1] != o and b[1][2] != o and b[1][3] != o and b[1][4] != o and (b[1][1] == p or b[1][2] == p or b[1][3] == p or b[1][4] == p): 
            score += 1
        if b[1][2] != o and b[1][3] != o and b[1][4] != o and b[1][5] != o and (b[1][2] == p or b[1][3] == p or b[1][4] == p or b[1][5] == p): 
            score += 1
        if b[1][3] != o and b[1][4] != o and b[1][5] != o and b[1][6] != o and (b[1][3] == p or b[1][4] == p or b[1][5] == p or b[1][6] == p): 
            score += 1
        if b[2][0] != o and b[2][1] != o and b[2][2] != o and b[2][3] != o and (b[2][0] == p or b[2][1] == p or b[2][2] == p or b[2][3] == p): 
            score += 1
        if b[2][1] != o and b[2][2] != o and b[2][3] != o and b[2][4] != o and (b[2][1] == p or b[2][2] == p or b[2][3] == p or b[2][4] == p): 
            score += 1
        if b[2][2] != o and b[2][3] != o and b[2][4] != o and b[2][5] != o and (b[2][2] == p or b[2][3] == p or b[2][4] == p or b[2][5] == p): 
            score += 1
        if b[2][3] != o and b[2][4] != o and b[2][5] != o and b[2][6] != o and (b[2][3] == p or b[2][4] == p or b[2][5] == p or b[2][6] == p): 
            score += 1
        if b[3][0] != o and b[3][1] != o and b[3][2] != o and b[3][3] != o and (b[3][0] == p or b[3][1] == p or b[3][2] == p or b[3][3] == p): 
            score += 1
        if b[3][1] != o and b[3][2] != o and b[3][3] != o and b[3][4] != o and (b[3][1] == p or b[3][2] == p or b[3][3] == p or b[3][4] == p): 
            score += 1
        if b[3][2] != o and b[3][3] != o and b[3][4] != o and b[3][5] != o and (b[3][2] == p or b[3][3] == p or b[3][4] == p or b[3][5] == p): 
            score += 1
        if b[3][3] != o and b[3][4] != o and b[3][5] != o and b[3][6] != o and (b[3][3] == p or b[3][4] == p or b[3][5] == p or b[3][6] == p): 
            score += 1
        if b[4][0] != o and b[4][1] != o and b[4][2] != o and b[4][3] != o and (b[4][0] == p or b[4][1] == p or b[4][2] == p or b[4][3] == p): 
            score += 1
        if b[4][1] != o and b[4][2] != o and b[4][3] != o and b[4][4] != o and (b[4][1] == p or b[4][2] == p or b[4][3] == p or b[4][4] == p): 
            score += 1
        if b[4][2] != o and b[4][3] != o and b[4][4] != o and b[4][5] != o and (b[4][2] == p or b[4][3] == p or b[4][4] == p or b[4][5] == p): 
            score += 1
        if b[4][3] != o and b[4][4] != o and b[4][5] != o and b[4][6] != o and (b[4][3] == p or b[4][4] == p or b[4][5] == p or b[4][6] == p): 
            score += 1
        if b[5][0] != o and b[5][1] != o and b[5][2] != o and b[5][3] != o and (b[5][0] == p or b[5][1] == p or b[5][2] == p or b[5][3] == p): 
            score += 1
        if b[5][1] != o and b[5][2] != o and b[5][3] != o and b[5][4] != o and (b[5][1] == p or b[5][2] == p or b[5][3] == p or b[5][4] == p): 
            score += 1
        if b[5][2] != o and b[5][3] != o and b[5][4] != o and b[5][5] != o and (b[5][2] == p or b[5][3] == p or b[5][4] == p or b[5][5] == p): 
            score += 1
        if b[5][3] != o and b[5][4] != o and b[5][5] != o and b[5][6] != o and (b[5][3] == p or b[5][4] == p or b[5][5] == p or b[5][6] == p): 
            score += 1
        # diagonal \
        if b[0][0] != o and b[1][1] != o and b[2][2] != o and b[3][3] != o and (b[0][0] == p or b[1][1] == p or b[2][2] == p or b[3][3] == p): 
            score += 1
        if b[0][1] != o and b[1][2] != o and b[2][3] != o and b[3][4] != o and (b[0][1] == p or b[1][2] == p or b[2][3] == p or b[3][4] == p): 
            score += 1
        if b[0][2] != o and b[1][3] != o and b[2][4] != o and b[3][5] != o and (b[0][2] == p or b[1][3] == p or b[2][4] == p or b[3][5] == p): 
            score += 1
        if b[0][3] != o and b[1][4] != o and b[2][5] != o and b[3][6] != o and (b[0][3] == p or b[1][4] == p or b[2][5] == p or b[3][6] == p): 
            score += 1
        if b[1][0] != o and b[2][1] != o and b[3][2] != o and b[4][3] != o and (b[1][0] == p or b[2][1] == p or b[3][2] == p or b[4][3] == p): 
            score += 1
        if b[1][1] != o and b[2][2] != o and b[3][3] != o and b[4][4] != o and (b[1][1] == p or b[2][2] == p or b[3][3] == p or b[4][4] == p): 
            score += 1
        if b[1][2] != o and b[2][3] != o and b[3][4] != o and b[4][5] != o and (b[1][2] == p or b[2][3] == p or b[3][4] == p or b[4][5] == p): 
            score += 1
        if b[1][3] != o and b[2][4] != o and b[3][5] != o and b[4][6] != o and (b[1][3] == p or b[2][4] == p or b[3][5] == p or b[4][6] == p): 
            score += 1
        if b[2][0] != o and b[3][1] != o and b[4][2] != o and b[5][3] != o and (b[2][0] == p or b[3][1] == p or b[4][2] == p or b[5][3] == p): 
            score += 1
        if b[2][1] != o and b[3][2] != o and b[4][3] != o and b[5][4] != o and (b[2][1] == p or b[3][2] == p or b[4][3] == p or b[5][4] == p): 
            score += 1
        if b[2][2] != o and b[3][3] != o and b[4][4] != o and b[5][5] != o and (b[2][2] == p or b[3][3] == p or b[4][4] == p or b[5][5] == p): 
            score += 1
        if b[2][3] != o and b[3][4] != o and b[4][5] != o and b[5][6] != o and (b[2][3] == p or b[3][4] == p or b[4][5] == p or b[5][6] == p): 
            score += 1
        # diagonal /
        if b[3][0] != o and b[2][1] != o and b[1][2] != o and b[0][3] != o and (b[3][0] == p or b[2][1] == p or b[1][2] == p or b[0][3] == p): 
            score += 1
        if b[3][1] != o and b[2][2] != o and b[1][3] != o and b[0][4] != o and (b[3][1] == p or b[2][2] == p or b[1][3] == p or b[0][4] == p): 
            score += 1
        if b[3][2] != o and b[2][3] != o and b[1][4] != o and b[0][5] != o and (b[3][2] == p or b[2][3] == p or b[1][4] == p or b[0][5] == p): 
            score += 1
        if b[3][3] != o and b[2][4] != o and b[1][5] != o and b[0][6] != o and (b[3][3] == p or b[2][4] == p or b[1][5] == p or b[0][6] == p): 
            score += 1
        if b[4][0] != o and b[3][1] != o and b[2][2] != o and b[1][3] != o and (b[4][0] == p or b[3][1] == p or b[2][2] == p or b[1][3] == p): 
            score += 1
        if b[4][1] != o and b[3][2] != o and b[2][3] != o and b[1][4] != o and (b[4][1] == p or b[3][2] == p or b[2][3] == p or b[1][4] == p): 
            score += 1
        if b[4][2] != o and b[3][3] != o and b[2][4] != o and b[1][5] != o and (b[4][2] == p or b[3][3] == p or b[2][4] == p or b[1][5] == p): 
            score += 1
        if b[4][3] != o and b[3][4] != o and b[2][5] != o and b[1][6] != o and (b[4][3] == p or b[3][4] == p or b[2][5] == p or b[1][6] == p): 
            score += 1
        if b[5][0] != o and b[4][1] != o and b[3][2] != o and b[2][3] != o and (b[5][0] == p or b[4][1] == p or b[3][2] == p or b[2][3] == p): 
            score += 1
        if b[5][1] != o and b[4][2] != o and b[3][3] != o and b[2][4] != o and (b[5][1] == p or b[4][2] == p or b[3][3] == p or b[2][4] == p): 
            score += 1
        if b[5][2] != o and b[4][3] != o and b[3][4] != o and b[2][5] != o and (b[5][2] == p or b[4][3] == p or b[3][4] == p or b[2][5] == p): 
            score += 1
        if b[5][3] != o and b[4][4] != o and b[3][5] != o and b[2][6] != o and (b[5][3] == p or b[4][4] == p or b[3][5] == p or b[2][6] == p): 
            score += 1
        
        return score