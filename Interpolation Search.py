import time
import random
seq = []

def addElement(N):
    for i in range(N):
        fig = random.randint(1,32767)
        seq.append(fig)

def Binary_Search(data, target, low , high):
    start = int(round(time.time() * 1000))
    if low > high:
        return False
    
    else:
        POS = (low + high) / 2

        if target == data[POS]:
            return True

        elif target < data[POS]:
            return Binary_Search(data, target, low, POS - 1)

        else:
            return Binary_Search(data, target, POS + 1, high)
    
    end = int(round(time.time() * 1000))
    t = end - start
    print(t)

def Interpolation_Search(Arr,a,target):

    start = int(round(time.time() * 1000))
    low = 0
    high = a - 1

    while low <= high and target >=Arr[low] and target <= Arr[high]:
        if low == high:
            if Arr[low] == target:
                return low

    POS = low + int(((high-low)*(target)-Arr[low])/(Arr[high]-Arr[low]))    

    if Arr[POS] == target:
        print("Position: " + POS)

    elif Arr[POS] < target:
        low = POS + 1

    else:
        high = POS + 1
        end = int(round(time.time() * 1000))
    t = end - start
    print(t)
    


N = 100
addElement(N)
Interpolation_Search(seq,N,4)
Binary_Search(seq, 5, 1, 32767)

N = 1000
addElement(N)
Interpolation_Search(seq,N,4)
Binary_Search(seq, 5, 1, 32767)

N = 5000
addElement(N)
Interpolation_Search(seq,N,4)
Binary_Search(seq, 5, 1, 32767)
