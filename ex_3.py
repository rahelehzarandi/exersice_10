#Extend the program again by adding a method fire_alarm that does not receive any parameters
# and moves all elevators to the bottom floor. Continue the main program by causing a fire
# alarm in your building.

class elevator:
    def __init__(self,num_floor=0,curent_floor=0):
        self.num_floor=num_floor
        self.curent_floor=curent_floor
        self.curent_floor_list = []


    def go_to_floor(self,floor):
        while self.curent_floor != floor:
            if floor > self.curent_floor:
                h.floor_up()
            elif floor < self.curent_floor:
                h.floor_down()
        print("YOU ARE IN CHOSEN FLOOR")



    def floor_up(self):
        while h.curent_floor != build.num_floor:
            self.curent_floor=self.curent_floor + 1

        return self.curent_floor_list.append(self.curent_floor)




    def floor_down(self):
         while h.curent_floor != build.num_floor:
             self.curent_floor = self.curent_floor - 1
         return self.curent_floor_list.append(self.curent_floor)






class Building:

    def __init__(self,num_elevators,num_floor=10):
        self.num_elevators=num_elevators
        self.num_floor=num_floor
        self.elevator_list = []

    def run_elevator(self,num_elevators,num_floor):

            self.num_floor=num_floor
            if num_floor < h.curent_floor:
                h.floor_down()

            elif num_floor > h.curent_floor:
                h.floor_up()
            return self.elevator_list.append(num_elevators)

    def fire_alarm(self):
        h.curent_floor_list.clear()
        self.num_floor=0
        for i in self.elevator_list:
            h.floor_down()





h=elevator()

build=Building(3)
build.run_elevator(2,4)
build.run_elevator(1,8)
build.run_elevator(3,6)
print(f"the elevator {build.elevator_list[0]} , is on floor :{h.curent_floor_list[0]} ")
print(f"the elevator {build.elevator_list[1]} , is on floor :{h.curent_floor_list[1]} ")
print(f"the elevator {build.elevator_list[2]} , is on floor :{h.curent_floor_list[2]} ")

build.fire_alarm()
print("!!! Fire!!!")
print(f"the elevator {build.elevator_list} , is on floor :{h.curent_floor_list}")

