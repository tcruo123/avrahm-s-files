#we eill import the pip library "turtle" if its not working enter to the windows command proamt "pip install turtle"
import turtle
#now let's create the function draw_triangle with no parameters by using python keyword "def"
def draw_triangle():
    #this is loop that will return the code three times:
    for x in range(3):
        #we want to call the function forward of the object turtle and go 45 steps
        turtle.forward(45)
        #now we want turn the turtle 120 right
        turtle.right(120)
#now lets create the function draw_sail:
def draw_sail():
    turtle.left(90)
    turtle.forward(50)
    turtle.right(150)
    draw_triangle()
    turtle.right(30)
    turtle.up()
    turtle.forward(50)
    turtle.down()
    turtle.left(90)

def draw_ship():
    turtle.forward(50)
    for x in range(3):
        draw_sail()
        turtle.forward(50)
    turtle.right(120)
    turtle.forward(20)
    turtle.right(60)
    turtle.forward(180)
    turtle.right(60)
    turtle.forward(20)
    turtle.right(300)
draw_ship()
def draw_fleet():
    turtle.up()
    turtle.forward(300)
    turtle.left(180)
    turtle.down()
    draw_ship()
if __name__ == '__main__' :
   draw_fleet() 
   turtle.done()
