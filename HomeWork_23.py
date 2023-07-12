class Fruits:

    def __init__(self, name: str, sort: str, list_vitamins: list[str], price: int):
        self.name = name
        self.sort = sort
        self.list_vitamins = list_vitamins
        self.price = price

    def clear(self):
        print(f'{self.name} clear!')


class Orange(Fruits):

    def __str__(self):
        return self.clear()


class Mandarin(Fruits):

    def __str__(self):
        return self.clear()


class Banana(Fruits):
    amount_potassium = 350

    def __str__(self):
        return self.clear()

    def get_info(self):
        print(f'potassium content per 100 grams Banana - {Banana.amount_potassium} grams')


class Apple(Fruits):

    def cut(self):
        print(f'{self.name} cut!')


orange = Orange('orange', 'A', ['a', 'b', 'c', 'd'], 120)
orange.clear()
mandarin = Mandarin('mandarin', 'B', ['d', 'pp', 'k', 'b1'], 100)
mandarin.clear()
banana = Banana('banana', 'A', ['b2', 'b12', 'A'], 80)
banana.clear()
banana.get_info()
apple = Apple('apple', 'A', ['a', 'b', 'c', 'b3'], 70)
apple.cut()