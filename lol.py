import pyautogui

def lol_button():
    print('หาห้องอยู่')
    while True:
        try:
            location = pyautogui.locateOnScreen('lol/accept.png')
            print('เจอห้องแล้ว')
            pyautogui.moveTo(location)
            pyautogui.click(location)
            break
        except:
            pyautogui.ImageNotFoundException
    exit()

lol_button()