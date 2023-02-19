class Human:
    default_name = 'Alex'
    default_age = 35

    def __init__(self, name=default_name, age=default_age):
        self.name = name
        self.age = age
        self.__money = 0
        self.__house = None

    def info(self):
        print(f'Name: {self.name}')
        print(f'Age: {self.age}')
        print(f'House: {self.__house}')
        print(f'Money: {self.__money}')

    @staticmethod
    def default_info():
        print(f'Default name: {Human.default_name}')
        print(f'Default age: {Human.default_age}')

    def earn_money(self, income):
        self.__money += income
        print(f'Earned {income} money! Current value: {self.__money}')

    def buy_house(self, house, discount):
        price = house.final_price(discount)
        if self.__money >= price:
            self.__make_deal(house, price)
        else:
            print('Недостаточно денег')

    def __make_deal(self, house, price):
        self.__money -= price
        self.__house = house


class House:

    def __init__(self, area, price):
        self._area = area
        self._price = price

    def final_price(self, discount):
        final_price = self._price * (100 - discount) / 100
        print(f'Final price: {final_price}')
        return final_price


class SmallHouse(House):
    default_area = 40

    def __init__(self, price):
        super().__init__(SmallHouse.default_area, price)


if __name__ == '__main__':
    Human.default_info()
    alexander = Human('Alexander', 27)
    alexander.info()

    small_house = SmallHouse(8_500)

    alexander.buy_house(small_house, 5)

    alexander.earn_money(10_000)
    alexander.buy_house(small_house, 5)
    alexander.info()

import string as s


class Alphabet:

    def __init__(self, lang, letters):
        self.lang = lang
        self.letters = list(letters)

    def print(self):
        print(self.letters)

    def letters_num(self):
        return len(self.letters)


class EngAlphabet(Alphabet):
    default_lang = 'En'
    default_letters = s.ascii_uppercase
    __letters_num = len(default_letters)

    def __init__(self):
        super().__init__(EngAlphabet.default_lang, EngAlphabet.default_letters)

    def is_en_letter(self, letter):
        return letter.upper() in self.letters

    def letters_num(self):
        return EngAlphabet.__letters_num

    @staticmethod
    def example():
        print('English Example:\nTo be or ot to be?! What is the question?')


if __name__ == '__main__':
    eng = EngAlphabet()
    eng.print()
    print(eng.letters_num())
    print(eng.is_en_letter('F'))
    print(eng.is_en_letter('Щ'))
    eng.example()


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
        self.tomatoes = [Tomato(index) for index in range(1, quantity + 1)]

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