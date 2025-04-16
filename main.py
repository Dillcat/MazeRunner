from window import Window
from maze import Maze

def main():

    #c1 = Cell(win)
    #c1.has_right_wall = False
    #c1.draw(50, 50, 100, 100)

    #c2 = Cell(win)
    #c2.has_left_wall = False
    #c2.draw(100, 50, 150, 100)

    #c1.draw_move(c2)

    num_rows = 12
    num_cols = 16
    margin = 50
    screen_x = 800
    screen_y = 600
    win = Window(screen_x, screen_y)
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win)
    
    #test
    #mt = Maze(10, 10, 3, 3, 100, 100, win)
    

    win.wait_for_close()
main()