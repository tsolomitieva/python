def sumintervals(a):
 list=[]
 for i in a:
   k=len(i) #αποθηκεύει τις ενδιάμεσες τιμές κάθε διαστήματος
   for j in range(i[0],i[k-1]):
     list.append(int(j))
 print (len(set(list))); #η τιμές που επαναλαμβάνονται αφαιρούνται 
a=[]
for i in range(int(input("Δώστε αριθμό διαστημάτων: "))): #παίρνει τα στοιχεία από τον χρήστη 
    x=int(input("Δώστε αρχή διαστήματος: "))
    y=int(input("Δώστε τέλος διαστήματος: "))
    a.append((x,y)) 
sumintervals(a)
