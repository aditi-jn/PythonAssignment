import random
from itertools import product
class Card:
	suit=('Hearts','Spades','Clubs','Dimonds')
	faces = ('two', 'three', 'four', 'five', 'six', 'seven', 'eight',
             'nine', 'ten', 'jack', 'queen', 'king', 'ace')
	values={'two':2,'three':3,'four':4,'five':5,'six':6,'seven':7,'eight':8,
	        'nine':9,'ten':10,'jack':11,'queen':12,'king':13,'ace':1}
	
		
class Deck:
	def __init__(self):
		self.deck1 = list(product(Card.suit,Card.faces))
	def draw_card(self):
		random.shuffle(self.deck1)
		if len(self.deck1) == 0:
			return 0
		else:
			v=self.deck1.pop()
			s=(Card.values[v[1]]),
			return v+s
	def __str__(self):
		return str(self.deck1)

class Hand:

	def __init__(self):
		pass
	def take_card(self):
		l=[]
		a=Deck.draw_card(self)
		b=Deck.draw_card(self)
		l.append(a)
		l.append(b)
		x=a[2]+b[2]
		for i in range(8):
			if x>30:							
				break
				print("you won")
			else:
				c=Deck.draw_card(self)
				l.append(c)
				x=x+c[2]
		return l		

class Player:
	def __init__(self):
		Deck.__init__(self)
		pass
	def show_hands(self):
		print(Hand.take_card(self))
	def play(self):
		l=Hand.take_card(self)
		for i in range(len(l)):
			ch=input("enter yes for continue")
			if ch=='yes':
				print(l[i])
			else:
				print("game is over")
				

p=Player()
ch=int(input("you want to play"))
if ch==1:
	p.show_hands()
elif ch==2:	
	p.play()	

	
	

	
