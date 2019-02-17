num1=int(input("Δώστε αρχή διαστήματος"))
num2=int(input("Δώστε τέλος διαστήματος"))
num3=int(input("Δώστε διαφορά"))
primes=[]
for i in range(num1,num2+1,1): 
   if i!=0:
    if i==2:
        primes.append(i) #το 2 ειναι πρώτος
    else:
     x="true"
     n=int(abs(i)**(1/2)) #ψαχνω για διαιρέτη μεχρι την ριζα του αριθμού
     
     for j in range(2,n+1,1):
       if abs(i)%j==0: #ο αριθμος έχει διαιρέτη
            x="false" 
     if x=="true":
        primes.append(i) #τοποθετώ τους πρώτους αριθμούς σε μια λίστα

y="false"
for i in range(0,len(primes)):
    if y=="true":
        break
    else:
     for j in range(i,len(primes)): #ψάχνει για διαφορά στην λίστα με τους πρώτους 
      if abs(primes[i]-primes[j])==num3:
       print ("(",primes[i],",",primes[j],")") 
       y="true"
       break
if y=="false":
    print("Δέν υπάρχει τέτοιο διάστημα")
