class Road:
    _mass_sq = 25
    _thickness = 10

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def asfalt_mass(self):
         print(int(self.__length) * int(self.__width) * Road._mass_sq * Road._thickness)


my_road = Road(305, 15)

my_road.asfalt_mass()
