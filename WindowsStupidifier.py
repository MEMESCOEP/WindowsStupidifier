### Windows Stupidifier ###
## IMPORTS ##
from playsound import playsound
import rotatescreen
import pyautogui
import keyboard
import win32con
import win32api
import win32gui
import random
import ctypes
import string
import time
import os

## VARIABLES ##
CursorPath = "CURSErZ\\"
SoundPath = "SOUNDZ\\"
ImagePath = "IMAGEz\\"
Cursor = win32gui.LoadImage(0, os.path.abspath(CursorPath + "CERSER.cur"), win32con.IMAGE_CURSOR, 0, 0, win32con.LR_LOADFROMFILE)
WallpaperPath = os.path.abspath(ImagePath + "highest_quality_wallpaper.bmp")
SPI_SetDesktopWallpaper = 20
SoundFiles = []
SndListLength = 0
screen = rotatescreen.get_primary_display()
keys = list(string.ascii_letters) + ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

## FUNCTIONS ##
# Change the system cursor
def SetSystemMouseCursor(CursorIMG):    
    ctypes.windll.user32.SetSystemCursor(CursorIMG, 32512)
    ctypes.windll.user32.DestroyCursor(CursorIMG)

# Change the desktop wallpaper
def SetWallpaper(AbsoluteWallpaperPath):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, AbsoluteWallpaperPath, 0)

## MAIN CODE ##
# Find all sound files that are located in a folder defined by the "SoundPath" variable. After that, detect the length of the sound file array
for file in os.listdir(SoundPath):
    if file.endswith('.wav') or file.endswith('.mp3'):
        SoundFiles.append(SoundPath + file)
        print("[INFO] >> Found sound file \"{}\"".format(SoundPath + file))

SndListLength = len(SoundFiles) - 1

# Disable pyautogui's failsafe because it'll kill the script (nasty!!1111)
pyautogui.FAILSAFE = False
        
# Change the mouse cursor and wallpaper images
SetWallpaper(WallpaperPath)
SetSystemMouseCursor(Cursor)

# Play random sounds and press random keys
while(True):
    playsound(SoundFiles[random.randint(0, SndListLength)], False)

    RNG = random.randint(1, 10)

    match RNG:
        case 1:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 0.1))
                keyboard.press_and_release("CAPSLOCK")

        case 2:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 0.1))
                keyboard.press_and_release("SHIFT")

        case 3:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 0.1))
                keyboard.press_and_release("TAB")

        case 4:
            pyautogui.moveRel(random.randint(-1000, 1000), random.randint(-1000, 1000), duration=random.uniform(0.1, 1))

        case 5:
            os.system("start {}".format(os.path.abspath(ImagePath + "fukyou.jpg")))

        case 6:
            start_pos = screen.current_orientation
            for i in range(1, 5):
                pos = abs((start_pos - i*90) % 360)
                screen.rotate_to(pos)
                time.sleep(random.uniform(0.1, 0.5))

        case 7:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 0.1))
                keyboard.press_and_release("WIN")

        case 8:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 1))
                keyboard.press_and_release(keys[random.randint(0, len(keys) - 1)])

        case 9:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 1))
                keyboard.write("MEOw :3")

        case 10:
            for x in range(random.randint(1, 10)):
                time.sleep(random.uniform(0.01, 1))
                keyboard.press_and_release("enter")
            
        case _:
            pass
        
    time.sleep(random.uniform(0.01, 1))
