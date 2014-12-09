import math
import random

class Player:
	heading = 0
	rheading = 0
	jumping = 0
	rjumping = 0
	potential = 0
	def f(self, x):
		x = x + 12 - self.potential
		return ( ( math.sin(x/7) + math.sin(-x/3)*0.2 ) / 1.4 ) + 0.1

	def __init__(self, potential):
		self.potential = potential
		self.heading = self.get_random()
		self.jumping = self.get_random()
		self.rheading = round(self.heading)
		self.rjumping = round(self.jumping)
	
	def get_random(self):
		while True:
			randy = random.random()
			randx = random.random() * 20
			if randy <= self.f(randx):
				if randx < 0.5:
					randx = 0.5
				return randx

	def print_info(self):
		print("Heading: %2.2f \nJumping: %2.2f" % ( self.heading, self.jumping ) )

	def fight(self, other):
		farr = [0] * ( (7 * self.rjumping) + ( 3 * self.rheading) ) +  [1] * ( (7 * other.rjumping) + ( 3 * other.rheading) )
		return random.choice(farr)
		print("Fight!\nPlayer 1:\t\t\tPlayer 2:\n\nHeading: %s\t\t\tHeading: %s\nJumping: %s\t\t\tJumping: %s\n\nWinner: %s" % (self.rheading, self.rjumping, other.rheading, other.rjumping, winner + 1))

mr = [0, 0]
for a in range(0,10):
	for i in range(0,100):
		a = Player(18)
		b = Player(15)
		winner = a.fight(b);
		mr[winner] = mr[winner] + 1
	print("%2.2f" % (mr[0]/mr[1]))