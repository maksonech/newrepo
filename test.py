import keyboard  # using module keyboard
import time
import pyautogui

while True:  # making a loop

    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('INS'):  # if key 'q' is pressed
            while True:

                print('You Pressed A Key!')
                pyautogui.click()
                time.sleep(0.02)
            #break  # finishing the loop
                if keyboard.is_pressed('END'):
                    print('Pause')
                    break





    except:
    #     if keyboard.is_pressed('q'):
             print('STOP!')
             break  # if user pressed a key other than the given key the loop will break