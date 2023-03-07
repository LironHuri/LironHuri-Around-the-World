import pygame
import time
import screen


width,height=screen.background_resolution()

def blit_rotate_center(wn,image,top_left,angle):
    rotated_image=pygame.transform.rotate(image,angle)
    new_rect=rotated_image.get_rect(
        center=image.get_rect(topleft=top_left).center)
    wn.blit(rotated_image,new_rect.topleft)

def blit_text_center(wn,font,text):
    render=font.render(text,1,(200,200,200))
    wn.blit(render,(render.get_width()*(5/52),render.get_height()*(5/3)))

def fuel_tank_text(wn,color,font,text):
    if color=="white":
        render=font.render(text,1,(255,255,255))
    else:
        render=font.render(text,1,(0,0,0))
    if len(text)==3:
        wn.blit(render,(width*(37/44),height*(191/216)))
    if len(text)==2:
        wn.blit(render,(width*(113/132),height*(191/216)))
    elif len(text)==1:
        wn.blit(render,(width*(115/132),height*(191/216)))



def main():
    print("classes & functions is ON")
    print(f"working from {__name__}")


if "__main__"==__name__:
    main()
