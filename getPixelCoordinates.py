import pyautogui

while True:
    currentMouseX, currentMouseY = pyautogui.position()  # get the current mouse cursor position
    print(currentMouseX, currentMouseY)