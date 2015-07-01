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
	
	def __init__(self, potential, pos):
		self.pos = pos
		self.potential = potential
		self._fattributes_ = {}
		self._attributes_ = {}
		self._good_attributes_ = self.good_attributes[self.pos]
		self._other_attributes_ = []
		self._attrwa_ = array.array('H')
		self._attrwal_ = array.array('H')
		for a in self.all_attributes:
			if a in self._good_attributes_:
				self._fattributes_[a] = self.get_random()
			else:
				self._other_attributes_.append(a)
				self._fattributes_[a] = self.get_random_low()
			self._attributes_[a] = round(self._fattributes_[a])

	
	def get_random(self):
		self.__init_attrwa__()
		summ = 0
		for i in range(self.sftimes):
			summ = summ + random.choice(self._attrwa_)
		return summ / self.sftimes

	def __init_attrwa__(self):
		if len(self._attrwa_) > 0:
			return
		for i in range(1, self.attr_max + 1):
			self._attrwa_.extend([i] * self.absw[abs(i-self.potential)])
			self._attrwal_.extend([i] * self.abswl[abs(i-self.potential)])

	def get_random_low(self):
		self.__init_attrwa__()
		summ = 0
		for i in range(self.sftimes):
			summ = summ + random.choice(self._attrwal_)
		return summ / self.sftimes

	def get_ability(self):
		gasum = 0
		galen = 0
		oasum = 0
		oalen = 0
		for ga in self._good_attributes_:
			gasum = gasum + self._fattributes_[ga]
			galen = galen + 1
		for oa in self._other_attributes_:
			oasum = oasum + self._fattributes_[oa]
			oalen = oalen + 1

		return round( ( ( gasum * self.good_attribute_weight ) / ( galen * self.attr_max ) ) + ( ( oasum * self.other_attribute_weight ) / ( oalen * self.attr_max ) ) )

	def _get_ability_(self):
		return ( self.good_attribute_weight * sum(self._good_attributes_) ) / ( len(self._good_attributes_) * self.attr_max ) + ( self.other_attribute_weight * sum(self._other_attributes_) ) / ( len(self._other_attributes_) * self.attr_max )

class Team:
	players_positions = {
		'fw' : 4,
		'mf' : 7,
		'df' : 7
	}
	def __init__(self, name, potential):
		self.name = name
		self.potential = potential
		self._best_player_ = None
		self._weakest_player_ = None
		self.players = []
		for key, value in self.players_positions.items():
			for n in range(value):
				self.players.append(Player(self.potential, key))

	def print_info(self):
		print("Team: %s\nPlayers:" % (self.name))
		for p in self.players:
			print("Position: %s, Ability: %d" % (p.pos, p.get_ability()) )

	def average_ability(self):
		pc = 0
		ps = 0
		for p in self.players:
			pc = pc + 1
			ps = ps + p.get_ability()
		return round(ps/pc)
	
	def get_best_player(self):
		if self._best_player_ != None:
			return self._best_player_
		for p in self.players:
			if self._best_player_ == None or self._best_player_.get_ability() < p.get_ability():
				self._best_player_ = p
		return self._best_player_
	
	def get_weakest_player(self):
		if self._weakest_player_ != None:
			return self._weakest_player_
		for p in self.players:
			if self._weakest_player_ == None or self._weakest_player_.get_ability() > p.get_ability():
				self._weakest_player_ = p
		return self._weakest_player_


ludogorets = Team('Ludogorets', 20)
ludogorets2 = Team('Ludogorets2', 20)
ludogorets3 = Team('Ludogorets3', 20)

#ludogorets.print_info()

print("Best: %d, Weakest: %d" % ( ludogorets.get_best_player().get_ability(), ludogorets.get_weakest_player().get_ability()))
print("Best: %d, Weakest: %d" % ( ludogorets2.get_best_player().get_ability(), ludogorets2.get_weakest_player().get_ability()))
print("Best: %d, Weakest: %d" % ( ludogorets3.get_best_player().get_ability(), ludogorets3.get_weakest_player().get_ability()))