import pygame
import math
import sounds
from utils import blit_rotate_center


class Plane(pygame.sprite.Sprite):

    def __init__(self,x,y,plane_type,plane_name,plane_color,angle=0):
        super(self.__class__, self).__init__()
        self.image=pygame.image.load(f"imgs/{plane_type}.{plane_name}.{plane_color}.gif").convert()
        self.x=x
        self.y=y
        self._vx=1
        self._vy=1
        self.angle=angle
        self.max_vel=3
        self.vel=1
        self.rotation_vel=4
        self.acceleration=0.1
        self.fuel=100
        self.COUNTER=0

    def update_v(self, vx,vy):
        self._vx=vx
        self._vy=vy

    def update_loc(self):
        self.x+=self._vx
        self.y+=self._vy

    def get_pos(self):
        return (self.x,self.y)

    def get_v(self):
        return self._vx,self._vy

    def rotate(self,left=False,right=False):
        if left:
            self.angle+=self.rotation_vel
        elif right:
            self.angle-=self.rotation_vel

    def move(self):
        try:
            if self.fuel>0:
                radians=math.radians(self.angle)
                vertical=math.cos(radians)*self.vel
                horizontal=math.sin(radians)*self.vel
                
                self.y-=vertical
                self.x-=horizontal
                self.COUNTER+=1

                if self.COUNTER==30:
                    self.fuel-=1
                    self.COUNTER=0
        except TypeError:
            None

    def move_forward(self):
        self.vel=min(self.vel+self.acceleration,self.max_vel)
        self.move()

    def add_fuel(self):
        if self.fuel+15<=100:
            self.fuel+=15
        else:
            self.fuel=100

    def substract_fuel(self):
        self.fuel-=1
        
    def draw(self,wn):
        blit_rotate_center(wn,self.image,(self.x, self.y),self.angle)
        


def main():
    print("classes & functions is ON")
    print(f"working from {__name__}")


if "__main__"==__name__:
    main()
