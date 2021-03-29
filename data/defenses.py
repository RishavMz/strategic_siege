
import pygame
import math


class Cannon:
    def __init__(self,table,posx,posy):
        self.table = table
        self.power = 0.3
        self.health = 30
        self.posx = posx
        self.posy = posy
        self.rad=15
        self.rangeatt = 200
    def damage(self,force):
        self.health -= force
    def draw(self):
        pygame.draw.circle(self.table.canvas, (192,192,192), (self.posx-self.rad//2, self.posy-self.rad//2), self.rad) 
        pygame.draw.rect(self.table.canvas, (255,0,0), (self.posx-18,self.posy-30, (self.health), 2))     
    def attack(self,troops):
        nearest, nearval = None,100000
        for i in range(len(troops)):
            dist = math.sqrt((self.posx-troops[i].posx)**2 + (self.posy-troops[i].posy)**2 )
            if(dist<= self.rangeatt) and (dist < nearval):
                nearval = dist
                nearest = i
        return nearest   


class Tower:
    def __init__(self,table,posx,posy):
        self.table = table
        self.power = 0.1
        self.health = 20
        self.posx = posx
        self.posy = posy
        self.rad=10
        self.rangeatt = 400
    def damage(self,force):
        self.health -= force
    def draw(self):
        pygame.draw.circle(self.table.canvas, (139,69,19), (self.posx-self.rad//2, self.posy-self.rad//2), self.rad) 
        pygame.draw.rect(self.table.canvas, (255,0,0), (self.posx-15,self.posy-25, (self.health), 2))     
    def attack(self,troops):
        nearest, nearval = None,100000
        for i in range(len(troops)):
            dist = math.sqrt((self.posx-troops[i].posx)**2 + (self.posy-troops[i].posy)**2 )
            if(dist<= self.rangeatt) and (dist < nearval):
                nearval = dist
                nearest = i
        return nearest        

# Author : RishavMz