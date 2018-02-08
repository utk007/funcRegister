global_func_reg = {}

def foo(func_to_track):
	def inside_func():
		print func_to_track.__code__.co_names
		global_func_reg[func_to_track.__name__] = []
		for aobj in func_to_track.__code__.co_names:
			if hasattr(aobj, '__callable__'):
				global_func_register[func_to_track].append(obj)
		print "func name=", func_to_track.__name__
		if global_func_reg[func_to_track.__name__]:
			print global_func_reg[func_to_track.__name__]
	return inside_func
