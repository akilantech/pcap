from time import sleep

seconds = 0

while True:
    try:
        print(seconds)
        seconds += 1
        print(seconds)
        sleep(1)
    except KeyboardInterrupt:
        print("Don't do that!")