import pyautogui as pg
import time

time.sleep(5)
time.sleep(3)
pg.write('spam chat akan terjadi dalam 1')
time.sleep(1)
pg.press('enter')
pg.write('spam chat akan terjadi dalam 2')
time.sleep(1)
pg.press('enter')
pg.write('spam chat akan terjadi dalam 3')
time.sleep(1)
pg.press('enter')
time.sleep(1)

text = open("E:\Project Website\python\python.spamchat2.0\katakata.txt","r")
for word in text:
    pg.write(word)
    pg.press("enter")