from test import Labyrint
import curses

def main():

    labyrint = Labyrint(10)
    labyrint.startEventyr()
    labyrint.printLabyrint()

main()