#student name: Weifeng Ke
#student number: 18879288

import threading
import random #is used to cause some randomness 
import time   #is used to cause some delay in item production/consumption

class circularBuffer: 
    """ 
        This class implement a barebone circular buffer.
        Use as is.
    """
    def __init__ (self, size: int):
        """ 
            The size of the buffer is set by the initializer 
            and remains fixed.
        """
        self._buffer = [0] * size   #initilize a list of length size
                                    #all zeroed (initial value doesn't matter)
        self._in_index = 0   #the in reference point
        self._out_index = 0  #the out reference point

    def insert(self, item: int):
        """ 
            Inserts the item in the buffer.
            The safeguard to make sure the item can be inserted
            is done externally.
        """
        self._buffer[self._in_index] = item
        self._in_index = (self._in_index + 1) % SIZE

    def remove(self) -> int:
        """ 
            Removes an item from the buffer and returns it.
            The safeguard to make sure an item can be removed
            is done externally.
        """
        item = self._buffer[self._out_index]
        self._out_index = (self._out_index + 1) % SIZE
        return item

def producer() -> None:
    """
        Implement the producer function to be used by the producer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeProduced() -> int: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        return random.randint(1, 99)  #an item is produced

    for _ in range(SIZE * 2): #we just produce twice the buffer size for testing
        item = waitForItemToBeProduced()  #wait for an item to be produced
        print(f"DEBUG: {item} produced")
        #complete the function below here to correctly store the item in the circular buffer
        #acquire empty lock so empty pointer decrement by 1
        empty.acquire()
        #acqure the mutex lock so we can do buffer insert
        mutex.acquire()
        #insert the item to buffer
        circularBuffer.insert(buffer,item=item)
        #release the mutex lock since the insert is finished
        mutex.release()
        #increment the full pointer by 1 becasue we just wrote one to the buffer
        full.release() 

def consumer() -> None:
    """
        Implement the consumer function to be used by the consumer thread.
        It must correctly use full, empty and mutex.
    """
    def waitForItemToBeConsumed(item) -> None: #inner function; use as is
        time.sleep(round(random.uniform(.1, .3), 2)) #a random delay (100 to 300 ms)
        #to simulate consumption, item is thrown away here by just ignoring it
        
    for _ in range(SIZE * 2): #we just consume twice the buffer size for testing
        #write the code below to correctly remove an item from the circular buffer
        #acquire the full lock and decrement the pointer by 1
        full.acquire()
        #acqure the mutex lock so we can munipulate the buffer
        mutex.acquire()
        #remove the last element from the buffer
        item=circularBuffer.remove(buffer)
        #release the mutex lock
        mutex.release()
        #relase teh empty lock and increment the empty pointer by 1
        empty.release()
        
        #end of your implementation for this function
        #use the following code as is
        waitForItemToBeConsumed(item)  #wait for the item to be consumed
        print(f"DEBUG: {item} consumed")

if __name__ == "__main__":
    SIZE = 5  #buffer size
    buffer = circularBuffer(SIZE)  #initialize the buffer

    full = threading.Semaphore(0)         #full semaphore: number of full buffers
                                          #initial value set to 0
    empty = threading.Semaphore(SIZE)     #empty semaphore: number of empty buffers
                                          #initial value set to SIZE
    mutex = threading.Lock()  #lock for protecting data on insertion or removal

    #complete the producer-consumer thread creation below
    #set the thread to producer
    p=threading.Thread(target=producer,daemon=False)
    #set the thread to consumer
    c=threading.Thread(target=consumer,daemon=False)
    #start the threads for producer and consumer
    p.start()
    c.start()
    #blocking the main thread until the producer and the consumer are finished.
    p.join()
    c.join()
    
    
    