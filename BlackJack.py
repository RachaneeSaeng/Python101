import random

class Player(object):
    
    def __init__(self):
        self.cards = []
        
    def addCard(self, card):       
        self.cards.append(card)
        
    def displayCards(self):
        s = ''
        for c in self.cards:
            s += str(c) + ' | ';
        return s

class Card(object):
    def __init__(self, suit, character):
        self.suit = suit
        self.character = character
        if character == 'A':
            self.point = 1
        elif character in ['K', 'Q', 'J']:
            self.point = 10
        else:
            self.point = character
    
    def __str__(self):
        return '%s%s' %(str(self.character), self.suit)
                 
def pickCard(deck):    
    return deck.pop(random.choice(deck.keys()))

def creatDeck():
    cardSuits = ('s', 'h', 'd', 'c')
    suitMembers = (2, 3, 4, 5, 6, 7, 8, 9, 10, 'A', 'K', 'Q', 'J')
    
    deck = {}
    i = 0
    for s in cardSuits:
        for c in suitMembers:
            i += 1
            deck[i] = Card(s, c)
    return deck

def sumPoint(cards):
    sum = 0
    for card in cards:
        if card.character != 'A':
            sum += card.point
        else:
            sum += card.point
            if(sum + 10 <= 21):
                sum += 10 # A = 11
    return sum
            
def isBlackJack(cards):
    return sumPoint(cards) == 21

def isBust(cards):
    return sumPoint(cards) > 21

def hitOrStand():
    return raw_input('Do you want to Hit or Stand? Enter 1 or 2: ').lower().startswith('1')

def replay():
    return raw_input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')

#==================== Game =================
while True:    
    deck = creatDeck()
    isGameOn = True
    
    while len(deck) > 0 and isGameOn:
        # 2 Card for dealer
        dealer = Player()
        dealer.addCard(pickCard(deck))
        dealer.addCard(pickCard(deck))
        
        # 2 Card for player 
        card1 = pickCard(deck)
        card2 = pickCard(deck)
        print 'You got cards %s and %s' %(card1, card2)
        player = Player()
        player.addCard(card1)
        player.addCard(card2)
        
        # Ask to player get more card or stand as long as it's not BlackJack or Bust
        while True:
            if isBlackJack(player.cards):
                print 'BlackJack! you win :)'
                isGameOn = False
                break
            if isBust(player.cards):
                print 'Bust! dealer win T_T'
                isGameOn = False
                break
            if hitOrStand():
                pickedCard = pickCard(deck)
                print 'You got card %s' %pickedCard     
                player.addCard(pickedCard)
            else:
                # Compare with dealer and print result                
                while sumPoint(dealer.cards) < 17:  
                    pickedCard = pickCard(deck)
                    dealer.addCard(pickedCard)
                    
                print 'Your cards are: %s' %player.displayCards()
                print 'Dealer cards are: %s' %dealer.displayCards()  
                    
                if sumPoint(player.cards) > sumPoint(dealer.cards):
                    print 'You win :)'
                elif sumPoint(player.cards) < sumPoint(dealer.cards):
                    print 'Dealer win T_T'
                else:
                    print 'Push!'
                    
                isGameOn = False
                break  
            
    if not replay():
        break


