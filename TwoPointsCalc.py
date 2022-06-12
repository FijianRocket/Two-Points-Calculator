""" A simple calculator that find different information and applies formulas on two points """

def twoPointsCalc(x1,y1,x2,y2):
    m = (y2-y1)/(x2-x1)
    b = (m*(-x2))+y2
    r = (y2/y1)**(1/(x2-x1))

    print("\n---------------------------------------------------------------------------\n")

    print("Point-Slope Form: " + "y" + "-" + str(y2) + " = " + str(m) + "(x-" + str(x2) + ")")
    print("Slope-Intercept Form: " + "y = " + str(m) + "x" + str(b))
    print("Geometric Form: " + str(y1) + "(" + str(r) + ")^(x-" + str(x1)+")")

    print("")

    print("Range: " + "{" + str(y1) + " < y < " + str(y2) + "}")
    print("Domain: " + "{" + str(min(x1,x2)) + " < x < " + str(max(x1,x2)) + "}")

    print("\n---------------------------------------------------------------------------\n")

twoPointsCalc(
    float(input("X1: ")),
    float(input("Y1: ")),
    float(input("X2: ")),
    float(input("Y2: "))
    )
