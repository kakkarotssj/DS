expr = "(a+b/c*(d+e)-f)"
priorities = {'^': 3, '*': 2, '/':2, '+':1, '-':1}
stack = []
operators = '+-*/^'
ans = ""

stacklen = 0
for char in expr:
	if char == '(':
		stack.append(char)
		stacklen += 1
	elif char == ')':
		while stack[stacklen-1] != '(':
			ans += stack.pop()
			stacklen -= 1
		stack.pop()
		stacklen -= 1
	elif char in operators:
		if stacklen == 0:
			stack.append(char)
			stacklen += 1
		else:
			while len(stack) > 0 and stack[stacklen-1] in operators and priorities[stack[stacklen-1]] >= priorities[char]:
				ans += stack.pop()
				stacklen -= 1
			stack.append(char)
			stacklen += 1
	else:
		ans += char
ans += ''.join(stack)
print ans