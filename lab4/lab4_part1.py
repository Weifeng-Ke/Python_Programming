#student name: Weifeng Ke
#student number: 18879288

import threading

def sortingWorker(firstHalf: bool) -> None:
    """
       If param firstHalf is True, the method
       takes the first half of the shared list testcase,
       and stores the sorted version of it in the shared 
       variable sortedFirstHalf.
       Otherwise, it takes the second half of the shared list
       testcase, and stores the sorted version of it in 
       the shared variable sortedSecondHalf.
       The sorting is ascending and you can choose any
       sorting algorithm of your choice and code it.
    """
    #creating a temp sub-list
    result:list =[]
    #if the parameter is the first half, we first get it's begin and end index position
    if firstHalf:
        result=testcase[:int(len(testcase)/2)]
    else:
        result=testcase[int(len(testcase)/2):]
    #The sorting algorithm i choose is the bubleSort algrithm
    #Outter loop for each pass
    for i in range(len(result)):
        #inner loop for each pass after each inner loop pass the lagest item will ended up at the last so the next pass only needs to work up the end -1 position
        for j in range(0,len(result)-i-1):
            #if the next current element is larger than the next element, then swap
            if result[j]> result[j+1]:
                #move the smaller element to lower position
                #move the hiher element to current position
                result[j],result[j+1]=result[j+1],result[j]
    #if firsthald is true then the result gets saved into the sorted First half other wise it will be saved into sorted second half
    if firstHalf:
        sortedFirstHalf.extend(result)  #saving result to sorted first half 
    else:
        sortedSecondHalf.extend(result) #saving result to sorted second half
            
def mergingWorker() -> None:
    """ This function uses the two shared variables 
        sortedFirstHalf and sortedSecondHalf, and merges/sorts
        them into a single sorted list that is stored in
        the shared variable sortedFullList.
    """
    i=0 #pointer for sortedFirstHalf
    j=0 #pointer for sortedSecondHalf
    while i < len(sortedFirstHalf) and j < len(sortedSecondHalf):
        #if the element in sortedFirst Half is less than sorted second half
        if sortedFirstHalf[i]<sortedSecondHalf[j]:
            SortedFullList.append(sortedFirstHalf[i]) #here i will append the smaller element to the sorted full list
            i=i+1
        else:
            SortedFullList.append(sortedSecondHalf[j]) #here sorted secondhalf is equal or less than the fisrt sorted half, so i will append the sorted second half element to the sorted full list
            j=j+1
    #this is only a percusionary step, if the list length were miss matched, we will first append the remaining sorted first list to the sorted full list  
    while i<len(sortedFirstHalf):
        SortedFullList.append(sortedFirstHalf[i])
        i=i+1
    #this is only a percusionary step, if the list length were miss matched, we will append the remaining sorted second list to the sorted full list      
    while j<len(sortedSecondHalf):
        SortedFullList.append(sortedSecondHalf[j])
        j=j+1

if __name__ == "__main__":
    #shared variables
    testcase = [8,5,7,7,4,1,3,2]
    sortedFirstHalf: list = []
    sortedSecondHalf: list = []
    SortedFullList: list = []
    
    #to implement the rest of the code below, as specified 
    #assign the task to different threadings
    sort1=threading.Thread(target=sortingWorker, daemon=False, kwargs={"firstHalf": True})
    sort2=threading.Thread(target=sortingWorker, daemon=False, kwargs={"firstHalf": False})
    merge=threading.Thread(target=mergingWorker, daemon=False)
    #Start both sorting sublist threads 
    sort1.start()
    #start the sorted second list thread
    sort2.start() 
    #ensureing both threads are finished before merging them
    sort1.join()
    sort2.join()
    #I want to finish both sorting for the sub list before merging them
    merge.start()
    #i want to be able to finish the merging process before printing out the results
    merge.join()
    #as a simple test, printing the final sorted list
    print("The final sorted list is ", SortedFullList)