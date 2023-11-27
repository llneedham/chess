class Piece:
    def __init__(self, team, location: Coordinate, status):
        self.team = team
        self.location = location
        self.type = type
        self.status = status


class King:
    def move(self, start_location, end_location):
        self.start_location = location
        end_location = input('Please enter the coordinate you want to move to:    ')


#   Can move one square in any direction
#   Can castle with the castle when no pieces are between them and the King is moving for the first time, moving to the midpoint
#   between the two pieces and swapping sides

class Queen:
    def move(self, start_location, end_location):
        self.start_location = location
#   Can move in any direction any number of squares

class Bishop:
    pass
#   Can move diagonally any number of squares

class Rook:
    pass
#   Can move in an L shape in any direction

class Castle:
    pass
#   Can move horizontally or vertically any number of squares

class Pawn:
    pass

#   Can move two squares forward on the first move
#   Can move one square forward on every move but the first
#   Can attack diagonally
