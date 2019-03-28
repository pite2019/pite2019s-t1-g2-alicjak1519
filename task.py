class Car():

    def __init__(self):
        print("START")
        print("Speed is : 50")
        print("Wheel angle is : 0\n")
        self.wheel_angle = 0
        self.speed = 50

    def handle_event(self, event):
        event.affect_car(self)
        # # if self.speed > 200:
        # #     print("Too fast!\n")
        # #     self.speed = 200
        # elif self.speed == 0:
        #     print("Too slow!\n")
        # else:
        print("Speed is: {}".format(self.speed))
        print("Wheel angle is: {}\n".format(self.wheel_angle))
        event.set_parameters(self)

class Event():
    def affect_car(self, car):
        pass
    def set_parameters(self,car):
        pass

class ObstacleEvent(Event):
    def affect_car(self,car):
        car.speed = 30
        car.wheel_angle = 90
    def set_parameters(self,car):
        car.speed = 50
        car.wheel_angle = 0

class PedestrianEvent(Event):
    def affect_car(self, car):
        car.speed = 0
    def set_parameters(self,car):
        car.speed = 20

class TurningLeft(Event):
    def affect_car(self, car):
        car.speed -= 20
        car.wheel_angle = -45
    def set_parameters(self,car):
        car.speed = 50
        car.wheel_angle = 0

class TurningRight(Event):
    def affect_car(self, car):
        car.speed -= 20
        car.wheel_angle = 45
    def set_parameters(self,car):
        car.speed = 50
        car.wheel_angle = 0

class AccelerateEvent(Event):
    def affect_car(self, car):
        if car.speed >= 200:
            print("Too fast!\n")
            car.speed = 200
        else:
            car.speed += 10
    def set_parameters(self,car):
        pass

class DecelerateEvent(Event):
    def affect_car(self, car):
        if car.speed == 0:
            print("Too slow!\n")
            car.speed = 0
        else:
            car.speed -= 10
    def set_parameters(self,car):
        pass

class EmptyEvent(Event):
    def affect_car(self, car):
        pass
    def set_parameters(self,car):
        pass

car1 = Car()

events_dictionary = {
    'o': ObstacleEvent(),
    'p': PedestrianEvent(),
    'a': TurningLeft(),
    'd': TurningRight(),
    'w': AccelerateEvent(),
    's': DecelerateEvent(),
    '': EmptyEvent()
}

print("o = obstacle,\np = pedestrian, \na = turning_left")
print("d = turning_right, \nw = acceleration, \ns = deceleration")

while True:
    event_name = input()
    if event_name in events_dictionary:
        car1.handle_event(events_dictionary[event_name])
    else:
        print("Try something else\n")
