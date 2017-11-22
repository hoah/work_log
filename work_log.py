import csv
import datetime
import os
import re

from task import Task


def clear():
    '''Clears console.'''
    os.system('cls' if os.name == 'nt' else 'clear')


def menu():
    '''Displays the ciper options'''
    main_menu = '''WORK LOG
What would you like to do?
a) Add new entry
b) Search in exiting entries
c) Quit program
'''
    print(main_menu)


def new_entry():
    print('new entry menu')


def search():
    print('search menu')


def write_csv():
    print('write csv message')


def main():
    while True:
        clear()
        menu()
        # get choice
        choice = input('> ').lower()
        while choice not in ['a', 'b', 'c']:
            choice = input(
                "That's not an option. Would you like a, b, or c? ").lower()

        if choice == 'a':
            # run Add new entry
            new_entry()
        elif choice == 'b':
            # run Search in existing entries
            search()
        elif choice == 'c':
            check = input('Are you sure you want to quit? (y/n) ').lower()
            if check == 'y':
                # write to csv file before exiting program
                write_csv()
                # quit program
                break


tasks = []  # list of tasks

if __name__ == '__main__':
    main()
