from window import Window
from mouse1 import Mouse
import time

win = Window()

class Interface :
    def __init__(self) :
        self.pos_list = []
        self.mode = None
    
    def setClickOrder(self, count) :
        print("RGB를 추출할 부분을 클릭해주세요.")
        self.pos_list.append(win.getMouseEvent())

        time.sleep(0.2)

        for i in range(count) :
            print(i + 1, "번째 좌표를 클릭해주세요.")
            self.pos_list.append(win.getMouseEvent())
            
            time.sleep(0.2)

        return self.pos_list

    def setClickMode(self) :
        self.mode = str(input("모드를 입력해주세요 : "))
        return self.mode
    
    def start(self) :
        rgb = (109, 145, 236) #win.getPositionRGB(self.pos_list[0])
        del self.pos_list[0]
        mos = Mouse(False, self.pos_list, 5)

        mos.click(rgb, self.mode)
    
