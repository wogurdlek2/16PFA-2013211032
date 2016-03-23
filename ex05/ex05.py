name = 'Lee Jae Hyuk'
age = 23 # not a lie
height = 172 #inches
my_height_inch = height / (2.54)
weight = 70 # lbs
my_weight_pound = weight / (0.43)
eyes = "Brown"
teeth = "White"
hair = "Black"

print "Let's talk about %s." % name
print "He's %d inches tall." % my_height_inch
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is trixky, try to get it exactly right
print "If I add %s, %d, and %d I get %d." % (age, height, weight, age + height + weight)