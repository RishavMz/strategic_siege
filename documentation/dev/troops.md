# Troops


## 1. Infantry

### Add new unit

newinfantry = Infantry(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate were the troop is to be deployed
</p><p>y_position  - The y coordinate where the troop is to be deployed
</p>

### Data members (constants) :

<p>health          -   20
</p><p>attack force    -   0.4
</p><p>speed           -   2.5
</p><p>attack range    -   50  
</p>


## 2. Archer

### Add new unit

newarcher = Archer(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate were the troop is to be deployed
</p><p>y_position  - The y coordinate where the troop is to be deployed
</p>

### Data members (constants) :

<p>health          -   15
</p><p>attack force    -   0.18
</p><p>speed           -   4
</p><p>attack range    -   210 
</p>

## 3. Cavalry

### Add new unit

newcavalry = Cavalry(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate were the troop is to be deployed
</p><p>y_position  - The y coordinate where the troop is to be deployed
</p>

### Data members (constants) :

<p>health          -   25
</p><p>attack force    -   0.3
</p><p>speed           -   5
</p><p>attack range    -   120 
</p>

## 4. HeavyCavalry

### Add new unit

newheavycavalry = HeavyCavalry(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate were the troop is to be deployed
</p><p>y_position  - The y coordinate where the troop is to be deployed
</p>

### Data members (constants) :

<p>
</p><p>health          -   100
</p><p>attack force    -   0.05
</p><p>speed           -   1.5
</p><p>attack range    -   80 
</p>

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

#
#
#

## <div align="right">Made with ❤ by RishavMz</div>