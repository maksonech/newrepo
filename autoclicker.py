import keyboard
import pyautogui
import time

while True:

    try:
        if keyboard.is_pressed('INS'):
            while True:
                pyautogui.click(button='right')
                print('GO')
                pyautogui.click(button='right')
                time.sleep(0.002)
                
                if keyboard.is_pressed('END'):
                    print('Pause')
                    break

    except:

        print('ERROR!')
        break
