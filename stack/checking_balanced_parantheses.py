expr = "{()}[]"
stack = []
opening_brackets = "[{("
closing_brackets = ")}]"
mapping_brackets = {')':'(', '}':'{', ']':'['}
stack_len = 0

for char in expr:
	if char in opening_brackets:
		stack.append(char)
		stack_len += 1
	else:
		while True:
			if stack_len == 0:
				print "Brackets dont match."
				exit()
			else:
				temp = stack.pop()
				stack_len -= 1
				if temp == mapping_brackets[char]:
					break
				else:
					continue
if stack_len != 0:
	print "Brackets don't match."
else:
	print "Brackets match."