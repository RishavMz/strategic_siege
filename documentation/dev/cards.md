# Cards

Contain the list of troops to be deployed

## Add new card:

newcard = Card(canvas,x_position,state,number)

<p>canvas      - The pygame canvas upon which all rendering is to be done
</p><p>x_position  - The starting x coordinate fir this card on card deck
</p><p>state       - Variable which takes the value showing which card is selected
</p><p>number      - The quantity of each troop available
</p>

## Data Members(constants):

<p>y_position = 10
</p><p>height = 60
</p><p>width = 50
</p>

## Methods:

### checkmouse(x_position)
Takes an x coordinate as input and changes the state of selected troop if a particular card is clicked

### draw()
Draws a reactange shape for the card on screen


#
Note:   Images are being rendered seperately for card foreground ( just for UI )

#
#
#

## <div align="right">Made with ❤ by RishavMz</div>