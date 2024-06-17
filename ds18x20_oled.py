# A 4.7Kohm pullup between DATA and POWER is REQUIRED!

import busio
import adafruit_ssd1306
import board
import time
import microcontroller
from adafruit_onewire.bus import OneWireBus
import adafruit_ds18x20

ow_bus = OneWireBus(board.GP3)
devices = ow_bus.scan()
# for device in devices:
    # print("Rom = {} \tFamily = 0x{:02x}".format([hex(i) for i in device.rom], device.family_code))
# print(devices)
ds18b20 = adafruit_ds18x20.DS18X20(ow_bus, devices[0])

i2c = busio.I2C(board.GP1, board.GP0) # инициализация шины I2C

oled = adafruit_ssd1306.SSD1306_I2C(128, 32, i2c) # инициализация дисплея
oled.fill(1)
oled.show()
time.sleep(0.2)
print('Temperature: {0:0.3f} °C'.format(ds18b20.temperature))


while True:
    temp = ds18b20.temperature
    oled.fill(0)
    oled.text(f'{temp:.2f}C', 20, 10, 1, font_name='font5x8.bin', size=2)
    oled.show()
    time.sleep(1)
