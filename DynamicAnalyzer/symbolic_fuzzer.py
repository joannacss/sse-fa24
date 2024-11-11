# Code based on the code from the FuzzingBook.org
import inspect
import ast
from examples.twice import test
from examples.triangle import triangle
import z3

def collect_conditions(tree):
	paths = []

	def traverse_if_children(children, context, cond):
		previous_len = len(paths)
		for child in children:
			traverse(child, context + [cond])
		if len(paths) == previous_len:
			paths.append(context + [cond])

	def traverse(node, context):
		# method call, loops, ...
		if isinstance(node, ast.Call):
			# the actual dispatch
			pass
		elif isinstance(node, ast.If):
			cond = ast.unparse(node.test).strip()
			not_cond = f"z3.Not({cond})" #TODO: replace with Z3 syntax
			traverse_if_children(node.body, context, cond)
			traverse_if_children(node.orelse, context, not_cond)
		else:
			for child in ast.iter_child_nodes(node):
				traverse(child, context)

	traverse(tree, [])


	return [ "z3.And(" + ",".join(p) + ")" for p in paths]  #TODO: replace with Z3 syntax


def main():
	function_source = inspect.getsource(test)
	function_ast = ast.parse(function_source)
	paths = collect_conditions(function_ast)

	for i in range(len(paths)):
		print(f"Path {i + 1}", paths[i])
		# TODO: use z3 solver to find inputs that satisfy the path condition
		solver = z3.Solver()
		x = z3.Int('x')
		y = z3.Int('y')
		z = 2 * y #hardcoding the constraint from the function call

		constraint = paths[i]
		status = eval(f"solver.check({constraint})")
		if status == z3.sat:
			m = solver.model()
			print(f"Input: x={m[x]}, y={m[y]}")







if __name__ == '__main__':
	main()
