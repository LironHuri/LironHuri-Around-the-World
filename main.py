#main

import pygame
import random
import planes
import objects
import screen
import sounds
from utils import blit_rotate_center,blit_text_center,fuel_tank_text

#constants
wn_width,wn_height=screen.background_resolution()

#init screen
pygame.init()
size=(wn_width,wn_height)
wn=pygame.display.set_mode(size,pygame.FULLSCREEN)
pygame.display.set_caption("imgs/Around the World")

#upload screen background
wn_image,curr_background=pygame.image.load("imgs/map_part_1.gif"),"map_part_1"
wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
wn.blit(wn_image,(0,0))
pygame.display.flip()

#add timer
clock=pygame.time.Clock()
REFRESH_RATE=60

#Buttons
try_again_width,try_again_height=screen.object_resolution(200,202)

try_again=objects.TryAgain()
try_again.image=pygame.transform.scale(try_again.image,(try_again_width,try_again_height))
try_again.image=pygame.transform.rotate(try_again.image,0)
wn.blit(try_again.image,try_again.get_pos())

#icons
fuel_tank_width,fuel_tank_height=screen.object_resolution(66,77)

black_fuel_tank=objects.OrdinaryButton(wn_width*(59/66),wn_height*(47/54),"black_fuel_tank",0)
black_fuel_tank.image=pygame.transform.scale(black_fuel_tank.image,(fuel_tank_width,fuel_tank_height))
black_fuel_tank.image=pygame.transform.rotate(black_fuel_tank.image,0)
wn.blit(black_fuel_tank.image,black_fuel_tank.get_pos())

white_fuel_tank=objects.OrdinaryButton(wn_width*(59/66),wn_height*(47/54),"white_fuel_tank",0)
white_fuel_tank.image=pygame.transform.scale(white_fuel_tank.image,(fuel_tank_width,fuel_tank_height))
white_fuel_tank.image=pygame.transform.rotate(white_fuel_tank.image,0)
wn.blit(white_fuel_tank.image,white_fuel_tank.get_pos())

#add plane
plane_width,plane_height=screen.object_resolution(66,69)

mpl=planes.Plane(wn_width*(1/2),wn_height*(25/54),"jet","by_me","blue",0)
mpl.image=pygame.transform.scale(mpl.image,(plane_width,plane_height))
mpl.image=pygame.transform.rotate(mpl.image,mpl.angle)
wn.blit(mpl.image,mpl.get_pos())

#text
MAIN_FONT=pygame.font.SysFont("Consolas",44)
FUEL_TANK_FONT=pygame.font.SysFont("Consolas",60)

#background sounds
sounds.game_playing()



images=[(wn_image,(0,0))]
def draw(wn,curr_background,APEAR_TRY_AGAIN=False):
    for img,pos in images:
        wn.blit(img,pos)

    if curr_background=="map_part_1" or curr_background=="map_part_2" or curr_background=="map_part_3" or curr_background=="map_part_4":
        blit_text_center(
            wn,MAIN_FONT,f"Fly to: {curr_destination[1]}")

    if curr_background=="map_part_1" or curr_background=="map_part_1_game_over" or curr_background=="map_part_2" or curr_background=="map_part_2_game_over":
        white_fuel_tank.draw(wn)
        fuel_tank_text(
            wn,"white",FUEL_TANK_FONT,f"{mpl.fuel}")
    elif curr_background=="map_part_3" or curr_background=="map_part_3_game_over" or curr_background=="map_part_4" or curr_background=="map_part_4_game_over":
        black_fuel_tank.draw(wn)
        fuel_tank_text(
            wn,"black",FUEL_TANK_FONT,f"{mpl.fuel}")
    
    if APEAR_TRY_AGAIN:
        try_again.draw(wn)
        try_again.animation()

    mpl.draw(wn)
    pygame.display.update()


