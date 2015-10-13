from turtle import *
import random

mouse = Turtle()
mouse.ht()
mouse.pu()
UpKeyPressed = False
c=getcanvas()
CANVAS_WIDTH = c.winfo_width()
CANVAS_HEIGHT = c.winfo_height()

class Rectangle(Turtle):
	def __init__(self,x,y,dx,dy,w,h,color='black'):
		Turtle.__init__(self)
		self.penup()
		self.color("blue",color)
		self.goto(x,y)
		self.dx = dx
		self.dy = dy
		self.w = w
		self.h = h
		self.shape("square")
		self.ht()
	def get_dx(self):
		return self.dx
	def get_dy(self):
		return self.dy
	def get_width(self):
		return self.w
	def get_height(self):
		return self.h
	def set_dx(self,dx):
		self.dx = dx
	def set_dy(self,dy):
		self.dy = dy
	def set_width(self,w):
		self.w = w
	def set_height(self,h):
		self.h = h

def create_rectangle(rectangle):
	getscreen().tracer(0)
	if ('color' in rectangle.keys()):
		r = Rectangle(rectangle['x'],rectangle['y'],rectangle['dx'],rectangle['dy'],rectangle['width'],rectangle['height'],rectangle['color'])
	else:
		r = Rectangle(rectangle['x'],rectangle['y'],rectangle['dx'],rectangle['dy'],rectangle['width'],rectangle['height'])
	return r

def move_rectangle(r):
	x = r.xcor()
	dx = r.get_dx()
	y = r.ycor()
	dy = r.get_dy()
	r.goto(x+dx,y+dy)
	r.begin_fill()
	r.pd()
	r.goto(r.xcor()+r.get_width(),r.ycor())
	r.goto(r.xcor(),r.ycor()+r.get_height())
	r.goto(r.xcor()-r.get_width(),r.ycor())
	r.goto(r.xcor(),r.ycor()-r.get_height())
	r.pu()
	r.end_fill()
	r.color("black")

def move_rectangles(rectangles):
	ht()
	for r in rectangles:
		r.clear()
		move_rectangle(r)
	getscreen().update()

def create_screen(width, height):
	getscreen().screensize(width,height)

def get_screen_width():
	global CANVAS_WIDTH
	return CANVAS_WIDTH/2-10

def get_screen_height():
	global CANVAS_HEIGHT
	return CANVAS_HEIGHT/2-5

def get_x_mouse():
	global mouse
	return mouse.xcor()

def get_y_mouse():
	global mouse
	return mouse.ycor()

def movearound(event):
	global CANVAS_WIDTH
	global CANVAS_HEIGHT
	mouse.goto(event.x-c.winfo_width()/2,c.winfo_height()/2-event.y)
	if(CANVAS_WIDTH != c.winfo_width() or CANVAS_HEIGHT != c.winfo_height()):
		getscreen().screensize(c.winfo_width()/2,c.winfo_height()/2)
		CANVAS_WIDTH = c.winfo_width()
		CANVAS_HEIGHT = c.winfo_height()

def get_user_direction(cell):
	mouse_x = get_x_mouse()
	mouse_y = get_y_mouse()

	user_speed = cell.get_speed()
	distance = ((mouse_x - cell.xcor() )**2 + (mouse_y - cell.ycor())**2)**0.5

	if abs(mouse_x - cell.xcor()) < cell.get_radius():
		xdir = 0
	else:
		xdir = int(user_speed * (mouse_x - cell.xcor()) / distance)

	if abs(mouse_y - cell.ycor()) < cell.get_radius():
		ydir = 0
	else:
		ydir = int(user_speed * (mouse_y - cell.ycor()) / distance)

	return (xdir, ydir)

def get_random_x():
	return random.randint(-get_screen_width(), get_screen_width())
def get_random_y():
	return random.randint(-get_screen_height(), get_screen_height())

def upkeypress(event):
	global UpKeyPressed
	UpKeyPressed=True
	print("UpKeyPressed")

######################################################################
# Custom code goes here


######################################################################

c.bind("<Motion>", movearound)
c.bind("<Up>", upkeypress)
getscreen().listen()