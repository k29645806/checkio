def digit_stack(commands):
    stack = []
    stack_sum = 0
    for cmd in commands:
        action,number = cmd.split(' ') if ' ' in cmd else (cmd,None)

        if action=="PUSH":
            stack.append(number)
        elif action=="POP":
            try:
                stack_sum += int(stack.pop())
            except IndexError:
                pass
        elif action=="PEEK":
            try:
                stack_sum += int(stack[-1])
            except IndexError:
                pass
    return stack_sum



print digit_stack(["PUSH 3", "POP", "POP", "PUSH 4", "PEEK",
                        "PUSH 9", "PUSH 0", "PEEK", "POP", "PUSH 1", "PEEK"]) == 8, "Example"
print digit_stack(["POP", "POP"]) == 0, "pop, pop, zero"
print digit_stack(["PUSH 9", "PUSH 9", "POP"]) == 9, "Push the button"
print digit_stack([]) == 0, "Nothing"


'''
def digit_stack(commands):
    stack = []
    summ = 0
    for command in commands:
        c = command.split(" ")
        if c[0] == "PUSH":
            stack.append(int(c[1]))
        elif c[0] == "POP":
            summ += stack.pop() if len(stack) > 0 else 0
        elif c[0] == "PEEK":
            summ += stack[len(stack)-1] if len(stack) > 0 else 0
    return summ
'''
