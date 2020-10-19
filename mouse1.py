from PIL import ImageGrab as Ig
from multiprocessing import Process
import pyautogui as pg
import keyboard as kb
import threading as Th
import time
import sys

class Mouse :
    def __init__(self, is_poss_overlap, pos_range, click_range) :
        self.is_poss_overlap = is_poss_overlap
        self.pos_range = pos_range
        self.click_range = click_range

    def click(self, rgb, mode) :
        first_pos1 = min(self.pos_range[0][0], self.pos_range[1][0]) 
        second_pos1 = first_pos1 == self.pos_range[1][0] and self.pos_range[0][0] or self.pos_range[1][0]

        first_pos2 = min(self.pos_range[0][1], self.pos_range[1][1]) 
        second_pos2 = first_pos2 == self.pos_range[1][1] and self.pos_range[0][1] or self.pos_range[1][1]

        if(mode == "fast") :
            self.final_x, self.final_y = 0, 0
            def move() :
                while True :
                    screen = Ig.grab()
                    is_finished = False

                    for pos1 in range(first_pos1, second_pos1, 5) :
                        for pos2 in range(first_pos2, second_pos2, 5) :
                            pos_rgb = screen.getpixel((pos1, pos2))

                            if abs(pos_rgb[0] - rgb[0]) + abs(pos_rgb[1] - rgb[1]) + abs(pos_rgb[2] - rgb[2]) < 80 :
                                x, y = pos1 + self.click_range, pos2 + self.click_range
                                self.final_x, self.final_y = x, y
                    
                                pg.moveTo(x, y)

                                if not self.is_poss_overlap :
                                    is_finished = True
                                    break
            
                        if is_finished :
                            break

            Thread1 = Th.Thread(target=move)
            Thread1.daemon = True
            Thread1.start()

            def check() :
                if self.final_x != 0 or self.final_y != 0 :
                    pg.click()

            while True :
                check()

                if kb.is_pressed("x") :
                    print("종료")
                    sys.exit()
                    break

        elif(mode == "auto") :
            def move() :
                screen = Ig.grab()
                is_finished = False

                for pos1 in range(first_pos1, second_pos1, 5) :
                    for pos2 in range(first_pos2, second_pos2, 5) :
                        pos_rgb = screen.getpixel((pos1, pos2))

                        if abs(pos_rgb[0] - rgb[0]) + abs(pos_rgb[1] - rgb[1]) + abs(pos_rgb[2] - rgb[2]) < 80 :
                            x, y = pos1 + self.click_range, pos2 + self.click_range
                            
                            pg.moveTo(x, y)
                            pg.click()

                            if not self.is_poss_overlap :
                                is_finished = True
                                break
                
                    if is_finished :
                        break

            while True :
                move()

                if kb.is_pressed("x") :
                    print("종료")
                    sys.exit()
                    break
        
        else :
            print("지원하지 않는 모드입니다.")
            sys.exit()