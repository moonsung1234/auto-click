
from PIL import ImageGrab as Ig
import pyautogui as pg
import mouse
import time

class Window :
    def setMouseEvent(self, event_count, callback) :
        self.event_count = event_count

        while True:
            if mouse.is_pressed("left") and self.event_count != 0 :
                callback(pg.position())
                self.event_count += -1
            
            elif self.event_count == 0 :
                break

            time.sleep(0.1)

    def getPositionRGB(self, position) :
        po_X, po_Y = position
        screen = Ig.grab()

        return screen.getpixel((po_X, po_Y))


                
        