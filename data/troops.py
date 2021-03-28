import pygame


class Infantry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 20
        self.strength = 15
        self.speed = 10
        self.table = table
        self.rad = 11
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,0,0), (self.posx, self.posy), self.rad)    
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-15, (self.health), 2))     





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
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-15, (self.health), 2)) 



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
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-20, (self.health), 2)) 



class Cavalry:
    def __init__(self,table,posx,posy):
        self.posx = posx
        self.posy = posy
        self.health = 25
        self.strength = 15
        self.speed = 15
        self.table = table
        self.rad = 12
    def damage(self,force):
        self.health -= force
    def getHP(self):
        return self.health
    def draw(self):
        pygame.draw.circle(self.table.canvas, (255,255,0), (self.posx, self.posy), self.rad)
        pygame.draw.rect(self.table.canvas, (0,128,0), (self.posx-10,self.posy-18, (self.health), 2))    

