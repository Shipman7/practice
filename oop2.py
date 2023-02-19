class Tomato:
    states = {1: 'Семя', 2: 'Рассада', 3: 'Цветение', 4: 'Завязь', 5: 'Спелый плод'}
    
    def __init__(self, index):
        self._index = index
        self._state = 1
        
    def grow(self, state):
        return self._change_state()
        
    def is_ripe(self):
        return self._state == 5
    
    def _change_state(self):
        if self._state < 5:
	    self._state += 1
        self._print_state()
	
    def _print_state(self):
	print(f'Tomato {self._index} is {Tomato.states[self.state]}')
    
class TomatoBush:
    
    def __init__(self, quantity):
        self.tomatoes = [Tomato(index) for index in range(1, quantity+1)]
        
    def grow_all(self):
        for tomato in self.tomatoes:
	    tomato.grow()
	    
    def all_are_ripe(self):
    	return all([tomato.is_ripe() for tomato in self.tomatoes])
	
    def give_away_all(self):
	self.tomatoes = []
    
class Gardener:
    
    def __init__(self, name, plant):
	self.name = name
	self._plant = plant
    
    def work(self):
	print('Gardener is working...')
	self._plant.grow_all()
	print('Gardener finished')
    
    def harvest(self):
	print('Gardener is harvesting...')
	if self._plant.all_are_riped:
	    self._plant.give_away_all()
	    print('Harvesting is finished')
	else:
	    print('Too early! Your plant is green and not ripe.')
    
    @staticmethod
    def knowledge_base():
	print('''Harvest time for tomatoes should ideally occur
when the fruit is a mature green and
then allowed to ripen off the vine.
This prevents splitting or bruising
and allows for a measure of control over the ripening process.''')
if __name__ == '__main__':
    Gardener.knowledge_base()