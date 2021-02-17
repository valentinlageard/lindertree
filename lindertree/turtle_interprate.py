import turtle
from . import lsystem

def turtle_interprate(symbols, distance=5, angle=45, init_pos=(0,0), speed=0, pen_color='white', bg_color='black'):
	window = turtle.Screen()
	window.bgcolor(bg_color)

	stack = []

	t = turtle.Turtle()
	t.speed(speed)
	t.setheading(90)
	t.up()
	t.goto(init_pos)
	t.pencolor(pen_color)

	for symbol in symbols:
		if symbol.char == 'F':
			t.down()
			t.forward(distance)
		elif symbol.char == 'f':
			t.up()
			t.forward(distance)
		elif symbol.char == '+':
			t.left(angle)
		elif symbol.char == '-':
			t.right(angle)
		elif symbol.char == '[':
			clone = t.clone()
			clone.hideturtle()
			stack.append(clone)
		elif symbol.char == ']':
			t.hideturtle()
			t = stack.pop()
			t.showturtle()
	t.hideturtle()

	while True:
		pass
