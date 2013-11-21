def add(a, b):
    print "ADDING %d and %d" % (a, b)
    return a + b
    
def subtract(a, b):
    print "SUBTRACTING %d and %d" % (a, b)
    return a - b
    
def multiply(a, b):
    print "MULTIPLYING %d and %d" % (a, b)
    return a * b
    
def divide(a, b):
    print "DIVIDING %d and %d" % (a, b)
    return a / b

print "Let's do some math with just functions"

age = add(20, 3)
height = subtract( 200, 83)
weight = multiply( 90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

# for a little extra karma, mr. chameleon

print "Enjoy the karma"

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"
print "though the better question is why would you want to."