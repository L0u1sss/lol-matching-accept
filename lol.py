import pyautogui
def lol_button():
    print('หาห้องอยู่')
    while True:
        try:
            location = pyautogui.locateOnScreen('accept.png',confidence=0.6)
            print('เจอห้องแล้ว')
            pyautogui.moveTo(location)
            pyautogui.click(location)
            break
        except:
            pyautogui.ImageNotFoundException
    exit()

lol_button()