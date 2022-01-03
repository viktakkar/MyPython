def smaller_root(a,b,c):
    var_discriminant=(b**2)-4*a*c

    if var_discriminant<0 or a==0:
        print("Error: No real solutions")
    else:
        discriminant_sqrt=var_discriminant**0.5
        if a>0:
            smaller = -discriminant_sqrt
        else:
            smaller = discriminant_sqrt
        return (-b + smaller) / (2 * a)


###################################################
# Tests
# Student should not change this code.

coeff_a, coeff_b, coeff_c = 1, 2, 3
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))

coeff_a, coeff_b, coeff_c = 2, 0, -10
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


coeff_a, coeff_b, coeff_c = 6, -3, 5
print("The smaller root of " + str(coeff_a) + "x^2 + " + str(coeff_b) +
      "x + " + str(coeff_c) + " is: ")
print(str(smaller_root(coeff_a, coeff_b, coeff_c)))


###################################################
