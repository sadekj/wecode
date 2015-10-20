import wecode
running = True
score = 0
rectangle1 = {'x':200, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle2 = {'x':200, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle3 = {'x':400, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle4 = {'x':400, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle5 = {'x':600, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle6 = {'x':600, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle7 = {'x':800, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle8 = {'x':800, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle9 = {'x':1000, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle10 = {'x':1000, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle11 = {'x':1200, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle12 = {'x':1200, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

rectangle13 = {'x':1400, 'y':wecode.get_screen_height(), 'width':12, 'height':214, 'dx': -8, 'dy':0 ,'color':'red'}
rectangle14 = {'x':1400, 'y':-300, 'width':12, 'height':214, 'dx': -8, 'dy':0}

user_rect = {'x':-100, 'y':0, 'width':12, 'height':24, 'dx': 0, 'dy':0}

rectangles = []

rectangle = wecode.create_rectangle(rectangle1)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle2)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle3)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle4)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle5)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle6)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle7)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle8)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle9)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle10)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle11)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle12)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle13)
rectangles.append(rectangle)

rectangle = wecode.create_rectangle(rectangle14)
rectangles.append(rectangle)

user_rect = wecode.create_rectangle(user_rect)
rectangles.append(user_rect)

wecode.pd()
wecode.goto(-wecode.get_screen_width(),0)
wecode.goto(wecode.get_screen_width(),0)

def check_walls(rectangles):
	global score
	for r in rectangles:
		if (r.xcor() <= - wecode.get_screen_width()):
			random_y = wecode.get_random_y()
			if (r.ycor() + r.get_height() < 0 and random_y + r.get_height() < 0):
				r.goto(r.xcor(),random_y)

			random_y = wecode.get_random_y()
			if (r.ycor() > 0 and random_y > 0):
				r.goto(r.xcor(),random_y)

			r.goto(wecode.get_screen_width(),r.ycor())
			r.color("black")
			score +=1

def move_user_rect(user_rect):
	user_rect.set_dy(3)
	wecode.UpKeyPressed = False

def rects_collide(rect1, rect2):
	if (rect1.xcor() < rect2.xcor() + rect2.get_width() and rect1.xcor() + rect1.get_width() > rect2.xcor() and rect1.ycor() < rect2.ycor() + rect2.get_height() and rect1.get_height() + rect1.ycor() > rect2.ycor()):
		return True
	return False

def rects_collision(rectangles,user_rect):
	global running, score
	for rect1 in rectangles:
		if (rect1 != user_rect and rects_collide(rect1,user_rect)):
			rect1.color("red")
			score -=1
			#print ("you lost")
			#running = False

while(running):
	check_walls(rectangles)
	rects_collision(rectangles, user_rect)
	user_rect.set_dy(user_rect.get_dy()-0.1)
	if (wecode.UpKeyPressed):
		move_user_rect(user_rect)
	wecode.move_rectangles(rectangles)
	print(score)

wecode.mainloop()