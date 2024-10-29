#Create a command line app that prompts for commands and moves a rover around a 2D plane.
#The robot should point in a direction, turn to face different directions, and move in the direction it is facing.


class Rover(object):
    def __init__(self, n=(0,0), direction ='N'):
        self.n = n
        position = list(n)
        self.directions = ["N", "E", "S", "W"]
        self.direction = direction
        self.x = position[0]
        self.y = position[1]

    def distance(self):
        return (self.x **2 + self.y **2)
    
    def position(self):
        print("x:", self.x, "y:", self.y)

    def turn_left (self):
        i = self.directions.index(self.direction)
        self.direction = self.directions[(i - 1)%4]
        print(f"turned left {self.direction}")

    def turn_right(self):
        i = self.directions.index(self.direction)
        self.direction = self.directions[(i + 1)%4]
        print(f"turned right {self.direction}")

    def movement (self, move):
        x_d = self.x
        y_d = self.y
        #print(direction)
        #print(move)
        if self.direction == "N":
            y_d = self.y + move
        if self.direction == "E":
            y_d = self.y - move
        if self.direction == "S":
            x_d = self.y + move 
        if self.direction == "W":
            x_d = self.x - move
            #print(y_d)
        self.x = x_d
        self.y = y_d
        #print(self.x)
        #print(self.y)
        #return 0


if __name__ == "__main__":
    #direction_list = ["N", "E", "S", "W"]
    list2 = ["R", "L"]
    
    rover = Rover()
    while True:
        inputlist1 = input("Enter the direction and points to move with space in between ").split()
        if inputlist1[0] in list2 and inputlist1[1].isnumeric():
            if inputlist1[0] == "L":
                rover.turn_left()
                rover.movement(int(inputlist1[1]))
                #print (rover.position())
                rover.position()
                print ("distance ",rover.distance())
            if inputlist1[0] == "R":
                rover.turn_right()
                rover.movement(int(inputlist1[1]))
                #print (rover.position())
                rover.position()
                print ("distance ",rover.distance())
        else:
            print("Invalid Input")
            break
    