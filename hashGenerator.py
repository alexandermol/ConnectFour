# connect 4 win condition hash generator

# the function starts like:
# b = self.board
# p = currentPlayer
# o = opponent

# ends with: return False

print "# vertical"
for r in range(3):
    for c in range(7):
        output = "if "
        for i in range(4):
            output += "b["+str(r+i)+"]["+str(c)+"] != o"
            if i != 3:
                output += " and "
        output += " and ("
        for i in range(4):
            output += "b["+str(r+i)+"]["+str(c)+"] == p"
            if i != 3:
                output += " or "
        output += "): \n\tscore += 1"
        print output

print "# horizontal"
for r in range(6):
    for c in range(4):
        output = "if "
        for i in range(4):
            output += "b["+str(r)+"]["+str(c+i)+"] != o"
            if i != 3:
                output += " and "
        output += " and ("
        for i in range(4):
            output += "b["+str(r)+"]["+str(c+i)+"] == p"
            if i != 3:
                output += " or "
        output += "): \n\tscore += 1"
        print output

print "# diagonal \\"
for r in range(3):
    for c in range(4):
        output = "if "
        for i in range(4):
            output += "b["+str(r+i)+"]["+str(c+i)+"] != o"
            if i != 3:
                output += " and "
        output += " and ("
        for i in range(4):
            output += "b["+str(r+i)+"]["+str(c+i)+"] == p"
            if i != 3:
                output += " or "
        output += "): \n\tscore += 1"
        print output

print "# diagonal /"
for r in range(3):
    for c in range(4):
        output = "if "
        for i in range(4):
            output += "b["+str(r+3-i)+"]["+str(c+i)+"] != o"
            if i != 3:
                output += " and "
        output += " and ("
        for i in range(4):
            output += "b["+str(r+3-i)+"]["+str(c+i)+"] == p"
            if i != 3:
                output += " or "
        output += "): \n\tscore += 1"
        print output