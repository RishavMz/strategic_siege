import pygame
from data.troops import *
from data.defenses import *
from data.defence_levels import *

import math

WIDTH = 800
HEIGHT = 600
state = 0
level = 0

totalDamageDone = 0
totalDamageTaken = 0

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
        pygame.draw.rect(self.canvas, (255,255,255), (500,90, 300, self.height-90),1)   
        pygame.draw.rect(self.canvas, (255,255,255), (600,30, 90, 30))   


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
   

def assemble():
    for i in levels[level].showcards():
        cards.append(Cards(table1,i[0],i[1],i[2])) 

    for i in levels[level].showdefenses():
        if(i[0]==1):
            army.append(Infantry(table1,i[1],i[2]))
        elif(i[0]==2):
            army.append(Archer(table1,i[1],i[2]))
        elif(i[0]==3):
            army.append(Cavalry(table1,i[1],i[2]))
        elif(i[0]==4):
            army.append(HeavyCavalry(table1,i[1],i[2]))    

    print("Assembled")

table1 = Table(WIDTH, HEIGHT)
Table_name="Battle_Machine"

run = True
army = []
cards = []
defence = []    

assemble()

cardCannonImage = pygame.image.load(    'images/cardcannon.png')
cardTowerImage = pygame.image.load(      'images/cardtower.png')
cardBunkerImage = pygame.image.load(      'images/cardbunker.png')
cannonImage = pygame.image.load(          'images/cannon.png')
towerImage = pygame.image.load(           'images/tower.png')
bunkerImage = pygame.image.load(           'images/bunker.png')
infantryImage = pygame.image.load(        'images/infantry.png')
archerImage = pygame.image.load(          'images/archer.png')
cavalryImage = pygame.image.load(         'images/cavalry.png')
heavycavalryImage = pygame.image.load(    'images/heavycavalry.png')
displaySpace = pygame.display.set_mode((600,700))

def distanceCalc(body1, body2):
    return math.sqrt((body1.posx - body2.posx)**2 + (body1.posy - body2.posy)**2)


play = 0
start = 0
while run:
    table1.draw(Table_name)

    for i in range(len(cards)):
        if(state == (i+1)):
            for j in range(cards[i].number):
                pygame.draw.rect(table1.canvas, (255,255,255), (cards[i].posx + (j*4),75,2, 5))                    

    if(len(army)>0):
        play = 1
    if(play==1 and len(defence)==0 and start ==1):
        print("\nYou Lose\n")
        print("Total damage done : ",totalDamageDone)
        print("Total damage taken: ",totalDamageTaken)  
        print("\n")
        break
     

    fallen = []
    for i in range(len(army)):
        army[i].draw()
        if(army[i].health<=0):
            fallen.append(i)
    for i in fallen:
        army.pop(i)          


    for i in defence:
        i.draw()

    if(start==1):
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
                            totalDamageTaken += i.strength
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
                    totalDamageDone += defence[i].power
        cardsrem = 0
        for i in cards:
            cardsrem += i.number
        if(len(army)==0 and len(defence)>0 and cardsrem >= 0):
            if(level == len(levels)-1):
                run = False
                print("\n You Won\n")
                print("Total damage done : ",totalDamageDone)
                print("Total damage taken: ",totalDamageTaken)  
                print("\n") 
            else:
                level+= 1  
                start = 0
                defence=[]
                cards = []
                assemble()                   


    pygame.time.delay(10)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False 

        if event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            if(pos[1]>=30 and pos[1]<=60 and pos[0]>=600 and pos[0]<=690) :
                if(start==0):
                    start = 1
                    print("Attack started")
            elif(pos[1]<=60):
                for i in cards:
                    i.checkmouse(pos[0])         
            elif(pos[1]>=100 and pos[0]>500):
                if(state==1):     
                    if(cards[0].number>0):   
                        defence.append(Cannon(table1,pos[0],pos[1]))
                        cards[0].number -= 1
                elif(state==2):
                    if(cards[1].number>0):
                        defence.append(Tower(table1,pos[0],pos[1]))
                        cards[1].number -= 1
                elif(state==3):
                    if(cards[2].number>0):
                        defence.append(Bunker(table1,pos[0],pos[1]))
                        cards[2].number -= 1        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                if(state>1):
                    state -= 1
            if event.key == pygame.K_RIGHT:
                if(state<=3):
                    state += 1               


    displaySpace.blit(cardCannonImage,(cards[0].posx,cards[0].posy))
    displaySpace.blit(cardTowerImage,(cards[1].posx,cards[1].posy)) 
    displaySpace.blit(cardBunkerImage,(cards[2].posx,cards[2].posy))     
    
    for i in defence:
        if(i.type=="cannon"):
            displaySpace.blit(cannonImage,(i.posx-22,i.posy-22))
        elif(i.type=="tower"):
            displaySpace.blit(towerImage,(i.posx-15,i.posy-15))    
        elif(i.type=="bunker"):
            displaySpace.blit(bunkerImage,(i.posx-22,i.posy-22))    
    for i in army:
        if(i.type=="infantry"):
            displaySpace.blit(infantryImage,(i.posx-10,i.posy-10))
        elif(i.type=="archer"):
            displaySpace.blit(archerImage,(i.posx-8,i.posy-8))
        elif(i.type=="cavalry"):
            displaySpace.blit(cavalryImage,(i.posx-6,i.posy-6))
        elif(i.type=="heavycavalry"):
            displaySpace.blit(heavycavalryImage,(i.posx-15,i.posy-15))


    pygame.display.update()
pygame.quit()   

