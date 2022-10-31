class elevator:
    def __init__(self,num_floor=10,curent_floor=0):
        self.num_floor=num_floor
        self.curent_floor=curent_floor


    def go_to_floor(self,floor):
        while self.curent_floor != floor:
            if floor > self.curent_floor:
                h.floor_up()
            elif floor < self.curent_floor:
                h.floor_down()
        print("YOU ARE IN CHOSEN FLOOR",h.curent_floor)



    def floor_up(self):
        print("CURRENT FLOOR IS:", self.curent_floor)
        self.curent_floor=self.curent_floor + 1



    def floor_down(self):
        print("CURRENT FLOOR IS:", self.curent_floor)
        while h.curent_floor != 0:
            self.curent_floor = self.curent_floor - 1
            print(h.curent_floor)






h=elevator()
h.go_to_floor(3)
h.floor_down()



