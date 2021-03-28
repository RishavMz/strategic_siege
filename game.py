import pygame
from data.troops import *
from data.defenses import *
import math

pygame.init()
WIDTH = 700
HEIGHT = 600
state = 0


class Table:
    def __init__(self,width,height):
        self.width=width
        self.height=height
        self.canvas = canvas = pygame.display.set_mode((self.width,self.height))
    def draw(self, st):
        self.canvas = pygame.display.set_mode((self.width,self.height))
        pygame.display.set_caption(st)
        self.canvas.fill((0,0,0))
        pygame.draw.rect(self.canvas, (255,255,255), (30,90, self.width - 60, self.height-90),2)     
        pygame.draw.rect(self.canvas, (255,255,255), (500,90, 200, self.height-90),1)   


class Cards:
    def __init__(self,table,posx,state,number):
        self.table = table
        self.posx = posx
        self.posy = 10
        self.height = 60
        self.width = 50
        self.state = state  
        self.number = number   
    def checkmouse(self,posx):
        global state
        if(posx >= self.posx) and (posx <= (self.posx+self.width)):
            state = self.state
    def draw(self):     
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx,self.posy, self.width, self.height))     
   



table1 = Table(WIDTH, HEIGHT)
Table_name="Battle_Machine"

run = True
army = []
cards = []
defence = []

cards.append(Cards(table1, 40,1,10))
cards.append(Cards(table1,100,2,10))
cards.append(Cards(table1,160,3,5))
cards.append(Cards(table1,220,4,2))
infantryImage = pygame.image.load('images/infantry.png')
archerImage = pygame.image.load('images/archer.png')
cavalryImage = pygame.image.load('images/cavalry.png')
heavycavalryImage = pygame.image.load('images/heavycavalry.png')
displaySpace = pygame.display.set_mode((600,700))

cards.append(Cards(table1,530,11,4))
cards.append(Cards(table1,590,12,6))

def distanceCalc(body1, body2):
    return math.sqrt((body1.posx - body2.posx)**2 + (body1.posy - body2.posy)**2)



while run:
    table1.draw(Table_name)
    
    fallen = []
    for i in range(len(army)):
        army[i].draw()
        if(army[i].health<=0):
            fallen.append(i)
    for i in fallen:
        army.pop(i)          

    for i in defence:
        i.draw()

    for i in army:
        if(len(defence)>0):
            nearest , distance = None , 1000000
            for j in range(len(defence)):
                dist = distanceCalc(i,defence[j])
                if(dist<distance):
                    nearest = j
                    distance = dist
            if(nearest is not None):        
                if(abs(i.posx - defence[nearest].posx)<=i.range):
                    if(abs(i.posy - defence[nearest].posy)<=i.range):
                        defence[nearest].damage(i.strength)
                        pygame.draw.line(table1.canvas,(68,85,90),(defence[nearest].posx-10,defence[nearest].posy-10),(i.posx,i.posy)) 
                        if(defence[nearest].health<=0):
                            defence.pop(nearest)
                            break
                elif(i.posx > defence[j].posx):
                    i.movex(i.posx-i.speed)
                elif(i.posx < defence[j].posx):
                    i.movex(i.posx+i.speed)   
                if(abs(i.posy - defence[nearest].posy)<=i.range):
                    pass
                elif(i.posy > defence[j].posy):
                    i.movey(i.posy-i.speed)
                elif(i.posy < defence[j].posy):
                    i.movey(i.posy+i.speed)      

                      
    

    if(len(army)>0):
        for i in range(len(defence)):    
            damagedata = defence[i].attack(army)
            if(damagedata is not None):
                pygame.draw.line(table1.canvas,(195,115,119),(defence[i].posx-10,defence[i].posy-10),(army[damagedata].posx,army[damagedata].posy)) 
                army[damagedata].damage(defence[i].power)
                   

    pygame.time.delay(30)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()

            if(pos[1]<=60):
                for i in cards:
                    i.checkmouse(pos[0])

            elif(pos[1]>=100 and pos[0]<500):
                if(state==1):     
                    if(cards[0].number>0):   
                        army.append(Infantry(table1,pos[0],pos[1]))
                        cards[0].number -= 1
                elif(state==2):
                    if(cards[1].number>0):
                        army.append(Archer(table1,pos[0],pos[1]))
                        cards[1].number -= 1
                elif(state==3):
                    if(cards[2].number>0):
                        army.append(Cavalry(table1,pos[0],pos[1]))
                        cards[2].number -= 1
                elif(state==4):
                    if(cards[3].number>0):
                        army.append(HeavyCavalry(table1,pos[0],pos[1]))
                        cards[3].number -= 1

            elif(pos[1]>=100 and pos[0]>510):
                if(state==11):
                    defence.append(Cannon(table1,pos[0],pos[1]))
                elif(state==12):
                    defence.append(Tower(table1,pos[0],pos[1]))  




    displaySpace.blit(infantryImage,(cards[0].posx,cards[0].posy))
    displaySpace.blit(archerImage,(cards[1].posx,cards[1].posy))     
    displaySpace.blit(cavalryImage,(cards[2].posx,cards[2].posy))
    displaySpace.blit(heavycavalryImage,(cards[3].posx,cards[3].posy))


    pygame.display.update()
pygame.quit()   
