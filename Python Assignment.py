s = input()
 
index = dict()
for i, c in enumerate(s):
    index[c] = i
stack = []
for i, c in enumerate(s):
    if c in stack:
        continue
    while stack and c < stack[-1] and index[stack[-1]] > i:
        stack.pop()
    stack.append(c)
print(len(stack))

