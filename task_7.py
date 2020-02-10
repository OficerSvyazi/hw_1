#!/usr/bin/python3

from pyrob.api import *
@task
def task_5_4():
    while not wall_is_beneath():
        move_down()
    if wall_is_beneath():
        while True:
            move_right()
            if not wall_is_beneath():
                move_down(1)
                move_left(1)
                if not wall_is_on_the_left()==True:
                     break
    if not wall_is_on_the_left():
            while True:
                move_left()
                if wall_is_on_the_left()==True:
                     break-
    pass


if __name__ == '__main__':
    run_tasks()
