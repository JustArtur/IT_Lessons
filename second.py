import re
stack = []
file = open("test.html")
iterations = 0

for row in file:
    iterations += 1
    stack = stack + re.findall(r'<[^/]{,5}>', row)
    closed_tags = re.findall(r'</[^..]{,5}>', row)

    if len(closed_tags) != 0:
        for tag in closed_tags:
            tag = tag[:1] + tag[2:]
            if tag == stack[len(stack) - 1]:
                stack.pop(len(stack) - 1)
            else:
                raise Exception(f'Invalid tag')









