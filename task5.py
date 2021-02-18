class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        return print(f'Start drawing...')


class Pen(Stationery):
    def draw(self):
        print(f'Start drawing by {__class__.__name__.lower()}...')


class Pencil(Stationery):
    def draw(self):
        print(f'Start drawing by {__class__.__name__.lower()}...')


class Handle(Stationery):
    def draw(self):
        print(f'Start drawing by {__class__.__name__.lower()}...')


pen = Pen('Something')
pencil = Pencil('Something')
handle = Handle('Something')
pen.draw()
pencil.draw()
handle.draw()

