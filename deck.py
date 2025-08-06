cap = 10
deque = [None] * cap
front = -1
rear = -1

def is_empty():
    return front == -1

def is_full():
    return rear - front + 1 == cap

def insert_front(n):
    global front, rear
    if is_full():
        print("공간 없음")
        return
    if is_empty():
        front = 0
        rear = 0
    elif front > 0:
        front -= 1
    elif rear < cap - 1:
        for i in range(rear, front - 1, -1):
            deque[i + 1] = deque[i]
        rear += 1
    else:
        print("공간 없음(front)")
        return
    deque[front] = n

def insert_rear(n):
    global front, rear
    if is_full():
        print("공간 없음")
        return None
    if is_empty():
        front = 0
        rear = 0
    else:
        rear += 1
    deque[rear] = n

def delete_front():
    global front, rear
    if is_empty():
        print("값 없음")
        return None
    value = deque[front]
    deque[front] = None
    if front == rear:
        front = -1
        rear = -1
    else:
        front += 1
    return value

def delete_rear():
    global front, rear
    if is_empty():
        print("값 없음")
        return None
    value = deque[rear]
    deque[rear] = None
    if front == rear:
        front = -1
        rear = -1
    else:
        rear -= 1
    return value

def print_d():
    if is_empty():
        print("덱 : []")
        return None
    print("덱 :", [deque[i] for i in range(front, rear + 1)])