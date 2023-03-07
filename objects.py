import pygame
import math
import screen
from utils import blit_rotate_center

width,height=screen.background_resolution()

class OrdinaryButton(pygame.sprite.Sprite):
    width,height=screen.background_resolution()

    def __init__(self,x,y,file_name,angle=0):
        super().__init__()
        self.image=pygame.image.load(f"imgs/{file_name}.gif")
        self.rect=self.image.get_rect()
        self.x=x
        self.y=y
        self.angle=0
        self.max_vel=10
        self.vel=8
        self.acceleration=0.1
    

    def get_pos(self):
        return (self.x,self.y)

    def draw(self,wn):
        blit_rotate_center(wn,self.image,(self.x, self.y),self.angle)


class TryAgain(OrdinaryButton):

    def __init__(self):
        super().__init__(width+50,height*(35/54),"Try_Again_Button")

    def animation(self):
        if self.x>width*(145/198):
            self.x-=1*self.vel



def main():
    print("classes & functions is ON")
    print(f"working from {__name__}")


if "__main__"==__name__:
    main()
