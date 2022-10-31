#Extend the previous program by creating a Building class. The initializer parameters for the class are the
# numbers of the bottom and top floors and the number of elevators in the building. When a building is created
# , the building creates the required number of elevators. The list of elevators is stored as a property of the
# building. Write a method called run_elevator that accepts the number of the elevator and the destination floor as
# its parameters. In the main program, write the statements for creating a new building and running the elevators
# of the building




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

        print("CURRENT FLOOR IS:", self.curent_floor)
        while h.curent_floor != build.num_floor:
            self.curent_floor=self.curent_floor + 1
        #curent_floor_list.append(self.curent_floor)
        return self.curent_floor_list.append(self.curent_floor)




    def floor_down(self):
         print("CURRENT FLOOR IS:", self.curent_floor)
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





h=elevator()

build=Building(3)
build.run_elevator(2,4)
build.run_elevator(1,8)
build.run_elevator(3,6)
print(print(f"the elevator {build.elevator_list[0]} , is on floor :{h.curent_floor_list[0]} "))
print(print(f"the elevator {build.elevator_list[1]} , is on floor :{h.curent_floor_list[1]} "))
print(print(f"the elevator {build.elevator_list[2]} , is on floor :{h.curent_floor_list[2]} "))

