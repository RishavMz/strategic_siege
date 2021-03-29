# Game

#

Table   - Contais the canvas. The screen upon which all rendering is to be done and shown to the user.
<p>
function:<br/> draw(caption)  - Initializes the canvas and draws the game screen
</p>

#

### State variables:

<p>WIDTH    :   Width of the canvas</p>
<p>HEIGHT   :   Height of the canvas</p>
<p>STATE    :   Holds data for the selected card </p>
<p>Level    :   Stores which levels index the  user is currently in. Levels list is in levels.py file</p>
<p>run      :   Loop that keeps game running </p>
<p>army     :   List that stores all deployed(and alive) troops</p>
<p>cards    :   List that contains list of available cards for that level</p>
<p>defence  :   List that stores all the alive defence structures</p>
<p>play     :   0 is battle not yet started. 1 if battle ongoing. When it is 1 and all defences destroye, level incremented.</p>
<p>displaySpace :   Display area to render images</p>


#
### assemble() function
<p>
Takes in data(card details and defence details) from levels.py for each level and adds them to <b>cards</b> and <b>defences</b> list.
</p>

### distanecCalc(a,b) function

Returns euclidian distance between two given sets of points

#

## How the gameplay progresses

<p>
If any troop deployed, <b>play</b> becomes 1. When <b>play</b> is 1 and all defences destroyed ( <b>defence</b> list becomes empty ), <b>cards</b> and <b>army</b> lst also mde empty. Then <b>assemble()</b> function is called which increments <b>level</b> and fills data into <b>cards</b> and <b>defences</b> list .
</p>

<p>
A <b>fallen</b> list is made to collect troops whose health is 0 or negative after each frame. The army units which are iin this list are removed from <b>army</b> list.
</p>

<p>
For each unit in army, its nearest defence structure is calculated using <b>distanceCalc(a,b)</b> function. 
<br/>f the structure lies in range of the unit,  a line is drawn between the unit and its nearest defence structure to signify attack and <b>damage(force)</b> function is called for that defence structure present in <b>defence</b> list. If its health becomes 0 or negative, it is popped from the list. 
<br/>If the structure is beyond the range of unit, the army unit moves towards it appropriately using <b>movex(pos)</b> abd <b>movey(pos)</b> functions on that unit present in <b>army</b> list.
</p>
<p>
If <b>army</b> list is not zero, for each item in <b>defence</b> list, its nearest unit is calculated using <b>attack(army)</b> function. If a troop lies in range, a line is drawn towards the unit to show an attack and the troop unit health is reduced by <b>damage(force)</b> function.
</p>

#
#
#

## <div align="right">Made with ❤ by RishavMz</div>