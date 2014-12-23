import math
import random

class Player:
	good_attribute_weight = 75
	other_attribute_weight = 25
	attr_max = 20
	all_attributes = ['heading', 'jumping', 'tackling', 'marking', 'passing']
	good_attributes = {
		'fw' : ['heading', 'jumping'],
		'mf' : ['tackling', 'passing'],
		'df' : ['tackling', 'marking', 'heading']
	}
	def f(self, x):
		x = x + 12 - self.potential
		return ( ( math.sin(x/7) + math.sin(-x/3)*0.2 ) / 1.4 ) + 0.1

	def flow(self, x):
		x = x + 12 - self.potential
		return ( ( ( math.sin(x/7) + math.sin(-x/3)*0.2 ) / 1.4 ) + 0.1 + math.cos(x/11) ) / 2

	def __init__(self, potential, pos):
		self.pos = pos
		self.potential = potential
		self.fattributes = {}
		self.attributes = {}
		self.__good_attributes = self.good_attributes[self.pos]
		self.__other_attributes = []
		for a in self.all_attributes:
			if a in self.__good_attributes:
				self.fattributes[a] = self.get_random()
			else:
				self.__other_attributes.append(a)
				self.fattributes[a] = self.get_random_low()
			self.attributes[a] = round(self.fattributes[a])

	
	def get_random(self):
		while True:
			randy = random.random()
			randx = random.random() * self.attr_max
			if randy <= self.f(randx):
				if randx < 0.5:
					randx = 0.5
				return randx

	def get_random_low(self):
		while True:
			randy = random.random()
			randx = random.random() * self.attr_max
			if randy <= self.flow(randx):
				if randx < 0.5:
					randx = 0.5
				return randx

	def get_ability(self):
		gasum = 0
		galen = 0
		oasum = 0
		oalen = 0
		for ga in self.__good_attributes:
			gasum = gasum + self.fattributes[ga]
			galen = galen + 1
		for oa in self.__other_attributes:
			oasum = oasum + self.fattributes[oa]
			oalen = oalen + 1

		return round( ( ( gasum * self.good_attribute_weight ) / ( galen * self.attr_max ) ) + ( ( oasum * self.other_attribute_weight ) / ( oalen * self.attr_max ) ) )



	def _get_ability_(self):
		return ( self.good_attribute_weight * sum(self.__good_attributes) ) / ( len(self.__good_attributes) * self.attr_max ) + ( self.other_attribute_weight * sum(self.__other_attributes) ) / ( len(self.__other_attributes) * self.attr_max )

	def print_info(self):
		print("Heading: %2.2f \nJumping: %2.2f" % ( self.heading, self.jumping ) )

class Team:
	player_count = {
		'fw' : 4,
		'mf' : 7,
		'df' : 7
	}
	def __init__(self, name, potential):
		self.name = name
		self.potential = potential
		self.players = []
		for key, value in self.player_count.items():
			for n in range(value):
				self.players.append(Player(self.potential, key))

	def print_info(self):
		print("\n\nTeam: %s\n\nPlayers:\n\n" % (self.name))
		for p in self.players:
			print("Position: %s, Ability: %d" % (p.pos, p.get_ability()) )

	def average_ability(self):
		pc = 0
		ps = 0
		for p in self.players:
			pc = pc + 1
			ps = ps + p.get_ability()
		return round(ps/pc)

ludogorets = Team('Ludogorets', 20)

ludogorets.print_info()

print("Team ability: %d" % ludogorets.average_ability())