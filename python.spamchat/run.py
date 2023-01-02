import pyautogui as pg
import time
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

try : 

        for i in range(1000):
         pg.write('lerry pemabok')
         pg.press('enter')
         pg.write('kevin fifa')
         pg.press('enter')
         pg.write('renaldi aerox')
         pg.press('enter')
         pg.write('steven wibu')
         pg.press('enter')


except KeyboardInterrupt: # ctrl + c
        print('febrian menyetop script')
