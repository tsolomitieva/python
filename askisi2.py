num=int(input("Δώστε αριθμό μέχρι 100000: "))
while num>100000:
 num=int(input("Δώστε αριθμό μέχρι 100000: ")) 
primes=[]
x=10**3  #αρκεί να ελέγξουμε μεχρι την ρίζα του 100000 για διαιρέτες
while num>1:
 m="false"
 for i in range(2,x):
   if  num%i==0: #αν βρούμε διαιρέτη τον αποθηκεύουμε σε λίστα
     primes.append(i)
     m="true"
     break
 if m=="false":
  primes.append(int(num))#ο αριθμός ειναι πρώτος 
  break
 x=int((num/i)**(1/2))+1 # η ρίζα του πηλίκου
 num=num/i 

i=0
while i<len(primes):
    if primes.count(primes[i])==1:
        print ("(",primes[i],")",end=" ")
        i=i+1
    else:
        print("(",primes[i],"**",primes.count(primes[i]),")",end=" ")#υψώνω σε όσες φορές υπάρχει ο διαιρέτης
        i=i+primes.count(primes[i]) #πάω στον επόμενο διαιρέτη 
