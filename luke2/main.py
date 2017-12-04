from test import Labyrint
import curses

def main():

    labyrint = Labyrint(10)
    labyrint.startEventyr()
    labyrint.printLabyrint()

#main()
skjerm = curses.initscr()

skjerm.addstr(0,0, "Hello WOrld!")
skjerm.refresh()
skjerm.getch()
skjerm.endwin()