#this is count down timer
#
#import time
import time

# declear time
#
#
#
#
def countdown(t):
    while t:
        min , secs = divmod(t,60)
        timer = '{:02d}:{:02d}'.format(min,secs)
        print(timer,end='\n')
        time.sleep(1)
        t -= 1
        if t == 0:
            print_message()

def print_message():
    print('this count is done ')


t= input('enter : ')
countdown(int(t))