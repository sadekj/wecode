from turtle import *
import random

mouse = Turtle() # this line is making a turlte object that later will follow the mouse
mouse.hideturtle() # this line to hide the mouse turtle
mouse.penup() # this line tells mouse turtle to pen up so it will not draw line when the mouse move
UpKeyPressed = False # this variable will be set to True when the up arrow is pressed
canvas=getcanvas() # the canvas is the area that the turtle is moving (the white background)
CANVAS_WIDTH = canvas.winfo_width() # here we get canvas(screen) width
CANVAS_HEIGHT = canvas.winfo_height() # here we get the canvas(screen) height

## This is called a class we gave it the name Rectangle, this class inherit a turtle
## Class properties are self.dx, self.dy, self.width self.height
class Rectangle(Turtle):
	# here is inside the class and the first thing we notice is __init__ function
	# this function is called everytime we create a new rectangle object
	def __init__(self,x,y,dx,dy,width,height,color='black'):
		Turtle.__init__(self)
		self.penup()
		self.color(color)
		self.goto(x,y)
		self.dx = dx # the change in x (speed in x)
		self.dy = dy # the change in y (speed in y)
		self.width = width # the width of the rectangle
		self.height = height # the height of the rectangle
		self.shape("square")
		self.hideturtle()
	# here ends the __init__ function
	# here starts the rest of the functions, these functions are only used for Rectangle variables
	#get the change in x (speed in x)
	def get_dx(self):
		return self.dx
	
	#get the change in y (speed in y)
	def get_dy(self):
		return self.dy
	
	#get the width of the rectangle
	def get_width(self):
		return self.width

	#get teh height of the rectangle
	def get_height(self):
		return self.height
	
	# this function changes the dx (speed in x)
	def set_dx(self,new_dx):
		self.dx = new_dx
	
	# this function changes the dy (speed in y)
	def set_dy(self,new_dy):
		self.dy = new_dy
	
	# this function changes the width of the rectangle
	def set_width(self,new_width):
		self.width = width
	
	#this function changes the height of the rectangle
	def set_height(self,new_height):
		self.height = new_height
## here ends the class Rectangle
## and starts the defintion of normal functions

# this function takes a dictionary filled in with a rectangle's information
# and makes an object using the class we defined above,
# and returns a rectangle object with the dictionaries information
def create_rectangle(rectangle): 
	getscreen().tracer(0)
	if ('color' in rectangle.keys()):
		r = Rectangle(rectangle['x'],rectangle['y'],rectangle['dx'],rectangle['dy'],rectangle['width'],rectangle['height'],rectangle['color'])
	else:
		r = Rectangle(rectangle['x'],rectangle['y'],rectangle['dx'],rectangle['dy'],rectangle['width'],rectangle['height'])
	return r

# this function takes a rectangle object and draws it on the screen
def move_rectangle(rectangle):
	x = rectangle.xcor()
	dx = rectangle.get_dx()
	y = rectangle.ycor()
	dy = rectangle.get_dy()
	rectangle.goto(x+dx,y+dy)
	rectangle.begin_fill()
	rectangle.pendown()
	rectangle.goto(rectangle.xcor()+rectangle.get_width(),rectangle.ycor())
	rectangle.goto(rectangle.xcor(),rectangle.ycor()+rectangle.get_height())
	rectangle.goto(rectangle.xcor()-rectangle.get_width(),rectangle.ycor())
	rectangle.goto(rectangle.xcor(),rectangle.ycor()-rectangle.get_height())
	rectangle.penup()
	rectangle.end_fill()

# this function takes a list of rectangles and draws them on the screen
def move_rectangles(rectangles):
	hideturtle()
	for rectangle in rectangles:
		rectangle.clear()
		move_rectangle(rectangle)
	getscreen().update()

# This function returns the width of the screen
def get_screen_width():
	global CANVAS_WIDTH
	return CANVAS_WIDTH/2-10

# This function returns the height of the screen
def get_screen_height():
	global CANVAS_HEIGHT
	return CANVAS_HEIGHT/2-5

# This function returns the x location of the mouse on the screen
def get_x_mouse():
	global mouse
	return mouse.xcor()

# This function returns the y location of the mouse on the screen
def get_y_mouse():
	global mouse
	return mouse.ycor()

# this functio is called evertime the mouse moves on the screen
# and makes the mouse turtle goes and follows the mouse
# and updates the screen size if the screen size changed
def movearound(event):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	mouse.goto(event.x-canvas.winfo_width()/2,canvas.winfo_height()/2-event.y)
	if(CANVAS_WIDTH != canvas.winfo_width() or CANVAS_HEIGHT != canvas.winfo_height()):
		getscreen().screensize(canvas.winfo_width()/2,canvas.winfo_height()/2)
		CANVAS_WIDTH = canvas.winfo_width()
		CANVAS_HEIGHT = canvas.winfo_height()

# returns a random x on the screen
def get_random_x():
	return random.randint(-get_screen_width(), get_screen_width())

# return a random y on the screen
def get_random_y():
	return random.randint(-get_screen_height(), get_screen_height())

# this function is called eveytime the up arrow on the keybaord is pressed
def upkeypress(event):
	global UpKeyPressed
	UpKeyPressed=True

######################################################################
# Custom code goes here


######################################################################

canvas.bind("<Motion>", movearound) # this line tells turtle to call the function movearound (we defined above) everytime the mouse moves
canvas.bind("<Up>", upkeypress) # this line tells turtle to call the function upkeypress (we defined above) everytime Up arrow is pressed
getscreen().listen() # this line tells the screen in turtle to listen to the keyboard and the mouse, because we are using them