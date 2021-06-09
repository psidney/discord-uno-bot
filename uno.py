import random

class UnoGame:

    def __init__(self,playerCount,playerList):
        self.hands = []
        self.playerList = playerList
        self.direction = 1      # 1 for forward, -1 for reverse
        self.turn = 0
        self.lastPlayed = 'wild'
        for player in self.playerList:
            self.hands.append(Hand(player))
        
        for hand in self.hands:
            print(hand.playerName + ': ' + hand.getHandString())
            
    def nextTurn(self):
        self.turn += self.direction
        if self.turn == -1:
            self.turn = len(self.playerList)-1
        elif self.turn == len(self.playerList)-1:
            self.turn = 0
    
    def reverse(self):
        self.direction = -self.direction
    
    def 
    def checkForGameOver(self):
        for hand in self.hands:
            if len(hand)==0:
                return playerName
        return False

class Hand:

    def __init__(self,playerName):
        self.playerName = playerName
        self.cards = []
        for i in range(0,7):
            self.cards.append(Card())
        return
        
    def getHandString(self):
        returnString = ''
        for card in self.cards:
            returnString += card.displayCardNameWithColor() + ', '
        return returnString[:-2]
    
    def drawCard(self):
        self.cards.append(Card())
        
class Card:

    def __init__(self):
        self.suites = ['R','B','G','Y','']
        self.cards = ['1','2','3','4','5','6','7','8','9','draw2','reverse','skip']
        self.specials = ['wild','wild','wilddraw4']
        self.color = random.choice(self.suites)
        if self.color == '':
            self.number = random.choice(self.specials)
        else:
            self.number = random.choice(self.cards)
        return
    
    def displayCardName(self):
        return self.number + self.color
        
    def displayCardNameWithColor(self):
        emojiMappings = {'R':':red_square:','Y':':yellow_square:','B':':blue_square:','G':':green_square:','':':white_large_square:'}
        return self.displayCardName() + emojiMappings[self.color]
        

Game = UnoGame(2,['patrick','david'])
