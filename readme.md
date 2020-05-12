In the code there is an l-system class with the following methods and attributes:
-.segment (this is the length of the segment that the turtle draws each time he recieves a straight draw instruction. It is an integer. A recommended value is 1-10)

-.angle (this is the angle the turtle turns whenever he recieves a left or right turn instruction. It is an integer in degrees)

-.axiom (this is the starting string that gets rewritten in each generation. It is a string)

-.rule (this is the rule or rules that dictate how the string gets rewritten with each iteration. To write the rule you must write the character (a single character) that becomes another string of characters in the next iteration followed by an "=". After the "=" write the charcters that the charcter before the equal turns in to. If there are several rules it is important to separate them with a comma.
EX: properly written rule : "F=+F--F+" or with several rules "F=XFF-++F,X=FX"

-.turnchars (these are the characters that turtle uses to turn. this is a string. The most common characters are "+,-". As for the rules it is important to separate the characters with a comma)

-.movechars (these are the characters that turtle uses to move forward. This is a string. The characters are separated by a ",")

-.iterations (This is the integer amount of iterations of the lsystem. This is like the complexity of the fractal. Usable iterations are between 1-16)

-.stringcalc() (This method takes no argument. And calculates the string with the number of iterations, the rule and the axiom)

-.draw() (This method takes no argument and draws the fractal with the python turtle module. This method calls the stringcalc() method)


Any move and turn charcters can be used as long as they are consitent with the charcaters in the movechars and turnchars attributes. 
The save and restore state characters are always "[" and "]"
The coed works with any number of rules and move forward characters

Here are some interesting instances of the lsystem class, you can copy paste into the program
serpienski = lsystem(1,120,"F-G-G","F=F-G+F+G-F,G=GG","-,+","F,G",9)
kochright = lsystem(3.5,90,"FF+FF+FF+FF","F=F+F-F-F+F","-,+","F",4)
levy = lsystem(2,45,"F","F=+F--F+","-,+","F",14)
hexserpienski = lsystem(5,60,"A","A=B-A-B,B=A+B+A","+,-","A,B",7)
dragon =lsystem(0.5,90,"FX","X=X+YF+,Y=-FX-Y","-,+","F",18)
fractalplant = lsystem(1,25,"[X]","X=F+[[X]-X]-F[-FX]+X,F=FF","-,+","F",8)
fractalplant2 = lsystem(4,25,"F","F=FF-[-F+F+F]+[+F-F-F]","-,+","F",5)
fractalplant3 = lsystem(0.5,25.7,"Y","X=X[-FFF][+FFF]FX,Y=YFX[+Y][-Y]","-,+","F",9)
fractalplant4 = lsystem(3,25,"F","F=[+F]F[-F]F","-,+","F",7)
hexagongopser = lsystem(4,60,"A","A=A-B--B+A++AA+B-,B=+A-BB--B-A++A+B","-,+","A,B",5)
board = lsystem(2,90,"F+F+F+F","F=FF+F+F+F+FF","+,-","F",5)
crystal = lsystem(4,90,"F+F+F+F","F=FF+F++F+F","+,-","F",4)


