import random, copy

MAX_BARREL = 90
DIGITS_IN_CARD = 15
DIGITS_IN_LINE = 5


class LotoCard():
    def __init__(self, name):
        self.name = name
        self.card = self.gen_card

    @property
    def gen_card(self):
        num_comb = random.sample(range(1, MAX_BARREL + 1), DIGITS_IN_CARD)
        card = [sorted(num_comb[i:i + DIGITS_IN_LINE]) for i in range(0, len(num_comb), DIGITS_IN_LINE)]
        return card

    def update_card(self, barell):
        for line in self.card:
            yield ['-' if x == barell else x for x in line]

    def show_card(self):
        card = copy.deepcopy(self.card)
        placeholders = ' '.join(['{:>2}' for i in range(9)])
        for line in card:
            for space in ' ' * 4:
                line.insert(random.randint(0, len(line) - 1), space)
        return [placeholders.format(*line) for line in card]

    @staticmethod
    def is_empty(card):
        for line in card:
            for elt in line:
                if elt != '-':
                    return False
        return True

    @staticmethod
    def barr_in_card(card, barrel):
        return barrel in [barrel for line in card for barrel in line]


class LotoGame:

    def __init__(self, player_1, player_2):
        self.__player_1_card = player_1
        self.__player_2_card = player_2
        self.barr_list = random.sample(range(1, MAX_BARREL + 1), 90)

    def get_barr(self):
        yield self.barr_list.pop()

    def start(self):
        barr_list = self.barr_list

        while True:
            barrel = next(self.get_barr())
            print(f'New barrel: {barrel} (left {len(barr_list)})')
            print("{0} {1}'s card {0}\n{2}\n{3}\n{4}".format('*' * 6, self.__player_1_card.name,
                                                             *self.__player_1_card.show_card()))
            print("{0} {1}'s card {0}\n{2}\n{3}\n{4}".format('*' * 6, self.__player_2_card.name,
                                                             *self.__player_2_card.show_card()))
            answ = 'a'
            while answ not in 'ynq':
                answ = input("Is the barrel in player's card? y/n or q for exit: ")
            if answ == 'q':
                break
            elif (answ == 'y' and self.__player_1_card.barr_in_card(self.__player_1_card.card, barrel)) or (
                    answ == 'n' and not self.__player_1_card.barr_in_card(self.__player_1_card.card, barrel)):
                print("You're right! \n\nNext turn...")
            else:
                print("You lose!")
                break
            self.__player_1_card.card = list(self.__player_1_card.update_card(barrel))
            self.__player_2_card.card = list(self.__player_2_card.update_card(barrel))
            if self.__player_1_card.is_empty(self.__player_1_card.card):
                print('You filled the entire card!')
                break
            if self.__player_2_card.is_empty(self.__player_2_card.card):
                print('Computer filled the entire card!')
                break


player_1 = LotoCard('Player')
player_2 = LotoCard('Computer')
game = LotoGame(player_1, player_2)
game.start()
