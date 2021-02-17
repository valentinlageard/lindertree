# Symbols

class Symbol:
	def __init__(self, char, parameters=None):
		self.char = char
		self.parameters = parameters

	def __str__(self):
		if self.parameters:
			return (self.char + '(' + ','.join(parameters) + ')')
		else:
			return (self.char)

def string_to_symbols(string):
	return [Symbol(char) for char in string]

def symbols_to_string(symbols):
	return ''.join([str(symbol) for symbol in symbols])

# Rules

class Rule:
	def __init__(self, predecessor, successor):
		self.predecessor = predecessor
		self.successor = successor

	@classmethod
	def from_string(cls, predecessor_string, successor_string):
		predecessor = string_to_symbols(predecessor_string)
		successor = string_to_symbols(successor_string)
		return (cls(predecessor, successor))

	def is_predecessor(self, symbol):
		return symbol.char == self.predecessor[0].char

	def get_successor(self):
		return self.successor

	def __str__(self):
		predecessor_string = symbols_to_string(self.predecessor)
		successor_string = symbols_to_string(self.successor)
		return (predecessor_string + ' -> ' + successor_string)

def apply_rules(symbols, rules):
	new_symbols = []
	for symbol in symbols:
		for rule in rules:
			if rule.is_predecessor(symbol):
				new_symbols += rule.get_successor()
				break
		else:
			new_symbols.append(symbol)
	return new_symbols

def generate_lsystem(iterations, axiom, rules):
	symbols_buffer = apply_rules(axiom, rules)
	for i in range(iterations - 1):
		symbols_buffer = apply_rules(symbols_buffer, rules)
	return symbols_buffer
