import pygame


class Infantry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 20
        self.strength = 15
        self.speed = 5
        self.table = table
        self.rad = 11
        self.range = 2
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,0,0), (self.posx, self.posy), self.rad)    
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
        self.strength = 20
        self.speed = 8
        self.table = table
        self.rad = 9
        self.range = 30
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (0,255,0), (self.posx, self.posy), self.rad)    
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-15, (self.health), 2)) 
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos


class HeavyCavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 50
        self.strength = 5
        self.speed = 3
        self.table = table
        self.rad = 15
        self.range = 5
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (0,255,255), (self.posx, self.posy), self.rad)  
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-20, (self.health), 2)) 
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos


class Cavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 25
        self.strength = 15
        self.speed = 10
        self.table = table
        self.rad = 12
        self.range = 10
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,0), (self.posx, self.posy), self.rad)
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-18, (self.health), 2))    
    def movex(self,pos):
        self.posx = pos
    def movey(self,pos):
        self.posy = pos
