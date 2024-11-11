from examples.triangle import triangle
import sys
import inspect

def analyze(frame, event, arg):
	# get function code
	function_code = frame.f_code

	# get function name
	function_name = function_code.co_name
	source_lines, start = inspect.getsourcelines(function_code)
	# get line number
	lineno = frame.f_lineno
	statement = source_lines[lineno - start].strip()
	variables = []
	for var in frame.f_locals:
		variables.append(f"{var}={frame.f_locals[var]}")

	variables = ",".join(variables)


	# prints them f"{event} --> {function_name}:{lineno}"
	print(f"{event} --> {function_name}:{lineno} {statement} ({variables})")

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