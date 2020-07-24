import random
class Deque:
    def __init__(self):
        self.array = []
        self.MaxArraySize = 20

        
    def isEmpty(self):
        if self.array == []:
            return True

        else:
            return False

    def isFull(self):
        if len(self.array) == self.MaxArraySize-1:
            return True

        else:
            return False

    def size(self):   
        return len(self.array)

    def add_to_front(self,x):
        self.array.insert(0, x)

    def add_to_back(self,x):
        self.array.append(x)

    def remove_front(self):
        if self.array == []:
            return "Nothing to remove"

        else:
            self.array.pop(0)

    def remove_back(self):
        if self.array == []:
            return "Nothing to remove"

        else:
            self.array.pop()

    

Deq = Deque()

for i in range(Deq.MaxArraySize//2):
    fig = random.randint(1,100)
    Deq.add_to_front(fig)

pro = random.uniform(0,1)
if pro > 0 and pro <= 0.1:
    a = random.randint(0,100)
    Deq.add_to_front(a)

elif pro > 0.1 and pro <= 0.3:
    Deq.remove_front()

elif pro > 0.3 and pro < 0.4:
    a = random.randint(1,100)
    Deq.add_to_back(a)

else:
    Deq.remove_back()

print("First Simulation")

print(Deq.array)
print(Deq.size())
print(Deq.isEmpty())
print(Deq.isFull())

pro2 = random.uniform(0,1)
if pro2 > 0 and pro2 <= 0.1:
    b = random.randint(0,100)
    Deq.add_to_front(b)

elif pro2 > 0.1 and pro2 <= 0.7:
    Deq.remove_front()

elif pro2 > 0.7 and pro2 <= 0.8:
    b = random.randint(1,100)
    Deq.add_to_back(b)

else:
    Deq.remove_back()

print("")
print("Second Simulation")
print(Deq.array)             
print(Deq.size())
print(Deq.isEmpty())
print(Deq.isFull())