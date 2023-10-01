import time

#define the function
def countdown_timer(seconds):
    mins=int(seconds/60)
    secs=int(seconds%60)

    timer = f'{mins}:{secs}'

    print(timer)
        
    seconds -= 1

print('Time Up!')
  
  
# input time in seconds
seconds = input("Enter the time in number of seconds: ")
  
# function call
countdown_timer(int(seconds))