import pyautogui
from PIL import Image, ImageGrab

import time

def hit(key):
    pyautogui.keyDown(key)
    return

def isCollide(data):
    # for birds detection
    for i in range(520, 548):
        for j in range(194,228 ):
            if data[i, j] < 90:
                hit("up")
                return
    # for cactus detection
    for i in range(520, 548):
        for j in range(164, 194):
            if data[i, j] < 90:
                hit("down")
                return
    return

if __name__ == "__main__":
    print("Dino start in 3 seconds")
    time.sleep(2)
    hit('up')

    while True:
        image = ImageGrab.grab().convert('L')
        data = image.load()
        isCollide(data)





