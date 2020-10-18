from window import Window
from mouse1 import Mouse

win = Window()
pos_list = []
target_rgb = None

def mouse(rgb) :
    del pos_list[0]
    mos = Mouse(False, pos_list, 3)
    mos.click(rgb)

def callback(position) :
    x, y = position
    rgb = win.getPositionRGB(position)
    pos_list.append((x, y))
    
    print("position : ", position)
    print("rgb : ", rgb)

    if win.event_count == 3 :
        global target_rgb 
        target_rgb = rgb 
        
        print("target rgb : ", target_rgb)
        print("첫번째 좌표를 클릭하세요.")

    if win.event_count == 2 :
        print("두번째 좌표를 클릭하세요.")

def main() :
    print("RPG를 추출할 부분을 클릭하세요.")
    win.setMouseEvent(3, callback)

    print("시작 : ", target_rgb)
    mouse(target_rgb)

main()
