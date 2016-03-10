import curses
myscreen = curses.initscr()

myscreen.border(0) 
myscreen.addstr(12, 25, "Python curses")
myscreen.refresh()
myscreen.getch()

curses.endwin()
