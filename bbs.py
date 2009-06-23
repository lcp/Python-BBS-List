#!/usr/bin/env python

from os import system
import curses
import sys

sites = [
["PTT",     "ssh",    "bbs@ptt.cc"],
["PTT2",    "ssh",    "bbs@ptt2.cc"],
["SayYa",   "telnet", "bbs.sayya.org"],
["MathBBS", "telnet", "140.112.50.3"]
];

def execute_cmd(cmd_string):
        system("clear")
	a = system(cmd_string)

x = 0
option = 0;
screen = curses.initscr();

while x != ord('q') and x != ord('Q'):
	start_row = 2;

	screen.clear();
	screen.border(0);

	for i in range(0, len(sites)):
		print_str = str(i+1) + " - " + sites[i][0];
		if i != option:
			screen.addstr(start_row+i, 4, print_str);

	screen.addstr( start_row+i+2, 4, "Q - Exit");

	print_str = str(option+1) + " - " + sites[option][0];
	screen.addstr(start_row+option, 4, print_str, curses.A_REVERSE);

	screen.refresh();

	x = screen.getch();

	if x == 65: #curses.KEY_UP:
		option = option - 1;
	elif x == 66:  #curses.KEY_DOWN:
		option = option + 1;
	elif x == 10: #curses.KEY_ENTER:
		i = option;
		screen.clear();
		curses.endwin();
		execute_cmd( sites[i][1] + " " +  sites[i][2] );
		break;

	if option < 0:
		option = len(sites)-1;
	elif option >= len(sites):
		option = 0;

screen.clear();
curses.endwin();
