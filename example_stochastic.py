from lindertree.lsystem import *
from lindertree.turtle_interprate import *

axiom = string_to_symbols('!(1)F(6)X')
constants = {'b':25, 'c':12.5, 'l':5, 'm':3, 'w':1.4, 'e':1.55, 'a':0.95}
width_rule = Rule.from_string('!(x)', '!(x*w)', constants)
elongation_rule = Rule.from_string('F(x)', 'F(x*e)', constants)
angle_rule1 = Rule.from_string('+(x)', '+(x*a)', constants)
angle_rule2 = Rule.from_string('-(x)', '-(x*a)', constants)
branching_rule = StochasticRule.from_string('X', [
	'!(1)+(c*~)[+(b+^*4)F(l+~*l/2)X]-(b+^*4)F(l+~*l/2)!(1)[-(b+^*4)F(m+~*m/2)X]+(c*~)F(m+~*m/2)X',
	'!(1)+(c*~)[-(b+^*4)F(l+~*l/2)X]+(b+^*4)F(l+~*l/2)!(1)[+(b+^*4)F(m+~*m/2)X]+(c*~)F(m+~*m/2)X',
	'!(1)+(c*~)[+(b+^*4)F(l+~*l/2)X]-(b+^*4)F(l+~*l/2)!(1)[+(b+^*4)F(m+~*m/2)X][-(b+^*4)F(m+~*m/2)X]+(c*~)F(m+~*m/2)X',
	'!(1)+(c*~)[-(b+^*4)F(l+~*l/2)X]+(b+^*4)F(l+~*l/2)!(1)[+(b+^*4)F(m+~*m/2)X][-(b+^*4)F(m+~*m/2)X]+(c*~)F(m+~*m/2)X'],
	weights=[0.25, 0.25, 0.25, 0.25], constants=constants)
rules = [width_rule, elongation_rule, branching_rule, angle_rule1, angle_rule2]

print('Axiom : ' + symbols_to_string(axiom))
print('Rules : ')
for rule in rules:
	print('- ' + str(rule))

symbols = generate_lsystem(8, axiom, rules)
#print(symbols_to_string(symbols))
turtle_interprate(symbols, init_pos=(0,-400), print_progress=True)#, distance_dev=(0,0.2,0,1), angle_dev=(0,0.0,0,30))
