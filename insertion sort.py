list = [4,3,9,2,123782316721,1]
def insertionSort(alist):
   for index in range(1,len(alist)):

     currentvalue = alist[index]
     position = index
     print(alist) # Optional shows progress

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue
insertionSort(list)
print(list)