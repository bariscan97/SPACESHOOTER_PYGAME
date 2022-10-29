import pygame
import os
import time
import random

pygame.init()

width,height = 750, 750
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space Shooter Tutorial")


redship = pygame.image.load(os.path.join("assets", "redship.png"))
greenship= pygame.image.load(os.path.join("assets", "greenship.png"))
blueship = pygame.image.load(os.path.join("assets", "blueship.png"))
playerlasers=pygame.image.load(os.path.join("assets","playerlaser.png"))

playership = pygame.image.load(os.path.join("assets", "playership.png"))

BG = pygame.transform.scale(pygame.image.load(os.path.join("assets", "bg.png")), (width, height))
redlaser = pygame.image.load(os.path.join("assets", "redlaser.png"))
greenlaser = pygame.image.load(os.path.join("assets", "greenlaser.png"))
bluelaser = pygame.image.load(os.path.join("assets", "bluelaser.png"))
playerlaser = pygame.image.load(os.path.join("assets", "playerlaser.png"))
run=True
clock=pygame.time.Clock()
FPS=60
gemi=[redship,greenship,blueship]
lazer=[redlaser,greenlaser,bluelaser,redlaser,greenlaser,bluelaser]
gemiler=list()
lazerler=list()
playerlaserlist=list()
skor=0
class enemy:
    
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.vel=1
        self.mask=pygame.mask.from_surface(self.img)

    def draw(self):
        
        window.blit(self.img,(self.x,self.y))
        
class lasers:
    
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.vel=5
        self.mask=pygame.mask.from_surface(self.img)
    def draw(self):
        
        window.blit(self.img,(self.x,self.y))

class player:
    
    def __init__(self,x,y,img):
        self.x=x
        self.y=y
        self.img=img
        self.mask=pygame.mask.from_surface(self.img)
        self.health=1000
    def draw(self):
        
        window.blit(self.img,(self.x,self.y))
        
        pygame.draw.rect(window,(255,114,86),(self.x,self.y+100,100,10))
        pygame.draw.rect(window,(255,0,0),(self.x,self.y+100,self.health/10,10))        
def collision(obj,obj1):
    x=obj1.x-obj.x
    y=obj1.y-obj.y
    return obj.mask.overlap(obj1.mask,(x,y))



player1=player(320,600,playership)

def drawing():
    window.blit(BG,(0,0))
    window.blit(cantablosu2,(520,0))
    window.blit(cantablosu,(3,0))
    for i in gemiler:
        i.draw()
    for i in lazerler:
        i.draw()
    player1.draw()
    for i in playerlaserlist:
        i.draw()
    pygame.display.update()
font=pygame.font.SysFont("comicsans",50)    

jump=0
count=0
while run:
    clock.tick(FPS)
    if count<100:
         count+=1
    if count==100:
         count=0

    if jump<7:
         jump+=1
    if jump==7:
         jump=0
    
    cantablosu=font.render("can:{}".format(int(player1.health/10)),1,(255,255,255))
    cantablosu2=font.render("skor:{}".format(skor),1,(255,255,255))
    




    keys=pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        player1.x-=6
    if keys[pygame.K_RIGHT]:
        player1.x+=6
    if keys[pygame.K_x] and jump==0:
        playerlasers=lasers(player1.x,player1.y,playerlaser)
        playerlaserlist.append(playerlasers)





    if len(gemiler)<4:
        for i in gemi:
            enemy1=enemy(random.randint(0,700),random.randrange(-150,-10),i)
            
            gemiler.append(enemy1)
    if len(gemiler)==6:
        for i in range(len(lazer)):
            lazer1=lasers(gemiler[i].x-15,gemiler[i].y,lazer[i])
            if count==0 and gemiler[i].x>0:
                lazerler.append(lazer1)
            
    
    for i in playerlaserlist:
        i.y-=5
        for j in gemiler:
            if collision(i,j) and i.y>5 and j.y>5:
                j.y=random.randrange(-150,-50)
                skor+=1
                playerlaserlist.remove(i)
    for i in gemiler:
        i.y+=i.vel
        if i.y>750 or collision(player1,i):
            i.y=random.randrange(-150,-50)
            player1.health-=10
            

    for i in lazerler:
        i.y+=i.vel
        if collision(i,player1):
            player1.health-=10
            lazerler.remove(i)
    for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

    if player1.health==0:
        run=False
    drawing()       
    
pygame.quit()
