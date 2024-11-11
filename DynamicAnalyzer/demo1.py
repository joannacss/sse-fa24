from examples.triangle import triangle
import sys

def analyze(frame, event, arg):
	# get function code
	function_code = frame.f_code

	# get function name
	function_name = function_code.co_name

	# get line number
	lineno = frame.f_lineno

	# prints them f"{event} --> {function_name}:{lineno}"
	print(f"{event} --> {function_name}:{lineno}")

	# returns the function itself to track the new scope
	return analyze
    
    

def main():
	# start tracing the invocation
	sys.settrace(analyze)
	output = triangle(2, 2, 1)

	# stop tracing the invocation
	sys.settrace(None)


	print("Output at main()", output)
    

if __name__ == '__main__':
	main()