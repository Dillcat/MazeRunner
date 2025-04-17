from cell import Cell
import time
import random

class Maze:
    def __init__(
        self,
        x1,
        y1,
        num_rows,
        num_cols,
        cell_size_x,
        cell_size_y,
        win=None,
        seed=None
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

        if seed:
            random.seed(seed)
    # call create_cells
        self._create_cells()
        self._break_entrance_and_exit()
        self._break_walls_r(0, 0)
        self._reset_cells_visited(0, 0)


    def _create_cells(self):
        self._cells = []
        
        for i in range(self._num_cols):
            cell_list = []
            for j in range(self._num_rows):
                cell_list.append(Cell(self._win))
            self._cells.append(cell_list)
        for i in range(self._num_cols):
            for j in range(self._num_rows):   
                self._draw_cell(i, j)

        print(self._cells)

        

    def _draw_cell(self, i, j):
        # x1, y1 start at top left
        # next cell starts at x1, y1 times size
        if self._win is None:
            return

        x1_pos = self._x1 + (i * self._cell_size_x)
        y1_pos = self._y1 + (j * self._cell_size_y)

        x2_pos = x1_pos + self._cell_size_x
        y2_pos = y1_pos + self._cell_size_y

        self._cells[i][j].draw(
            x1_pos, y1_pos, x2_pos, y2_pos
        )
        self._animate()

    def _animate(self):
        if self._win is None:
            return
        self._win.redraw()
        if self._num_cols < 5 or self._num_rows < 5: 
            time.sleep(0.001)
        else:
            time.sleep(0.001)
        


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)

    def _break_walls_r(self, i, j):
        self._cells[i][j].visited = True

        while True:
            need_visit = []
            
            #left
            if i > 0 and not self._cells[i - 1][j].visited:
                need_visit.append((i - 1, j))
            #right
            if i < self._num_cols - 1 and not self._cells[i + 1][j].visited:
                need_visit.append((i + 1, j))
            #top
            if j > 0 and not self._cells[i][j - 1].visited:
                need_visit.append((i, j - 1))
            #bottom
            if j < self._num_rows - 1 and not self._cells[i][j + 1].visited:
                need_visit.append((i, j + 1))
                
            if len(need_visit) == 0:
                self._draw_cell(i, j)
                return

            direction_index = random.randrange(len(need_visit))
            next_d = need_visit[direction_index]

            if next_d[0] == i + 1:
                self._cells[i][j].has_right_wall = False
                self._cells[i + 1][j].has_left_wall = False
            if next_d[0] == i - 1:
                self._cells[i][j].has_left_wall = False
                self._cells[i - 1][j].has_right_wall = False
            if next_d[1] == j + 1:
                self._cells[i][j].has_bottom_wall = False
                self._cells[i][j + 1].has_top_wall = False
            if next_d[1] == j - 1:
                self._cells[i][j].has_top_wall = False
                self._cells[i][j - 1].has_bottom_wall = False
                
            self._break_walls_r(next_d[0], next_d[1])

    def _reset_cells_visited(self, i, j):
        for i in range(self._num_cols):
            for j in range(self._num_rows):
                self._cells[i][j].visited = False
                print(self._cells[i][j])

    def _solve_r(self, i, j):
        self._animate()
        self._cells[i][j].visited = True

        if i == self._num_cols - 1 and j == self._num_rows - 1:
            return True

       #move left
        if (
            i > 0
            and not self._cells[i][j].has_left_wall
            and not self._cells[i - 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i - 1][j])
            if self._solve_r(i - 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i - 1][j], True)
            
        #move right
        if (
            i < self._num_cols
            and not self._cells[i][j].has_right_wall
            and not self._cells[i + 1][j].visited
        ):
            self._cells[i][j].draw_move(self._cells[i + 1][j])
            if self._solve_r(i + 1, j):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i + 1][j], True)
        
        #move top
        if (
            j > 0
            and not self._cells[i][j].has_top_wall
            and not self._cells[i][j - 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j - 1])
            if self._solve_r(i, j - 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j - 1], True)
        
        #move bottom
        if (
            j < self._num_rows
            and not self._cells[i][j].has_bottom_wall
            and not self._cells[i][j + 1].visited
        ):
            self._cells[i][j].draw_move(self._cells[i][j + 1])
            if self._solve_r(i, j + 1):
                return True
            else:
                self._cells[i][j].draw_move(self._cells[i][j + 1], True)

        return False

    def solve(self):
        return self._solve_r(0, 0)