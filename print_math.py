import math as m

def golden_ratio():
    print(( 1 + m.sqrt(5)) / 2)

def six_squared():
    print(m.pow(6, 2))

def hypotenuse():
    print(m.sqrt(m.pow(5, 2) + m.pow(12, 2)))

def pi():
    print(m.pi)

def e():
    print(m.e)

def squares_area():
    string = "1"
    for x in range(2, 11):
        string += f" {str(x**2)}"
    print(string)

if __name__ == "__main__" :
    golden_ratio()
    six_squared()
    hypotenuse()
    pi()
    e()
    squares_area()