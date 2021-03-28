# Cards

Contain the list of troops to be deployed

## Add new card:

newcard = Card(canvas,x_position,state,number)

canvas      - The pygame canvas upon which all rendering is to be done
x_position  - The starting x coordinate fir this card on card deck
state       - Variable which takes the value showing which card is selected
number      - The quantity of each troop available


## Data Members(constants):

y_position = 10
height = 60
width = 50


## Methods:

### checkmouse(x_position)
Takes an x coordinate as input and changes the state of selected troop if a particular card is clicked

### draw()
Draws a reactange shape for the card on screen


#
Note:   Images are being rendered seperately for card foreground ( just for UI )