def move_player():
    keys=pygame.key.get_pressed()

    if event.type==pygame.KEYDOWN and draw_plane==True:
        if keys[pygame.K_RIGHT]:
            mpl.rotate(right=True)
        if keys[pygame.K_LEFT]:
            mpl.rotate(left=True)
        if keys[pygame.K_UP]:
            mpl.move_forward()
            

def rand_destination():
    global curr_destination

    if len(destinations)==0:
        curr_destination=("X","X")
    if len(destinations)>0:
        curr_destination=destinations[random.randint(0,len(destinations)-1)]


def restart():
    wn_image,curr_background=pygame.image.load("imgs/map_part_3.gif"),"map_part_3"
    wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
    wn.blit(wn_image,(0,0))
    images=[(wn_image,(0,0))]
    pygame.display.update()
    mpl=planes.Plane(wn_width*(1/2),wn_height*(25/54),"jet","by_me","blue",0)
    mpl.image=pygame.transform.scale(mpl.image,(plane_width,plane_height))
    mpl.image=pygame.transform.rotate(mpl.image,mpl.angle)
    wn.blit(mpl.image,mpl.get_pos())
    return

def set_destinations():
    global destinations
    destinations=[("map_part_1","Israel"),
                  ("map_part_1","India"),
                  ("map_part_1","Japan"),
                  ("map_part_1","Turkey"),
                  ("map_part_1","Italy"),
                  ("map_part_1","Ethiopia"),
                  ("map_part_2","U.S.A"),
                  ("map_part_2","Canada"),
                  ("map_part_2","Mexico"),
                  ("map_part_3","Zimbabwe"),
                  ("map_part_3","Madagascar"),
                  ("map_part_3","Australia"),
                  ("map_part_4","Brazil"),
                  ("map_part_4","Chile"),
                  ("map_part_4","Argentina")]#15 Countries
set_destinations()


rand_destination()

finish=False
draw_plane=True
APEAR_TRY_AGAIN=False

blit_text_center(
    wn,MAIN_FONT,f"Fly to: {curr_destination[1]}")
fuel_tank_text(
    wn,"white",FUEL_TANK_FONT,f"{mpl.fuel}")

pygame.display.update()

sprites=pygame.sprite.Group()
#sprites.add(mpl)
sprites.add(try_again)

