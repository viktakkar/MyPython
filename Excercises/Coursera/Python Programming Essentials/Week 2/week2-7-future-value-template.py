"""
Given pp dollars, the future value of this money when compounded yearly at a rate of rr percent interest for yy years is  p (1 + 0.01 r)^yp(1+0.01r)y
(Remember that you don't need to understand how this formula works, only how to translate it into Python.)
Write a Python statement that calculates and prints the value of 10001000 dollars compounded at 77 percent interest for 1010 years
"""
"""
Solution - Compute the future value of a given present value, annual rate, and number of years.
"""

###################################################
# Future value formula
# Student should enter statement on the next line.
p=1000
y=10
r=7

future_value=p*(1+0.01*r)**y

print("the future value of this money =",future_value)


###################################################
# Expected output
# Student should look at the following comments and compare to printed output.

#1967.15135729