def maxDistance(numbers,num):
 import itertools
 result = [sum(seq) for i in range(len(numbers), 0, -1) for seq in itertools.combinations(numbers, i) if sum(seq) <= num]
 print (max(result))
numbers = []
for i in range(int(input("Δώστε μέγεθος λίστας: "))): #παίρνει την λίστα απο τον χρήστη 
    numbers.append(int(input("Δώστε στοιχείο λίστας: ")))
num=int(input("Δώστε ακέραιο: "))
maxDistance(numbers,num);