while not finish:
    clock.tick(REFRESH_RATE)

    draw(wn,curr_background,APEAR_TRY_AGAIN)

    
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            finish=True
        #elif event.type==pygame.KEYDOWN:
            #if event.key==pygame.K_RIGHT:
                #mpl.add_to_angle()
        if event.type==pygame.MOUSEBUTTONUP:
            pos=pygame.mouse.get_pos()

            # get a list of all sprites that are under the mouse cursor
            clicked_sprites=[s for s in sprites if s.rect.collidepoint(pos) and s==try_again]
            if pygame.mouse.get_pressed()[0]:
                pass
            draw_plane=True
            APEAR_TRY_AGAIN=False
            wn_image,curr_background=pygame.image.load("imgs/map_part_1.gif"),"map_part_1"
            wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
            wn.blit(wn_image,(0,0))
            images=[(wn_image,(0,0))]
            pygame.display.update()
            mpl=planes.Plane(wn_width*(1/2),wn_height*(25/54),"jet","by_me","blue",0)
            mpl.image=pygame.transform.scale(mpl.image,(plane_width,plane_height))
            mpl.image=pygame.transform.rotate(mpl.image,mpl.angle)
            wn.blit(mpl.image,mpl.get_pos())
            try_again.x=wn_width+wn_width*(5/198)
            set_destinations()
            rand_destination()
            sounds.game_playing()



    mpl.move_forward()
    #print(f"{mpl.angle},(x,y): ({mpl.x},{mpl.y})")

    move_player()
    

    if mpl.x<=wn_width*(-31/1980) and curr_background=="map_part_1":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_2.gif"),"map_part_2"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(377/396)
    elif mpl.y>=wn_height*(349/360) and curr_background=="map_part_1":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_3.gif"),"map_part_3"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.y=wn_height*(-31/1080)
    elif mpl.x>=wn_width*(943/990) and curr_background=="map_part_1":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_2.gif"),"map_part_2"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(-1/66)
    elif mpl.y<=wn_height*(-31/1080) and curr_background=="map_part_1":
        mpl.fuel="X"
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load("imgs/map_part_1_game_over.gif"),"map_part_1_game_over"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()


    elif mpl.x>=wn_width*(943/990) and curr_background=="map_part_2":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_1.gif"),"map_part_1"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(-1/66)
    elif mpl.y>=wn_height*(349/360) and curr_background=="map_part_2":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_4.gif"),"map_part_4"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.y=wn_height*(-31/1080)
    elif mpl.x<=wn_width*(-31/1980) and curr_background=="map_part_2":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_1.gif"),"map_part_1"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(377/396)
    elif mpl.y<=wn_height*(-31/1080) and curr_background=="map_part_2":
        mpl.fuel="X"
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load("imgs/map_part_2_game_over.gif"),"map_part_2_game_over"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        

    elif mpl.x<=wn_width*(-31/1980) and curr_background=="map_part_3":
        wn_image,curr_background=pygame.image.load("imgs/map_part_4.gif"),"map_part_4"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(377/396)
    elif mpl.y<=wn_height*(-4/135) and curr_background=="map_part_3":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_1.gif"),"map_part_1"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.y=wn_height*(523/540)
    elif mpl.x>=wn_width*(943/990) and curr_background=="map_part_3":
        wn_image,curr_background=pygame.image.load("imgs/map_part_4.gif"),"map_part_4"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(-1/66)
    elif mpl.y>=wn_height*(349/360) and curr_background=="map_part_3":
        mpl.fuel="X"
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load("imgs/map_part_3_game_over.gif"),"map_part_3_game_over"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()


    elif mpl.x>=wn_width*(943/990) and curr_background=="map_part_4":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_3.gif"),"map_part_3"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(-1/66)
    elif mpl.y<=wn_height*(-4/135) and curr_background=="map_part_4":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_2.gif"),"map_part_2"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.y=wn_height*(523/540)
    elif mpl.x<=wn_width*(-31/1980) and curr_background=="map_part_4":
        draw_plane=True
        wn_image,curr_background=pygame.image.load("imgs/map_part_3.gif"),"map_part_3"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
        mpl.x=wn_width*(377/396)
    elif mpl.y>=wn_height*(349/360) and curr_background=="map_part_4":
        mpl.fuel="X"
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load("imgs/map_part_4_game_over.gif"),"map_part_4_game_over"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()



    if wn_width*(109/660)<=mpl.x<=wn_width*(59/330) and  wn_height*(53/90)<=mpl.y<=wn_height*(86/135) and curr_background==curr_destination[0] and curr_destination[1]=="Israel":
        destinations.pop(destinations.index(("map_part_1","Israel")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif (wn_width*(137/396)<=mpl.x<=wn_width*(301/660) and wn_height*(377/540)<=mpl.y<=wn_height*(211/270) and curr_background==curr_destination[0] and curr_destination[1]=="India") or (wn_width*(743/1980)<=mpl.x<=wn_width*(43/99) and wn_height*(211/270)<=mpl.y<=wn_height*(949/1980) and curr_background==curr_destination[0] and curr_destination[1]=="India"):
        destinations.pop(destinations.index(("map_part_1","India")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif (wn_width*(1469/1980)<=mpl.x<=wn_width*(17/22) and wn_height*(55/108)<=mpl.y<=wn_height*(71/135) and curr_background==curr_destination[0] and curr_destination[1]=="Japan") or (wn_width*(1421/1980)<=mpl.x<=wn_width*(299/396) and wn_height*(283/540)<=mpl.y<=wn_height*(121/216) and curr_background==curr_destination[0] and curr_destination[1]=="Japan") or (wn_width*(112/165)<=mpl.x<=wn_width*(299/396) and wn_height*(67/120)<=mpl.y<=wn_height*(229/360) and curr_background==curr_destination[0] and curr_destination[1]=="Japan"):
        destinations.pop(destinations.index(("map_part_1","Japan")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(61/495)<=mpl.x<=wn_width*(449/1980) and wn_height*(91/180)<=mpl.y<=wn_height*(101/180) and curr_background==curr_destination[0] and curr_destination[1]=="Turkey":
        destinations.pop(destinations.index(("map_part_1","Turkey")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif (wn_width*(31/660)<=mpl.x<=wn_width*(3/44) and wn_height*(49/90)<=mpl.y<=wn_height*(17/30) and curr_background==curr_destination[0] and curr_destination[1]=="Italy") or (wn_width*(53/1980)<=mpl.x<=wn_width*(9/110) and wn_height*(31/60)<=mpl.y<=wn_height*(59/108) and curr_background==curr_destination[0] and curr_destination[1]=="Italy") or (wn_width*(61/1980)<=mpl.x<=wn_width*(19/220) and wn_height*(1/2)<=mpl.y<=wn_height*(14/27) and curr_background==curr_destination[0] and curr_destination[1]=="Italy") or (wn_width*(17/660)<=mpl.x<=wn_width*(113/1980) and wn_height*(49/108)<=mpl.y<=wn_height*(271/540) and curr_background==curr_destination[0] and curr_destination[1]=="Italy"):
        destinations.pop(destinations.index(("map_part_1","Italy")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif (wn_width*(31/180)<=mpl.x<=wn_width*(163/660) and wn_height*(937/1980)<=mpl.y<=wn_height*(25/27) and curr_background==curr_destination[0] and curr_destination[1]=="Ethiopia") or (wn_width*(119/660)<=mpl.x<=wn_height*(71/330) and wn_height*(49/60)<=mpl.y<=wn_height*(313/360) and curr_background==curr_destination[0] and curr_destination[1]=="Ethiopia"):
        destinations.pop(destinations.index(("map_part_1","Ethiopia")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(557/1980)<=mpl.x<=wn_width*(11/18) and  wn_height*(79/180)<=mpl.y<=wn_height*(131/216) and curr_background==curr_destination[0] and curr_destination[1]=="U.S.A":
        destinations.pop(destinations.index(("map_part_2","U.S.A")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(527/1980)<=mpl.x<=wn_width*(11/18) and  wn_height*(19/540)<=mpl.y<=wn_height*(119/270) and curr_background==curr_destination[0] and curr_destination[1]=="Canada":
        destinations.pop(destinations.index(("map_part_2","Canada")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(557/1980)<=mpl.x<=wn_width*(907/1980) and  wn_height*(109/180)<=mpl.y<=wn_height*(33/40) and curr_background==curr_destination[0] and curr_destination[1]=="Mexico":
        destinations.pop(destinations.index(("map_part_2","Mexico")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(62/495)<=mpl.x<=wn_width*(79/495) and  wn_height*(41/270)<=mpl.y<=wn_height*(37/180) and curr_background==curr_destination[0] and curr_destination[1]=="Zimbabwe":
        destinations.pop(destinations.index(("map_part_3","Zimbabwe")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(71/330)<=mpl.x<=wn_width*(511/1980) and wn_height*(7/72)<=mpl.y<=wn_height*(139/540) and curr_background==curr_destination[0] and curr_destination[1]=="Madagascar":
        destinations.pop(destinations.index(("map_part_3","Madagascar")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(1163/1980)<=mpl.x<=wn_width*(401/495) and wn_height*(23/270)<=mpl.y<=wn_height*(509/1080) and curr_background==curr_destination[0] and curr_destination[1]=="Australia":
        destinations.pop(destinations.index(("map_part_3","Australia")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(311/495)<=mpl.x<=wn_width*(382/495) and wn_height*(-7/270)<=mpl.y<=wn_height*(13/60) and curr_background==curr_destination[0] and curr_destination[1]=="Brazil":
        destinations.pop(destinations.index(("map_part_4","Brazil")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(361/660)<=mpl.x<=wn_width*(1169/1980) and wn_height*(47/270)<=mpl.y<=wn_height*(125/216) and curr_background==curr_destination[0] and curr_destination[1]=="Chile":
        destinations.pop(destinations.index(("map_part_4","Chile")))
        mpl.add_fuel()
        rand_destination()
        continue

    elif wn_width*(302/495)<=mpl.x<=wn_width*(23/36) and wn_height*(263/1080)<=mpl.y<=wn_height*(61/108) and curr_background==curr_destination[0] and curr_destination[1]=="Argentina":
        destinations.pop(destinations.index(("map_part_4","Argentina")))
        mpl.add_fuel()
        rand_destination()
        continue



    try:
        if mpl.fuel<=0 and curr_background=="map_part_1":
            draw_plane=False
            APEAR_TRY_AGAIN=True
            draw(wn,curr_background,APEAR_TRY_AGAIN)
            sounds.pause_game_playing()
            wn_image,curr_background=pygame.image.load(f"imgs/map_part_1_game_over"+".gif"),f"map_part_1_game_over"
            wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
            wn.blit(wn_image,(0,0))
            images=[(wn_image,(0,0))]
            pygame.display.update()
        elif mpl.fuel<=0 and curr_background=="map_part_2":
            draw_plane=False
            APEAR_TRY_AGAIN=True
            draw(wn,curr_background,APEAR_TRY_AGAIN)
            sounds.pause_game_playing()
            wn_image,curr_background=pygame.image.load(f"imgs/map_part_2_game_over"+".gif"),"map_part_2_game_over"
            wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
            wn.blit(wn_image,(0,0))
            images=[(wn_image,(0,0))]
            pygame.display.update()
        elif mpl.fuel<=0 and curr_background=="map_part_3":
            draw_plane=False
            APEAR_TRY_AGAIN=True
            draw(wn,curr_background,APEAR_TRY_AGAIN)
            sounds.pause_game_playing()
            wn_image,curr_background=pygame.image.load(f"imgs/map_part_3_game_over"+".gif"),"map_part_3_game_over"
            wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
            wn.blit(wn_image,(0,0))
            images=[(wn_image,(0,0))]
            pygame.display.update()
        elif mpl.fuel<=0 and curr_background=="map_part_4":
            draw_plane=False
            APEAR_TRY_AGAIN=True
            draw(wn,curr_background,APEAR_TRY_AGAIN)
            sounds.pause_game_playing()
            wn_image,curr_background=pygame.image.load(f"imgs/map_part_4_game_over"+".gif"),"map_part_4_game_over"
            wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
            wn.blit(wn_image,(0,0))
            images=[(wn_image,(0,0))]
            pygame.display.update()
    except TypeError:
        None



    if len(destinations)==0 and curr_background=="map_part_1":
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load(f"imgs/map_part_1_congratulations"+".png"),"map_part_1_congratulations"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
    elif len(destinations)==0 and curr_background=="map_part_2":
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load(f"imgs/map_part_2_congratulations"+".png"),"map_part_2_congratulations"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
    elif len(destinations)==0 and curr_background=="map_part_3":
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load(f"imgs/map_part_3_congratulations"+".png"),"map_part_3_congratulations"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()
    elif len(destinations)==0 and curr_background=="map_part_4":
        draw_plane=False
        APEAR_TRY_AGAIN=True
        draw(wn,curr_background,APEAR_TRY_AGAIN)
        sounds.pause_game_playing()
        wn_image,curr_background=pygame.image.load(f"imgs/map_part_4_congratulations"+".png"),"map_part_4_congratulations"
        wn_image=pygame.transform.scale(wn_image,(wn_width,wn_height))
        wn.blit(wn_image,(0,0))
        images=[(wn_image,(0,0))]
        pygame.display.update()



    pygame.display.flip()
pygame.quit()
