import threading
import pyautogui
import time
def clicking(clicks,interval, button, clickTime):
    time_to = {"s": 1, "min": 60, "h": 360}
    time.sleep(3)
    for _ in range(10):
        #print(type(clicks), type(interval), type(button))
        if clickTime == "ms":
            pyautogui.click(clicks, interval/60, button)
        else:
            pyautogui.click(clicks=clicks, interval=interval*time_to[clickTime], button=button)

thread = threading.Thread(target=clicking, args=(1, 1, "right", "s"))
thread.start()
#for x in range(10):
    #pyautogui.click(clicks=1, interval=1, button="left")
pyautogui.click()
