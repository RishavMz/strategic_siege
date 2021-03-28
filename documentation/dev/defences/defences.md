# Defences

## Available defence structures:

## 1. Cannon

### Add new cannon

newcannon = Cannon(canvas, x_position, y_position)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate of the cannon
y_position  - The y coordinate of the cannon 

## Data members (constants):

power           = 0.6
hitpoints       = 150
attack range    = 200 

# Methods:

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

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The x coordinate of the tower
y_position  - The y coordinate of the tower 

## Data members (constants):

power           = 0.2
hitpoints       = 100
attack range    = 400 

# Methods:

<p>
damage(force)       -   Takes strength of attack as input and reduces its hitpoints by the input attack strength
</p>

<p>
draw()              -   Draws a circle representing the cannon and a red healthbar above it whose width is its health(hitpoints)
</p>

<p>
attack(troops)      -   Takes input as a list of army units (of any type Troop). Finds the troop unit whose distance is least from it and returns the unit index from the input list. This function selects which unit is to be attacked by the tower
</p>
