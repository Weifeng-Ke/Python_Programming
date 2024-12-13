class Stack:
    def __init__(self):
        """ initializes an empty stack and sets it size
            data fields: 
                stack: a python list as the internal data structure
                size: a counter to keep track of the size of the stack 
        """
        self.list = []    #Initialize the list with empty stack
        self.size = 0 #initialize the size to be 0
    def push(self, item):
        """ puts the item on top of the stack and adjusts the stack size"""
        self.list.append(item)
        self.size=self.size+1
    def pop(self):
        """ removes and returns the item on top of the stack
            also adjusts the stack size accordingly
            if the stack is empty, an Exception should be raise
        """
        if self.size == 0:
            raise Exception("Stack is empty")
        else:
            top=self.list[-1]
            self.list[:]=self.list[:-1]
            self.size=self.size-1
            return(top)
    def peek(self):
        """ returns the item on top of the stack without affecting it
            if the stack is empty, returns None
        """
        if self.size == 0:
            return None
        else:
            return(self.list[-1])
    def getSize(self):
        """ returns the size of the stack"""
        return(self.size)
    
if __name__=="__main__":
    #Testing: 
    #   instantiate a stack object
    st=Stack()
    #   call push to push 1
    st.push(1)
    #   call push to push "one"
    st.push('one')
    #   call peek and print the returned item
    result=st.peek()
    print(f"This is the result of peek: '{result}'")
    #   call pop and print the returned item
    result_pop=st.pop()
    print(f"This is the result of pop: '{result_pop}'")
    #   call getSize and print the returned value
    size=st.getSize()
    print(f"This is the size of the stack {size}")
    print(f"This is the result of pop: '{st.pop()}'")