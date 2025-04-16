from cell import Cell
import time

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
    ):
        self._x1 = x1
        self._y1 = y1
        self._num_rows = num_rows
        self._num_cols = num_cols
        self._cell_size_x = cell_size_x
        self._cell_size_y = cell_size_y
        self._win = win
        self._cells = []

    # call create_cells
        self._create_cells()
        self._break_entrance_and_exit()


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
            time.sleep(0.3)
        else:
            time.sleep(0.01)
        


    def _break_entrance_and_exit(self):
        self._cells[0][0].has_top_wall = False
        self._draw_cell(0, 0)
        self._cells[self._num_cols - 1][self._num_rows - 1].has_bottom_wall = False
        self._draw_cell(self._num_cols - 1, self._num_rows - 1)