import sys
import turtle
import numpy as np
import random
from . import lsystem

def deviate(value, dev):
	return value * (2 ** np.random.normal(dev[0], dev[1])) + dev[2] + random.uniform(-dev[3], +dev[3])

def turtle_interprate(symbols, distance=5, angle=45, init_pos=(0,0), speed=0, pen_color='white', bg_color='black', mode='instant', print_progress=False, distance_dev=(0,0,0,0), angle_dev=(0,0,0,0)):
	window = turtle.Screen()
	window.bgcolor(bg_color)

	if print_progress:
		symbols_len = len(symbols)
	if mode == 'instant':
		turtle.tracer(0,0)

	turtle.tracer(0,0)
	stack = []

	t = turtle.Turtle()
	t.speed(speed)
	t.setheading(90)
	t.up()
	t.goto(init_pos)
	t.pencolor(pen_color)

	for i, symbol in enumerate(symbols):
		if symbol.char == 'F':
			t.down()
			if (symbol.parameters):
				t.forward(deviate(symbol.parameters[0], distance_dev))
			else:
				t.forward(deviate(distance, distance_dev))
		elif symbol.char == 'T':
			t.down()
			if (symbol.parameters):
				t.pensize(symbol.parameters[1])
				t.forward(deviate(symbol.parameters[0], distance_dev))
			else:
				t.forward(deviate(distance, distance_dev))
		elif symbol.char == 'f':
			t.up()
			if (symbol.parameters):
				t.forward(deviate(symbol.parameters[0], distance_dev))
			else:
				t.forward(deviate(distance, distance_dev))
		elif symbol.char == '+':
			if (symbol.parameters):
				t.left(deviate(symbol.parameters[0], angle_dev))
			else:
				t.left(deviate(angle, angle_dev))
		elif symbol.char == '-':
			if (symbol.parameters):
				t.right(deviate(symbol.parameters[0], angle_dev))
			else:
				t.right(deviate(angle, angle_dev))
		elif symbol.char == '[':
			clone = t.clone()
			clone.hideturtle()
			stack.append(clone)
		elif symbol.char == ']':
			t.hideturtle()
			t = stack.pop()
			t.showturtle()
		elif symbol.char == '!' and symbol.parameters:
			t.pensize(symbol.parameters[0])
		if print_progress:
			sys.stdout.write('\r' + 'Progress : ' + str(round((i/symbols_len)*100)) + '%')

	t.hideturtle()

	while True:
		if mode == 'instant':
			turtle.update()
