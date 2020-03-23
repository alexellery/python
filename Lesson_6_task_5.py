class Stationery:
    _title = None

    def __init__(self, title):
        self._title = title

    def draw(self):
        print('Rendering started')


class Pen(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Inking started')


class Pencil(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Drawing started')


class Handle(Stationery):

    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print('Filling started')


drawing_1 = Pen('Erich Krause')
drawing_2 = Pencil('Crayola')
drawing_3 = Handle('Copic')

drawing_1.draw()
drawing_2.draw()
drawing_3.draw()