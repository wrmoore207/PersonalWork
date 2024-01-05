# This is a simple program for a countdown timer
# October 27, 2022

# Time Library Docs: 
# https://docs.python.org/3/library/time.html

# source code
# https://www.geeksforgeeks.org/how-to-create-a-countdown-timer-using-python/

# import the time module
import time

# define the countdown func.
def countdown(t):

    for i in range(4):
        while t:
            mins, secs = divmod(t, 60)
            timer = '{:02d}:{:02d}'.format(mins, secs)
            print(timer, end="\r")
            time.sleep(1)
            t -= 1
            i +=1
            print("test")
# input time in seconds
t = input("Enter the time in seconds: ")

# function call
countdown(int(t))


