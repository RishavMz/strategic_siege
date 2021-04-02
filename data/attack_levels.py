class Level:
    def __init__(self,cards,defence):
        self.cards = [[50,1],[150,2],[250,3],[350,4]]
        self.defence = defence
        for i in range(len(cards)):
            self.cards[i].append(cards[i])
    def showcards(self):
        return self.cards
    def showdefenses(self):
        return self.defence 

cards0=[10,10,10,10]
defence0 = [[1,550,200],[3,600,350],[2,600,500]]  
level0 = Level(cards0,defence0)                 

cards1 = [8,8,5,3]
defence1 = [[1,550,150],[1,620,300],[1,620,450],[1,550,550]]     
level1 = Level(cards1,defence1)      


cards2 = [6,6,5,2]
defence2 = [[2,600,150],[2,550,300],[2,550,450],[2,600,550]]     
level2 = Level(cards2,defence2)   

cards3 = [8,8,5,1]
defence3 = [[1,550,150],[2,580,300],[2,620,350],[3,520,370],[2,620,400],[2,580,450],[1,550,550]]     
level3 = Level(cards3,defence3)   

cards4 = [6,6,5,1]
defence4 = [[3,550,200],[3,550,400],[2,620,250],[2,620,350],[1,680,150],[1,680,450],[1,680,300],[2,680,320],[2,700,310]]     
level4 = Level(cards4,defence4)  

card5 = [6,6,5,1]
defence5 = [[2,620,150],[2,620,250],[2,620,350],[2,620,450],[2,620,550],[1,550,130],[1,550,180],[1,550,230],[1,550,280],[1,550,330],[1,550,380],[1,550,430],[1,550,480],[1,550,530],[1,550,580]]
level5 = Level(card5,defence5)

levels = [level0,level1,level2,level3,level4,level5]

