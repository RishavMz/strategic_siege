import pygame
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
   


class Infantry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 20
        self.strength = 10
        self.speed = 10
        self.table = table
        self.rad = 11
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,0,0), (self.posx, self.posy), self.rad)    
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-10,self.posy-15, (self.health), 2))     





class Archer:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 15
        self.strength = 20
        self.speed = 12
        self.table = table
        self.rad = 9
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (0,255,0), (self.posx, self.posy), self.rad)    
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-10,self.posy-15, (self.health), 2)) 



class HeavyCavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 50
        self.strength = 5
        self.speed = 8
        self.table = table
        self.rad = 15
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (0,255,255), (self.posx, self.posy), self.rad)  
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-10,self.posy-20, (self.health), 2)) 



class Cavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 18
        self.strength = 16
        self.speed = 15
        self.table = table
        self.rad = 12
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,0), (self.posx, self.posy), self.rad)
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-10,self.posy-18, (self.health), 2))    



class Cannon:
    def __init__(self,table,power,health,posx,posy):
        self.table = table
        self.power = power
        self.posx = posx
        self.posy = posy
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-20,self.posy-20, 20 ,20))     
    def attack(self,troops):
        nearest, nearval = 0,1000
        for i in range(len(troops)):
            dist = math.sqrt((self.posx-troops[i].posx)**2 + (self.posy-troops[i].posy)**2 )
            if(dist < nearval):
                nearval = dist
                nearset = i
        return nearest   



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

cannons.append(Cannon(table1,0.2,50,650,150))
cannons.append(Cannon(table1,0.2,50,650,350))
cannons.append(Cannon(table1,0.2,50,650,550))


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

    pygame.display.update()
pygame.quit()   