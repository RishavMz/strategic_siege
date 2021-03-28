# Troops

# Available troops:

## 1. Infantry

### Add new unit

newinfantry = Infantry(canvas, x_position, y_position)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate were the troop is to be deployed
y_position  - The y coordinate where the troop is to be deployed

### Data members (constants) :

health          -   20
attack force    -   2
speed           -   5
attack range    -   50  

## 1. Archer

### Add new unit

newarcher = Archer(canvas, x_position, y_position)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate were the troop is to be deployed
y_position  - The y coordinate where the troop is to be deployed

### Data members (constants) :

health          -   15
attack force    -   0.9
speed           -   8
attack range    -   210 

## 1. Cavalry

### Add new unit

newcavalry = Cavalry(canvas, x_position, y_position)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate were the troop is to be deployed
y_position  - The y coordinate where the troop is to be deployed

### Data members (constants) :

health          -   25
attack force    -   1
speed           -   10
attack range    -   120 

## 1. HeavyCavalry

### Add new unit

newheavycavalry = HeavyCavalry(canvas, x_position, y_position)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate were the troop is to be deployed
y_position  - The y coordinate where the troop is to be deployed

### Data members (constants) :

health          -   50
attack force    -   0.6
speed           -   3
attack range    -   80 
#
## Common Functions:

<p>
damage(force)       -   Takes strength of attack as input and reduces its hitpoints by the input attack strength 
</p>
<p>
getHP()     -   deprecated function
</p>
<p>
draw()              -   Draws a circle representing the cannon and a red healthbar above it whose width is its health(hitpoints)
</p>
<p>
movex(pos)  -   Changes the x coordinate of unit to given position
</p>
<p>
movey(pos)  -   Changes the y coordinate of unit to given position
</p>