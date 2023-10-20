class Piece:
    location = (column, row)
    def __init__(self, team):
        self.team = team
        self.location = location
        self.type = type

    def get_location(self, location):
        return location
class King:
    def move_king(self, start_location, end_location):
        self.start_location = get_location

#   Can move one square in any direction
#   Can castle with the castle when no pieces are between them and the King is moving for the first time, moving to the midpoint
#   between the two pieces and swapping sides

# class Queen:
#   Can move in any direction any number of squares

# class Bishop:
#   Can move diagonally any number of squares

# class Rook:
#   Can move in an L shape in any direction

# class Castle:
#   Can move horizontally or vertically any number of squares

# class Pawn:
#   Can move two squares forward on the first move
#   Can move one square forward on every move but the first
#   Can attack diagonally
