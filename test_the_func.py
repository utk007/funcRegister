from func_stack import foo

@foo
def bar():
	print "inside bar"
	bar1()

def bar1():
	print "inside bar1"
	bar2()

def bar2():
	print "inside bar2"

bar()
