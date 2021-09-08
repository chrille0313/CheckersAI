from func import *


class Checkers:
    def __init__(self, rows, columns, boardWidth, boardHeight, color1=WHITE, color2=BLACK):
        self.rows, self.columns = rows, columns
        self.boardSize = self.boardWidth, self.boardHeight = boardWidth, boardHeight
        self.color1, self.color2 = color1, color2

        self.rectSize = Vector2(self.boardWidth/self.columns, self.boardWidth/self.rows)

        self.board = []
        for row in range(self.rows):
            evenRow = row % 2 == 0
            for column in range(self.columns):
                if evenRow:
                    color = self.color1 if column % 2 == 0 else self.color2
                else:
                    color = self.color2 if column % 2 == 0 else self.color1

                self.board.append(Tile(Vector2(row * self.rectSize.x, column * self.rectSize.y), self.rectSize.x, self.rectSize.y, color))

    def draw(self):
        [tile.draw() for tile in self.board]


class Tile:
    def __init__(self, pos, width, height, color, piece=None):
        self.pos = pos
        self.width, self.height = width, height
        self.color = color
        self.piece = piece if piece else None

    @property
    def occupied(self):
        return self.piece is not None

    def draw(self):
        draw_rect(self.pos.x, self.pos.y, self.width, self.height, 0, color=self.color)
