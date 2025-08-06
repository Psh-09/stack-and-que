cap = 5
c_q = [None] * cap
front = -1
rear = -1

def is_empty():
    return front == -1

def is_full():
    return (rear + 1) % cap == front

def enqueue(n):
    global front, rear
    if is_full():
        print("공간 없음")
        return None
    if is_empty():
        front = 0
        rear = 0
    else:
        rear = (rear + 1) % cap
    c_q[rear] = n

def dequeue():
    global front, rear
    if is_empty():
        print("값 없음")
        return None
    value = c_q[front]
    c_q[front] = None
    if front == rear:
        front = -1
        rear = -1
    else:
        front = (front + 1) % cap
    return value

def peek():
    if is_empty():
        print("비어있음")
        return None
    return c_q[front]

def print_q():
    if is_empty():
        print("선형 큐 : []")
        return None
    result = []
    i = front
    while True:
        result.append(c_q[i])
        if i == rear:
            break
        i = (i + 1) % cap
    print("선형 큐 : ", result)