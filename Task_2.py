def create_stack():
    stack=[]
    return stack
def check_empty(stack):
    return len(stack)==0
def push(stack,item):
    stack.append(item)
    print("Pushed item is :",item)
def pop(stack):
    if(check_empty(stack)):
        return "Stack is empty"
    else:
        return stack.pop()    
def sortStack(stack):
    stack.sort()


Stack=create_stack()
push(Stack,str(1))
push(Stack,str(2))
push(Stack,str(8))
push(Stack,str(4))
push(Stack,str(5))
push(Stack,str(34))
print("The stack is :",str(Stack))
pop(Stack)
print("The stack is :",str(Stack))
sortStack(Stack)
print("The stack after sort is :",str(Stack))