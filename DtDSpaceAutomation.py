import pyautogui
import time
from pynput.keyboard import Controller

x, y = 1112, 970  # coordinates of the pixel
green_bar = (0, 194, 0)  # in RGB
delay = 0.01  # delay in seconds, 0.5s = 500ms

keyboard = Controller()

while True:
    pixel_color = pyautogui.pixel(x, y)
    print(f"Current color: {pixel_color}")

    if pixel_color == green_bar:
        continue
    else:
        keyboard.press(' ')
        print('Spacebar pressed')
        time.sleep(0.01)
        keyboard.release(' ')
        time.sleep(delay)
