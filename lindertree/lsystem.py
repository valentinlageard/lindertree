import re

symbol_regex = '([A-Za-z\[\]\+\-\!])+?(\(.*?\))?'
parameter_regex = '([A-Za-z]+[A-Za-z\d\*\+\-\/\s]*|\d+\.*\d*)'

# Symbols

class Symbol:
	def __init__(self, char, parameters=None):
		self.char = char
		self.parameters = parameters

	@staticmethod
	def __param_string_to_parameters(param_string):
		if not param_string:
			return None
		parameters = []
		regexed_param_string = re.findall(parameter_regex, param_string)
		for regexed_param in regexed_param_string:
			try:
				new_param = float(regexed_param)
			except ValueError:
				new_param = regexed_param
			parameters.append(new_param)
		if not parameters:
			return None
		return parameters

	@classmethod
	def from_string(cls, string):
		symbol_param_tuples = re.findall(symbol_regex, string)
		char = symbol_param_tuples[0][0]
		param_string = symbol_param_tuples[0][1]
		parameters = cls.__param_string_to_parameters(param_string)
		return (cls(char, parameters))

	@classmethod
	def from_symbol_param_tuple(cls, symbol_param_tuple):
		char = symbol_param_tuple[0]
		param_string = symbol_param_tuple[1]
		parameters = cls.__param_string_to_parameters(param_string)
		return (cls(char, parameters))

	def __str__(self):
		if self.parameters:
			formatted_parameters = ','.join([str(param) for param in self.parameters])
			return (self.char + '(' + formatted_parameters + ')')
		else:
			return (self.char)

def string_to_symbols(string):
	symbol_param_tuples = re.findall(symbol_regex, string)
	return [Symbol.from_symbol_param_tuple(symbol_param_tuple) for symbol_param_tuple in symbol_param_tuples]

def symbols_to_string(symbols):
	return ''.join([str(symbol) for symbol in symbols])

# Rules

class Rule:
	def __init__(self, predecessor, successor, constants=None):
		self.predecessor = predecessor
		self.successor = successor
		self.constants = constants

	@classmethod
	def from_string(cls, predecessor_string, successor_string, constants=None):
		predecessor = string_to_symbols(predecessor_string)
		successor = string_to_symbols(successor_string)
		return (cls(predecessor, successor, constants))

	def is_predecessor(self, symbol):
		return symbol.char == self.predecessor[0].char

	def __get_locals(self, concrete_predecessor):
		variables = {}
		if (concrete_predecessor.parameters):
			for i, parameter in enumerate(concrete_predecessor.parameters):
				variables[self.predecessor[0].parameters[i]] = parameter
		return {**variables, **self.constants}

	def __compute_symbol_parameters(self, symbol, locals):
		if symbol.parameters is not None:
			new_parameters = []
			for parameter in symbol.parameters:
				if type(parameter) is str:
					new_parameters.append(eval(parameter,{},locals))
				else:
					new_parameters.append(parameter)
			return new_parameters
		else:
			return None

	def __compute_successor(self, concrete_predecessor):
		locals = self.__get_locals(concrete_predecessor)
		computed_successor = []
		for symbol in self.successor:
			computed_successor.append(Symbol(symbol.char, self.__compute_symbol_parameters(symbol, locals)))
		return computed_successor

	def get_successor(self, concrete_predecessor):
		return self.__compute_successor(concrete_predecessor)

	def __str__(self):
		predecessor_string = symbols_to_string(self.predecessor)
		successor_string = symbols_to_string(self.successor)
		return (predecessor_string + ' -> ' + successor_string)

def apply_rules(symbols, rules):
	new_symbols = []
	for symbol in symbols:
		for rule in rules:
			if rule.is_predecessor(symbol):
				new_symbols += rule.get_successor(symbol)
				break
		else:
			new_symbols.append(symbol)
	return new_symbols

def generate_lsystem(iterations, axiom, rules):
	if not type(axiom) is list:
		axiom = [axiom]
	symbols_buffer = apply_rules(axiom, rules)
	for i in range(iterations - 1):
		symbols_buffer = apply_rules(symbols_buffer, rules)
	return symbols_buffer
