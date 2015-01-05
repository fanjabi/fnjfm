import math
import random
import array

class Player:
	good_attribute_weight = 75
	other_attribute_weight = 25
	attr_max = 20
	sftimes = 3
	absw = [25, 15, 10, 8, 6, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
	abswl = [15, 10, 9, 8, 5, 4, 3, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0]
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
		self.__attrwa = array.array('i')
		self.__attrwal = array.array('i')
		for a in self.all_attributes:
			if a in self.__good_attributes:
				self.fattributes[a] = self.get_random()
			else:
				self.__other_attributes.append(a)
				self.fattributes[a] = self.get_random_low()
			self.attributes[a] = round(self.fattributes[a])

	
	def get_random(self):
		self.__init_attrwa()
		summ = 0
		for i in range(self.sftimes):
			summ = summ + random.choice(self.__attrwa)
		return summ / self.sftimes

	def __init_attrwa(self):
		if len(self.__attrwa) > 0:
			return
		for i in range(1, self.attr_max + 1):
			self.__attrwa.extend([i] * self.absw[abs(i-self.potential)])
			self.__attrwal.extend([i] * self.abswl[abs(i-self.potential)])

	def get_random_low(self):
		self.__init_attrwa()
		summ = 0
		for i in range(self.sftimes):
			summ = summ + random.choice(self.__attrwal)
		return summ / self.sftimes

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

ludogorets = Team('Ludogorets', 5)

ludogorets.print_info()

print("Team ability: %d" % ludogorets.average_ability())