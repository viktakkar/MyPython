"""
Challenge: Write a Python statement that calculates and prints the distance between the points (2, 2)(2,2) and (5, 6)(5,6).
(Hint: Remember that a square root can be computed by raising a value to the 0.50.5 power.)

"""

"""
Solution - Compute the distance between the points (x0, y0) and (x1, y1).
"""

###################################################
# Distance formula
# Student should enter statement on the next line.

x0=2
y0=2
x1=5
y1=6

distance_bw_two_points=(((x0-x1)**2)+((y0-y1)**2))**0.5

print("The distance between two points",distance_bw_two_points)
# Hint: You need to use the power operation ** .


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#5.0

