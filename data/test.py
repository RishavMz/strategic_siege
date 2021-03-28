import math
def distanceCalc(body1, body2):
    return math.sqrt((body1[0] - body2[0])**2 + (body1[1] - body2[1])**2) 

army = [[0,0],[1,1],[2,2],[3,3]]
defence = [[0,0],[10,10],[2.5,2.4]]

for i in army:
    if(len(defence)>0):
        nearest, distance = None , 100000
        for j in range(len(defence)):
            dist = distanceCalc(i,defence[j])
            print(i,defence[j],dist)