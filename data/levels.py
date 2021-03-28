class Level:
    def __init__(self,cards,defence):
        self.cards = [[40,1],[100,2],[160,3],[220,4]]
        self.defence = defence
        for i in range(len(cards)):
            self.cards[i].append(cards[i])
    def showcards(self):
        return self.cards
    def showdefenses(self):
        return self.defence            


class Game:
    def __init__(self):
        self.level = 0


cards1 = [8,8,5,5]
defence1 = [[1,550,150],[1,620,300],[1,620,450],[1,550,550]]     
level1 = Level(cards1,defence1)      


cards2 = [6,6,5,3]
defence2 = [[2,600,150],[2,550,300],[2,550,450],[2,600,550]]     
level2 = Level(cards2,defence2)   

cards3 = [8,8,5,2]
defence3 = [[1,550,150],[2,580,300],[2,620,350],[1,520,370],[2,620,400],[2,580,450],[1,550,550]]     
level3 = Level(cards3,defence3)   

cards4 = [6,6,5,2]
defence4 = [[1,550,150],[2,580,300],[2,620,350],[1,520,370],[2,620,400],[2,580,450],[2,620,200],[2,580,500],[1,550,550]]     
level4 = Level(cards4,defence4)  

levels = [level1,level2,level3,level4]