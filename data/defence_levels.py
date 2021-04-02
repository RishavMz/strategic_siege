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

cards0=[10,10,10,0]
defence0 = [[1,150,200],[2,300,400],[1,250,210],[2,210,491],[1,350,260],[2,190,460]]  
level0 = Level(cards0,defence0)                 

cards1 = [5,5,2,0]
defence1 = [[1,350,150],[2,220,300],[3,220,450],[4,350,450]]     
level1 = Level(cards1,defence1)      


cards2 = [5,5,2,0]
defence2 = [[1,350,150],[2,220,300],[3,220,450],[4,350,450],[4,300,150],[3,170,300],[2,170,450],[1,300,450]]     
level2 = Level(cards2,defence2)   

cards3 = [8,8,2,0]
defence3 = [[4,400,200],[4,400,400],[3,100,220],[3,100,420],[3,100,180],[3,100,180],[2,150,220],[2,150,420],[2,150,180],[2,150,180]]     
level3 = Level(cards3,defence3)   

cards4 = [6,6,2,0]
defence4 = [[4,400,200],[4,400,400],[3,100,220],[3,100,420],[3,100,180],[3,100,180],[2,150,220],[2,150,420],[2,150,180],[2,150,180],[1,180,220],[1,180,420],[1,180,180],[1,180,180]]     
level4 = Level(cards4,defence4)  

levels = [level0,level1,level2,level3,level4]

