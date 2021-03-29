# Defences

## Available defence structures:

## 1. Cannon

### Add new cannon

newcannon = Cannon(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate of the cannon
</p><p>y_position  - The y coordinate of the cannon 
</p>

## Data members (constants):

<p>power               = 0.15
</p><p>hitpoints       = 30
</p><p>attack range    = 200 

</p>

## Methods:

<p>
damage(force)       -   Takes strength of attack as input and reduces its hitpoints by the input attack strength
</p>

<p>
draw()              -   Draws a circle representing the cannon and a red healthbar above it whose width is its health(hitpoints)
</p>

<p>
attack(troops)      -   Takes input as a list of army units (of any type Troop). Finds the troop unit whose distance is least from it and returns the unit index from the input list. This function selects which unit is to be attacked by the cannon
</p>

## 2. Tower

### Add new tower

newtower = Tower(canvas, x_position, y_position)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The x coordinate of the tower
</p><p>y_position  - The y coordinate of the tower 
</p>

## Data members (constants):

<p>power                = 0.05
</p><p>hitpoints       = 20
</p><p>attack range    = 400 
</p>

## Methods:

<p>
damage(force)       -   Takes strength of attack as input and reduces its hitpoints by the input attack strength
</p>

<p>
draw()              -   Draws a circle representing the cannon and a red healthbar above it whose width is its health(hitpoints)
</p>

<p>
attack(troops)      -   Takes input as a list of army units (of any type Troop). Finds the troop unit whose distance is least from it and returns the unit index from the input list. This function selects which unit is to be attacked by the tower
</p>

#
#
#

## <div align="right">Made with ❤ by RishavMz</div>