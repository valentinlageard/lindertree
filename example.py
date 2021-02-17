from lindertree.lsystem import *
from lindertree.turtle_interprate import *

# We generate our axiom (as a symbol list) by converting a string
axiom = string_to_symbols('X')

# We generate our rules from strings and store them in a rule list
rules = []
rule_growth = Rule.from_string('F', 'FF')
rule_branch = Rule.from_string('X', 'F[+X][-X]FX')
rules.append(rule_growth)
rules.append(rule_branch)

# We print our lsystem specification
print('Axiom : ' + symbols_to_string(axiom))
for i, rule in enumerate(rules):
	print('Rule ' + str(i) + ' : ' + str(rule))

# We generate our symbol list at the 7th iteration from our axiom and rules
symbols = generate_lsystem(7, axiom, rules)

# We turtle interprate our symbol list with some special parameters
turtle_interprate(symbols, distance=2, angle=27.5, init_pos=(0,-300))
