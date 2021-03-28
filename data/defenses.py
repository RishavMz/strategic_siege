import pygame
import math


class Cannon:
    def __init__(self,table,power,posx,posy):
        self.table = table
        self.power = power
        self.health = 20
        self.posx = posx
        self.posy = posy
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-20,self.posy-20, 20 ,20))
        pygame.draw.rect(self.table.canvas, (255,255,255), (self.posx-20,self.posy-25, (self.health), 2))     
     
    def attack(self,troops):
        nearest, nearval = 0,100000
        for i in range(len(troops)):
            dist = math.sqrt((self.posx-troops[i].posx)**2 + (self.posy-troops[i].posy)**2 )
            if(dist < nearval):
                nearval = dist
                nearest = i
        return nearest   