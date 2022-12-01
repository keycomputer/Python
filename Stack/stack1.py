##LIFO
## -  



stack = []
top = -1 # None
def push(elem):
    # overflow 
    global top 
    stack.append(elem)
    top = len(stack)-1

def pop():
    global top 
    if len(stack) == 0 :
        print("Stack is empty ") # print("Underflow")
    else:
        print("Deleting ", stack.pop())
        top = len(stack) - 1

def isEmpty():
    if len(stack) == 0:
        return True
    else:
        return False
    
def display():
    if isEmpty():
        print("No data ")
    else:
        for i in stack[::-1]:
            print(i, end="  ")
        print()
        
while True:
    print("1. Push ")
    print("2. Pop ")
    print("3. Display")
    print("4. exit ")
    choice = int(input("Enter yourt choice "))
    if choice == 1:
        elem = int(input("Enter element "))
        push(elem)
    elif choice == 2:
        pop()
    elif choice == 3:
        display()
    elif choice == 4:
        break
    else:
        print('invalid input' )
