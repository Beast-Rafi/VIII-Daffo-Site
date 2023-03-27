import pyautogui as pg
import time
x = input("Type:")
y = input("multitime")
time.sleep(3)
for i in range(int(y)):
    pg.typewrite(x)
    pg.click(1183, 688)
    pg.click(1268, 691)