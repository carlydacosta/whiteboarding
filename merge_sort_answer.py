def mergeSort(alist):
    print("Splitting ",alist)
    
    if len(alist)>1:            #if length of the list is more than 1 long
        mid = len(alist)//2     #get the midpoint of the list
        lefthalf = alist[:mid]  #everything left of but not including the midpoint
        righthalf = alist[mid:] #everything right of and including the midpoint

        mergeSort(lefthalf)     #recursive call of the function until it is one list item
        mergeSort(righthalf)    #recursive call of the function until it is one list item


        #when the single list is returned from the function these lines are run
        i=0             #pointer associated with the index in the lefthalf list
        j=0             #pointer associated with the index in the righthalf list
        k=0             #pointer associated with the alist we are modifying/sorting/merging

        print "lefthalf=",lefthalf, "righthalf=",righthalf
        while i < len(lefthalf) and j < len(righthalf):     #while i and j are both < list length do this
            
            print "i=",i, "j=",j, "k=",k
            if lefthalf[i] < righthalf[j]:                      #if value of lefthalf is < value of righthalf
           
                alist[k] = lefthalf[i]                              #set lefthalf value as the new value at index k in alist
                
                i = i + 1                                           #increase i by 1 so we move the pointer to the right in lefthalf list
           
            else:
                alist[k] = righthalf[j]                         #if value of righthalf is less, set it in alist at index k 
                
                j = j + 1                                           #and move the pointer to the right in righthalf
           
            k = k + 1                                           #since a value has been set, move the alist pointer to the next element to be replaced

        while i < len(lefthalf):                            #while i < length of lefthalf list
            print "i=",i, "k=",k
            alist[k] = lefthalf[i]                              #set lefthalf value as new value at index k in alist.
            
            i = i + 1                                           #move pointer in lefthalf list to the right
            k = k + 1                                           #move pointer in alist to the right

        while j < len(righthalf):                           #while j < length of righthalf list
            print "j=",j,"k=",k
            alist[k] = righthalf[j]                             #set righthalf value as new value at index k in alist.
            
            j = j + 1                                           #move pointer in righthalf list to the right
            k = k + 1                                           #move pointer in alist to the right    
    
    print "returned from function", alist                #if length of the list is 1 or less, return the list

alist = [54,26,93,17,77,31,44,55,20]
mergeSort(alist)
print(alist)
