import time
import random

seq = []


def addElement(N):
    for i in range(N):
        fig = random.randint(1, 32767)
        seq.append(fig)


def Binary_Search(data, target, low, high):
    #start = int(round(time.time() * 1000))
    # Checking base case
    if high>=low:
        POS = (low + high) // 2

        #if element is found at the middle
        if target == data[POS]:
            return True
        # If element is smaller than mid, then it can only
        # be present in left subarray
        elif  data[POS] >target:
            return Binary_Search(data, target, low, POS - 1)
        #else element would be located in the right sub array
        else:
            return Binary_Search(data, target, POS + 1, high)
    else:
        # Element is not present in the array
        return False





def Interpolation_Search(Arr, a, target):
    # Find indexs of two corners
    low = 0
    high = a - 1

    # Since array is sorted, an element present
    # in array must be in range defined by corner

    while low <= high and target >= Arr[low] and target <= Arr[high]:
        if low == high:
            if Arr[low] == target:
                return low
            return False
        POS = low + int(((float(high - low) / (Arr[high] - Arr[low])) * (target - Arr[low])))

        # target found
        if Arr[POS] == target:
            print("Position: " , POS)
            return True
        # if the target is larger , the target is in the upper part
        if Arr[POS] < target:
            low = POS + 1
        # if the target is lower , the target is in the lower part
        else:
            high = POS + 1
      #target not found
    return False



#TESTING
tArr = []

print("---Testing Binary Search---")
for i in range(5):
    start = time.time() * 1000
    N=100
    addElement(N)
    alist=sorted(seq)
    print(Binary_Search(alist,3321,0,len(alist)-1))
    end = time.time() * 1000
    t = end - start
    tArr.append(t)


Average = sum(tArr)/5
print("Average time: " , Average , " msec")
   
tArr2 = []
print("-----Testing Interpolation Search---")
for i in range(5):
    start = time.time() * 1000    
    N=100
    addElement(N)
    alist=sorted(seq)
    print(Interpolation_Search(alist,N,234))
    end = time.time() * 1000
    t = end - start
    tArr2.append(t)

Average = sum(tArr2)/5
print("Average time: " , Average , " msec")


tArr = []
print("---Testing Binary Search---")
for i in range(5):
    start = time.time() * 1000
    N=1000
    addElement(N)
    alist=sorted(seq)
    print(Binary_Search(alist,3321,0,len(alist)-1))
    end = time.time() * 1000
    t = end - start
    tArr.append(t)


Average = sum(tArr)/5
print("Average time: " , Average , " msec")
   
tArr2 = []

print("-----Testing Interpolation Search---")
for i in range(5):
    start = time.time() * 1000    
    N=1000
    addElement(N)
    alist=sorted(seq)
    print(Interpolation_Search(alist,N,234))
    end = time.time() * 1000
    t = end - start
    tArr2.append(t)

Average = sum(tArr2)/5
print("Average time: " , Average , " msec")


tArr = []
print("---Testing Binary Search---")
for i in range(5):
    start = time.time() * 1000
    N=5000
    addElement(N)
    alist=sorted(seq)
    print(Binary_Search(alist,3321,0,len(alist)-1))
    end = time.time() * 1000
    t = end - start
    tArr.append(t)


Average = sum(tArr)/5
print("Average time: " , Average , " msec")
   
tArr2 = []
print("-----Testing Interpolation Search---")
for i in range(5):
    start = time.time() * 1000    
    N=5000
    addElement(N)
    alist=sorted(seq)
    print(Interpolation_Search(alist,N,234))
    end = time.time() * 1000
    t = end - start
    tArr2.append(t)

Average = sum(tArr2)/5
print("Average time: " , Average , " msec")
