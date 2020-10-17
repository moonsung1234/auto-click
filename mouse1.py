from PIL import ImageGrab as Ig
import pyautogui as pg

class Mouse :
    def __init__(self, is_poss_overlap, pos_range, click_range) :
        self.is_poss_overlap = is_poss_overlap
        self.pos_range = pos_range
        self.click_range = click_range

    def click(self, rgb) :
        print("1")

        first_pos1 = min(self.pos_range[0][0], self.pos_range[1][0]) 
        second_pos1 = first_pos1 == self.pos_range[1][0] and self.pos_range[0][0] or self.pos_range[1][0]

        first_pos2 = min(self.pos_range[0][1], self.pos_range[1][1]) 
        second_pos2 = first_pos2 == self.pos_range[1][1] and self.pos_range[0][1] or self.pos_range[1][1]

        screen = Ig.grab()

        print(first_pos1, ", ", second_pos1, " : ", first_pos2, ", ", second_pos2)

        for pos1 in range(first_pos1, second_pos1) :
            for pos2 in range(first_pos2, second_pos2) :
                if screen.getpixel((pos1, pos2)) == rgb :
                    pg.moveTo(pos1 + self.click_range, pos2 + self.click_range, 2)

                    if not self.is_poss_overlap :
                        return
                        
