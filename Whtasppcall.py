import subprocess
import pyautogui
import time

def phone_number(number):
    url = f"whatsapp://send?phone=+91{number}"
    subprocess.Popen(["cmd", "/C", f"start {url}"], shell=True)

phone_number('9087270492')

#time.sleep(5)
#x, y = pyautogui.position()

# Print the position
#print(f"The current position of the mouse cursor is ({x}, {y})")

# Clicks whatsapp call button
pyautogui.moveTo(1439, 75)
pyautogui.click(duration=5)

#Start recording
time.sleep(30)
pyautogui.press('f12')

#Puts LK
pyautogui.hotkey('ctrl', 'alt', 'z')

time.sleep(120) #add timer in seconds
subprocess.call("TASKKILL /F /IM whatsapp.exe", shell=True)
