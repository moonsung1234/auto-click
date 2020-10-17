from window import Window
from mouse1 import Mouse

win = Window()
pos_list = []

def mouse(rgb) :
    mos = Mouse(False, pos_list, 0)
    mos.click(rgb)

def callback(position) :
    print("position : ", position)
    print("rgb : ", win.getPositionRGB(position))
    
    x, y = position
    pos_list.append((x, y))

    if win.event_count != 1 :
        print("두번째 좌표를 클릭하세요.")

def main() :
    print("첫번째 좌표를 클릭하세요.")
    win.setMouseEvent(2, callback)

    print("시작.")
    mouse(win.getPositionRGB(pos_list[0]))

main()
