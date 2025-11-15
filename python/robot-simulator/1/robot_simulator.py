EAST = "EAST"
NORTH = "NORTH"
WEST = "WEST"
SOUTH = "SOUTH"

DIRECTIONS = (SOUTH, WEST, NORTH, EAST)
VALUES = (-1,-1, 1, 1)

class Robot:
    def __init__(self, direction=NORTH, x_pos=0, y_pos=0):
        self.direction   = direction
        self.coordinates = (x_pos, y_pos)
        
    def move(self, commands):
        index = DIRECTIONS.index(self.direction)
        coord = list(self.coordinates)
        for command in commands:
            if command == "L":
                index = (index - 1) % 4
            elif command == "R":
                index = (index + 1) % 4
            else:
                if index == 1 or index == 3:
                    coord[0] += VALUES[index]
                else:
                    coord[1] += VALUES[index]

        self.direction   = DIRECTIONS[index]
        self.coordinates = tuple(coord)
