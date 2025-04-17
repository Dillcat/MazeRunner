from window import Window
from maze import Maze
import sys

def main():

    #c1 = Cell(win)
    #c1.has_right_wall = False
    #c1.draw(50, 50, 100, 100)

    #c2 = Cell(win)
    #c2.has_left_wall = False
    #c2.draw(100, 50, 150, 100)

    #c1.draw_move(c2)

    num_rows = 100
    num_cols = 160
    margin = 50
    screen_x = 1600
    screen_y = 1000
    win = Window(screen_x, screen_y)
    cell_size_x = (screen_x - 2 * margin) / num_cols
    cell_size_y = (screen_y - 2 * margin) / num_rows

    sys.setrecursionlimit(10000)

    m1 = Maze(margin, margin, num_rows, num_cols, cell_size_x, cell_size_y, win, 9)
    
    print("prepare to be aMAZEd!")
    is_solvable = m1.solve()
    if not is_solvable:
        print("this isn't so aMAZEing...")
    else:
        print("we MAZEd it!")

    #test
    #mt = Maze(10, 10, 3, 3, 100, 100, win)
    

    win.wait_for_close()
main()