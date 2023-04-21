from time import sleep

# countdown for things that take a long time
def countdown(t):
    print('Countdown Before Continuing:')
    while t:
        mins, secs = divmod(t, 60)
        timer = '{:02d}:{:02d}'.format(mins, secs)
        print(timer, end="\r")
        sleep(1)
        t -= 1
countdown(10)