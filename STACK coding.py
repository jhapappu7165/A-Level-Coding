stack = []

def push():
    element = input("Enter the value to be pushed into the stack = ")
    stack.append(element)
    print(stack)

def pop_element():
    if not stack:
        print("stack is empty")

    else:
        e = stack.pop()
        print("removed element:", e)
        print(stack)

while True:
    choice = int(input("enter the operation number: 1 for push, 2 for pop, 3 to quit = "))

    if choice == 1:
        push()
    elif choice == 2:
        pop_element()
    elif choice == 3:
        print("The STACK operation STOPS, right here & right now")
        break
    else:
        print("Please! Enter the correct operation")











# SECOND PROCESS - BEST FOR A-LEVEL

stack=[0]*5
top = -1

def push():
    global stack,top

    if top == len(stack) - 1:
        print("stack is full")
    else:
        num = int(input("Enter the number to be pushed = "))
        top = top + 1
        stack[top] = num
        print(stack)
push()
push()
push()
push()
push()
push()

def pop():
    global stack,top
    if top==-1:
        print("stack is empty")

    else:
        value=stack[top]
        stack[top]=""
        top=top-1
        print(stack)
pop()
pop()
