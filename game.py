import pygame
from data.troops import *
from data.defenses import *

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
    def __init__(self,table,posx,state):
        self.table = table
        self.posx = posx
        self.posy = 10
        self.height = 60
        self.width = 50
        self.state = state     
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
cannons = []

cards.append(Cards(table1, 40,1))
cards.append(Cards(table1,100,2))
cards.append(Cards(table1,160,3))
cards.append(Cards(table1,220,4))
cards.append(Cards(table1,550,11))




while run:
    table1.draw(Table_name)
    
    fallen = []
    for i in range(len(army)):
        army[i].draw()
        if(army[i].health<=0):
            fallen.append(i)
    for i in fallen:
        army.pop(i)       

    for i in cards:
        i.draw()    

    for i in cannons:
        i.draw()

    if(len(army)>0):
        for i in range(len(cannons)):    
            damagedata = cannons[i].attack(army)
            pygame.draw.line(table1.canvas,(12,34,56),(cannons[i].posx-10,cannons[i].posy-10),(army[damagedata].posx,army[damagedata].posy)) 
            army[damagedata].damage(cannons[i].power)

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
                    army.append(Infantry(table1,pos[0],pos[1]))
                elif(state==2):
                    army.append(Archer(table1,pos[0],pos[1]))
                elif(state==3):
                    army.append(Cavalry(table1,pos[0],pos[1]))
                elif(state==4):
                    army.append(HeavyCavalry(table1,pos[0],pos[1]))

            elif(pos[1]>=100 and pos[0]>510):
                if(state==11):
                    cannons.append(Cannon(table1,0.5,pos[0],pos[1]))        

    pygame.display.update()
pygame.quit()   