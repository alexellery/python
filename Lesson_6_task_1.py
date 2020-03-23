from time import sleep

class TrafficLights:
    __color = ['red', 'yellow', 'green']

    def running(self):
        i = 0
        while i < 3:
            print(f'The traffic light is {TrafficLights.__color[i]}')
            if i == 0:
                sleep(7)
            elif i == 1:
                sleep(2)
            else:
                sleep(15)
            i += 1


Moscovskaya_Cross = TrafficLights()

Moscovskaya_Cross.running()


