
def are_pair(open, close):
    if (open == '(' and close == ')'):
        return True
    elif (open == '{' and close == '}'):
        return True
    elif (open == '[' and close == ']'):
        return True
    return False

def are_balanced(exp):
    stack = []
    for i in exp:
        if (i =='(' or i == '[' or i == '{'):
            stack.append(i)
        elif (i ==')' or i == ']' or i == '}'):
            if (len(stack) == 0 or not are_pair(stack[-1], i)):
                return False
            else:
                # .pop() remove the last elem in array [only takes index]
                stack.pop()
    return len(stack) == 0


expression = input("Supply an Expression> ")
if are_balanced(expression):
    print("Balanced")
else:
    print("Are not Balanced")