stack = []

def push(n):
    stack.append(n)

def pop():
    if is_empty():
        print("값 없음")
        return None
    return stack.pop()

def top():
    if is_empty():
        print("값 없음")
        return None
    return stack[-1]

def is_empty():
    return len(stack) == 0

def print_s():
    if is_empty():
        print("스택 : []")
    else:
        print("스택 : ", stack)