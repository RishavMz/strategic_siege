import pygame


class Infantry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 20
        self.strength = 0.25
        self.speed = 2.5
        self.table = table
        self.rad = 10
        self.range = 30
        self.type="infantry"
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-15, (self.health), 2))    
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos         





class Archer:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 15
        self.strength = 0.09
        self.speed = 4
        self.table = table
        self.rad = 8
        self.range = 210
        self.type="archer"
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-15, (self.health), 2)) 
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos


class HeavyCavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 100
        self.strength = 0.025
        self.speed = 1.5
        self.table = table
        self.rad = 15
        self.range = 50
        self.type="heavycavalry"
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-20, (self.health), 2)) 
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos


class Cavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 15
        self.strength = 0.15
        self.speed = 5
        self.table = table
        self.rad = 12
        self.range = 90
        self.type="cavalry"
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-18, (self.health), 2))    
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos

# Author : RishavMz