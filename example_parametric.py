from lindertree.lsystem import *
from lindertree.turtle_interprate import *

axiom = string_to_symbols('!(1)F(5)X')
constants = {'w':1.4, 'e':1.6, 'a':1.1}
width_rule = Rule.from_string('!(x)', '!(x*w)', constants)
elongation_rule = Rule.from_string('F(x)', 'F(x*e)', constants)
angle_rule1 = Rule.from_string('+(x)', '+(x*a)', constants)
angle_rule2 = Rule.from_string('-(x)', '-(x*a)', constants)
branching_rule = Rule.from_string('X', '!(1)[+(25)F(2)X]F(2)[-(25)F(2)X]!(1)F(5)X', constants)
rules = [width_rule, elongation_rule, branching_rule, angle_rule1, angle_rule2]

print('Axiom : ' + symbols_to_string(axiom))
print('Rules : ')
for rule in rules:
	print('- ' + str(rule))

symbols = generate_lsystem(8, axiom, rules)
print(symbols_to_string(symbols))
turtle_interprate(symbols, init_pos=(0,-400))
