import random

class Car:
    def __init__(self, speed, color, name, is_police):
        self._speed = speed
        self._color = color
        self._name = name
        self._is_police: bool = is_police

    def go(self):
        print('The car started moving')

    def stop(self):
        print('The car stopped')

    def turn(self):
        direction = random.choice(('left', 'right', 'back'))
        print(f'The car turned {direction}')

    def show_speed(self):
        print(self._speed)


class TownCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self._has_trailer = bool
        self._type = random.choice(('sedan', 'hatchback', 'SUV', 'crossover'))
        self._number_of_accidents = random.randint(1, 10)

    def show_speed(self):
        if self._speed > 60:
            print("You are speeding! Slow down or you'll be arrested.")
        else:
            print(self._speed)


class SportCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self._number_of_races = random.randint(1, 50)
        self._type = random.choice(('off-road', 'Drifting', 'Drag', 'Track'))


class WorkCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self._type = random.choice(('Ambulance', 'Firearms', 'Transport'))

    def show_speed(self):
        if self._speed > 40:
            print("You are speeding! Slow down or you'll be arrested.")
        else:
            print(f'Your speed is {self._speed}. Keep moving.')


class PoliceCar(Car):
    def __init__(self, speed, color, name, is_police):
        super().__init__(speed, color, name, is_police)
        self._type = random.choices(('Patrol', 'Traffic', 'Dog', 'Response', 'Unmarked'))


moms_car = TownCar(80, 'grey', 'Nissan', False)
boss_car = SportCar(200, 'yellow', 'BMW', False)
dads_car = WorkCar(35, 'red', 'Volvo', False)
cops_car = PoliceCar(70, 'black', 'Ford', True)

dads_car.show_speed()
moms_car.show_speed()