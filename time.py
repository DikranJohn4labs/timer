import time


def countdown(timer):
    parts = timer.split(":")
    h = int(parts[0])
    m = int(parts[1])
    s = int(parts[2])

    total = h*3600 + m*60 + s

    while total >= 0:
        h = total // 3600
        m = (total % 3600) // 60
        s = total % 60

        print(f"{h:02}:{m:02}:{s:02}")  # String
        time.sleep(1)
        total -= 1

timer = input("Insert time to count down (h:m:s): ")
countdown(timer)