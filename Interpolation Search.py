import time
seq = []
def Binary_Search(data, target, low , high):
    if low > high:
        return False
    
    else:
        POS = (low + high) // 2

        if target == data[POS]:
            return True

        elif target < data[POS]:
            return Binary_Search(data, target, low, POS - 1)

        else:
            return Binary_Search(data, target, POS + 1, high)
    
    t = int(round(time.time() * 1000))
    print(t)

