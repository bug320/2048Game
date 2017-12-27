# -*- coding:utf-8 -*-
import curses

class ExitException(Exception):
    pass

def curses_main(stdscr):
    stdscr.addstr("Hello world")
    screen = curses.newwin(30,30,1,10)
    screen.addstr("New screen")
    stdscr.refresh()
    screen.refresh()
    while True:
        if stdscr.getch() == ord('q'):
            raise ExitException("Deault quiting")

            pass
    pass

if __name__ == '__main__':
    curses.wrapper(curses_main)
    pass