queue=[]
def enqueue():
    element=input("Enter the value to be enqueued in the queue = ")
    index=int(input("Enter the value of index = "))

    queue.insert(index,element) #first select index=0, then increase it by 1 consecutively

    print(queue)

def dequeue():
    if not queue:
        print("Queue is empty")
        
    else:
        e=queue.pop(0) #pop(0) means delete the element at 0th index i.e., first element
        print("removed element:",e)
        print(queue)

while True:
    choice=int(input("enter the number: 1 for enqueue, 2 for dequeue & 3 to quit = "))
    
    if choice==1:
        enqueue()
    elif choice==2:
        dequeue()
    elif choice==3:
        print("The QUEUE operation STOPS, right here & right now")
        break
    else:
        print("Please! Enter the correct operation")

#SECOND - BEST PROCESS (FOR A-LEVEL)

num=[""]*5
front=-1
rear=-1

def enqueue():
    global num,front,rear
    
    if rear==len(num)-1:
        print("QUEUE is full")

    elif front==-1 and rear==-1: #empty queue
        front=front+1 #front=0
        rear=rear+1 #rear=0

        n=int(input("Enter a number = "))
        num[rear]=n
        print(num)

    else:
        n=int(input("Enter a number = "))
        rear=rear+1
        num[rear]=n
        print(num)

enqueue()
enqueue()
enqueue()
enqueue()
enqueue()

def pop():
    global num,front,rear
    
    if front==-1 and rear==-1:
        print("QUEUE is empty")
    
    elif front==rear:
        value=num[front]
        num[rear]=""
        front=-1
        rear=-1
        print(num)

    else:
        value=num[front]
        num[front]=""
        front=front+1
        print(num)

pop()
pop()
