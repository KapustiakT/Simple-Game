#!/usr/bin/env python
# coding: utf-8

# In[1]:


legal_moves = set([(0,1,3),
                      (0,2,5),
                      (5,2,0),
                      (1,3,6),
                      (1,4,8),
                      (2,4,7),
                      (2,5,9),
                      (3,1,0),
                      (3,4,5),
                      (3,6,10),
                      (3,7,12),
                      (4,7,11),
                      (4,8,13),
                      (5,4,3),
                      (5,8,12),
                      (5,9,14),
                      (6,3,1),
                      (6,7,8),
                      (7,4,2),
                      (7,8,9),
                      (8,4,1),
                      (8,7,6),
                      (9,5,2),
                      (9,8,7),
                      (10,6,3),
                      (10,11,12),
                      (11,7,4),
                      (11,12,13),
                      (12,7,3),
                      (12,8,5),
                      (12,11,10),
                      (12,13,14),
                      (13,8,4),
                      (13,12,11),
                      (14,9,5),
                      (14,13,12)])


# In[2]:


os=[]
us=[]


# In[3]:


def game_over_bro(os,us):
    for x in os:
        for y in os:
            for z in us:
                if (x,y,z) in legal_moves:
                    return False
    return True


# In[4]:


def game_over(board: list,os,us) -> bool:
    pegs_removed=sum(list(map(lambda x: x == " *",board)))
    if game_over_bro(os,us) == True: 
        if pegs_removed == 14:
            printboard(board)
            print("YOU'RE A GENIUS!")
            return True
        elif pegs_removed == 13:
            printboard(board)
            print("YOU'RE PURTY SMART!")
            return True
        elif pegs_removed == 12:
            printboard(board)
            print("YOU'RE JUST PLAIN DUMB!")
            return True
        elif pegs_removed == 11:
            printboard(board)
            print("YOU'RE JUST PLAIN *EG-NO-RA-MOOSE*!")
            return True
        elif pegs_removed == 10:
            printboard(board)
            print("I DID NOT KNOW YOU COULD BE THAT BAD!")
            return True
        elif pegs_removed == 9:
            printboard(board)
            print("I DID NOT KNOW YOU COULD BE THAT BAD!")
            return True


# In[5]:


def makeboard(y=0):
    board =[i for i in range(15)]
    y = int(input("Choose a peg to remove: "))
    board[y]=' *'
    return board


# In[6]:


def displayboard():
    baseboard =[i for i in range(15)]
    return baseboard


# In[7]:


def printboard(board):
    row=1
    z=0
    n=5
    for x in board:
        if not z:
            print(" "*(2*n-1-row),end="")
        if x == " *":
            print(x, end = ' ')
        else:
            print(f'{float(x):2.0f}', end = ' ')
        z+=1
        if z == row:
            print()
            z=0
            row+=1


# In[8]:


def occupied_slots(board):
    occupied=[]
    for x in board:
        if x != " *":
            occupied.append(x)
    return occupied


# In[9]:


def empty_slots(board):
    empty=[]
    for i,x in enumerate(board):
        if x == " *":
            empty.append(i)
    return empty


# In[10]:


def find_peg3(peg1,peg2):
    for moves in legal_moves:
        if peg1 == moves[0] and peg2 ==moves[1]:
            return moves[2]


# In[11]:


def makemove(board):
    peg1=int(input("Peg you are moving: "))
    peg2=int(input("Peg you are jumping: "))
    peg3=find_peg3(peg1,peg2)
    if (peg1,peg2,peg3) not in legal_moves:
        print("illegal move")
        return makemove(board)
    if board[peg1] == " *" or board[peg2] == " *" or board[peg3]!= " *":
        print("Bad Peg")
        return makemove(board)
    board[peg2]=" *"
    board[peg1]=" *"
    board[peg3]=peg3
#     os=occupied_slots(board)
#     us=empty_slots(board)


# In[12]:


baseboard=displayboard()
printboard(baseboard)
board=makeboard()
while not game_over(board,os,us):
    printboard(board)
    makemove(board)
    os=occupied_slots(board)
    us=empty_slots(board)

