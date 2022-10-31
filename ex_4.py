class car:
    def __init__(self,registration_number,maximum_speed,current_speed=0):

        self.registration_number=registration_number
        self.maximum_speed=maximum_speed
        self.current_speed=current_speed
        self.travelled_distance=0


    def accerelate(self,speed):
            self.current_speed=self.current_speed + speed

    def drive(self,hours=1):
            self.travelled_distance = self.travelled_distance + self.current_speed * hours


class race:
    def __init__(self,name,distance,car_list):
        self.name=name
        self.distance=distance
        self.car_list=car_list

    def hour_passes(self):
        for car_race in self.car_list:
            car_race.current_speed=random.randrange(-10,15)
            car_race.drive(1)

    def print_status(self):
        for car_race in self.car_list:
            print(f"name race is: {race1.name},registration_number :{car_race.registration_number}, car speed is: {car_race.current_speed}"
                  f"travel distance is: {car_race.travelled_distance}")

    def race_finished(self):
        win_distance=0
        for car_race in self.car_list:
            win_distance=max(win_distance,car_race.travelled_distance)
            if win_distance>=self.distance:

                return  True






import random
car_list=[]
register_num_list=['ABC-1','ABC-2','ABC-3','ABC-4','ABC-5','ABC-6','ABC-7','ABC-8','ABC-9','ABC-10']

maximum_speed_list=[]
car_race=[]

for i in range(0,10):
    maxSpeed=random.randrange(100,200)
    regNum=register_num_list[i]
    car_list.append(car(regNum,maxSpeed))


# win_distance=0
# while win_distance <10000:
#     for car_race in car_list:
#         speed=random.randrange(-10,15)
#         car_race.accerelate(speed)
#         car_race.drive(1)
#         win_distance=max(car_race.travelled_distance,win_distance)

race1=race("Grand Demolition Derby",8000,car_list)

# for car_race in car_list:
#     print(vars(car_race))

hour=0
while race1.race_finished()is not True:
    hour=hour+1
    race1.hour_passes()
    if hour % 10 ==0:
        print(f"After {hour} Hours")
        race1.print_status()
        print()
print(f"!!!!!!!!!!!!!!!!!!!!!!!Finish after {hour} hours!!!!!!!!!!!!!!!!!!!!!!!")
race1.print_status()
