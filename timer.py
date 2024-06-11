import time, board, digitalio

led = digitalio.DigitalInOut(board.GP3)
led.direction = digitalio.Direction.OUTPUT
led.value = False

power = digitalio.DigitalInOut(board.GP2)
power.direction = digitalio.Direction.OUTPUT
power.value = False

timer_dict = {True: 15*60, False: 45*60 }
timer_flag = True
timer = timer_dict[timer_flag]
time_stamp = time.monotonic()
while True:
    power.value = timer_flag
    if time.monotonic() - time_stamp >= 1:
        time_stamp = time.monotonic()
        led.value = not led.value
        if timer:
            timer -= 1
            print(f'{time.monotonic()}\t timer: {timer}\t flag: {timer_flag}')
        else:
            timer_flag = not timer_flag
            timer = timer_dict[timer_flag]
