import turtle


class lsystem:
    def __init__(self, segment, angle, axiom, rule, turnchars, movechars, iterations):
        self.angle = angle
        self.segment = segment
        self.axiom = axiom
        self.rule = rule

        self.turnchars = turnchars
        self.movechars = movechars
        self.iterations = iterations

    def stringcalc(self):
        """
        This function calculates the the string of instructions and returns a string
        :argument
        self
        :return
        string -- the rewritten lsystem string
        """

        string = self.axiom
        rules = self.rule.split(",")
        keys = [rules[i][0] for i in range(len(rules))]
        for i in range(self.iterations):
            tmpstring = ""
            for k in string:
                # for loop assures that code works with any number of rules
                for j in range(len(rules)):
                    if k == rules[j][0]:
                        tmpstring += rules[j][2:]
                if k not in keys:
                    tmpstring += k
            string = tmpstring
        return string

    def draw(self):
        """
        Draws the fractal encoded by the lsystem intruction string

        :argument
        self
        :return
        None
        """
        turtle.left(90)
        inst = self.stringcalc()
        turtle.tracer(1e3, 0)
        turtle.ht()
        # creates list of move forward and turn chars
        turns = self.turnchars.split(',')
        moves = self.movechars.split(',')
        # statelist saves the states of the turtle
        statelist = []
        for i in inst:
            # this for loop ensures that the code works with any number of move forward chars

            for j in range(len(moves)):
                if i in moves:
                    turtle.forward(self.segment)
            # An if ladder is used and works because no character can correspond to several actions at once
            if i == turns[0]:
                turtle.right(self.angle)
            if i == turns[1]:
                turtle.left(self.angle)
            if i == '[':
                # save turtle state
                statelist.append((turtle.position(), turtle.heading()))
            if i == ']':
                # restore turtle state
                position, heading = statelist.pop()
                turtle.penup()
                turtle.setposition(position)
                turtle.setheading(heading)
                turtle.pendown()
        turtle.update()
        turtle.exitonclick()

# create any instance of the lsystem class below
# Here is an example
# dragon =lsystem(5,90,"FX","X=X+YF+,Y=-FX-Y","-,+","F",12)
# have fun
