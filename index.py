
from window import Window

win = Window()

def callback(position) :
    print("position : ", position)
    print("rgb : ", win.getPositionRGB(position))
    
    if win.event_count != 1 :
        print("두번째 좌표를 클릭하세요.")

print("첫번째 좌표를 클릭하세요.")
win.setMouseEvent(2, callback)

