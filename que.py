q = []

def enqueue(n):
    q.append(n)

def dequeue():
    if is_empty():
        print("비어있음")
        return None
    return q.pop(0)

def front():
    if is_empty():
        print("비어있음")
        return None
    return q[0]

def is_empty():
    return len(q) == 0

def print_q():
    print("큐 :", q)