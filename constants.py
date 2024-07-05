SCREEN_TITLE = "Prachka"
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 800

CELL_WIDTH = 60
CELL_HEIGHT = 60
ROW_COUNT = 11
COLUMN_COUNT = 11
PLAYER_SPEED = 20

def justify_x(position_x, cell_width):
    for x in range(COLUMN_COUNT):
        cell_center_x = difference(x, cell_width)
        if position_x - cell_center_x <= cell_width / 2:
            return cell_center_x
def justify_y(position_y, cell_height):
    for y in range(ROW_COUNT):
        cell_center_y = difference(y, cell_height)
        if position_y - cell_center_y <= cell_height / 2:
            return cell_center_y
def difference(coordinate, distance):
    return coordinate * distance + distance / 2