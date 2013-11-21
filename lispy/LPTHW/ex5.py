name = 'Paul O. Grant'
age = 23 # not a lie
height = 193 # cm
weight = 86 # kilos
eyes = 'brown'
teeth = 'white'
hair = 'brown'

print "Let's talk about %s." % name
print "He's %d cm tall." % height
print "He's %d kilos heavy." %weight
print "Not bad for a guy that reads all day."
print "His teeth are usually %s depending on the amount coffee." % teeth

# this next line is supposed to be tricky
print "If I add %d, %d, and %d I get %d." % (
    age, height, weight, age + height + weight)