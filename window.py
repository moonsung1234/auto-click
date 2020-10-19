from PIL import ImageGrab as Ig
import pyautogui as pg
import mouse
import time

class Window :
    def getMouseEvent(self) :
        while True:
            if mouse.is_pressed("left") :
                return pg.position()

    def getPositionRGB(self, position) :
        po_X, po_Y = position
        screen = Ig.grab()

        return screen.getpixel((po_X, po_Y))


                
        