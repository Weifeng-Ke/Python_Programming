import threading
import random, time

def reader(buffer:list,out_index:int):
    '''This is a reader function that is planing to just read'''
    result=buffer[out_index]
    print(f"I am reading: {result}")
    
def writer():
    '''This is a writer function that is planing to just write'''

def consumer():
    '''This is a consumer function that is planing to just consume'''


def producer(buffer:list, index:int):
    '''This is a producer function that is planing to just produce'''
    circular_buffer[index]=random(0,10)

if __name__=="__main__":
    buffer_size=5
    circular_buffer=[]
    pointer_in = 0
    pointer_out = 0
    count=0
    
    p1=threading.Thread(target=reader,args=(circular_buffer,pointer_out),daemon=False)
    p2=threading.Thread(target=reader,args=(circular_buffer,pointer_out),daemon=False)
    p3=threading.Thread(target=reader,args=(circular_buffer,pointer_out),daemon=False)
    
    p4=threading.Thread(target=writer,args=(circular_buffer,pointer_in),daemon=False)
    p5=threading.Thread(target=writer,args=(circular_buffer,pointer_in),daemon=False)
    