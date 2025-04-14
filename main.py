from window import Window, Line, Point

def main():
    win = Window(1000, 800)
    l = Line(Point(100, 150), Point(400, 400))
    win.draw_line(l, "red")
    win.wait_for_close()

main()