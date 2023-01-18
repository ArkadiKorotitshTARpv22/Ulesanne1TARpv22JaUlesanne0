#1 Ülesanne 1 kasutades "While"
print("---------------------------------------------------------")#eraldamine
N=input("Palun sisesta oma nimi: ")
k=float(input("Mitu korda soovite, et teid tervitataks? "))
x=1
while x < k+1:
    print("Ole tervitatud,",N,x,".korda.")
    x=x+1

#2 Ülesanne 1 kasutades "While True"
print("---------------------------------------------------------")
M=input("Palun sisesta oma nimi: ")
l=float(input("Mitu korda soovite, et teid tervitataks? "))
z=1
while True:
    print("Ole tervitatud,",M,z,".korda.")
    z=z+1
    if z==l+1: 
        break

#3 Ülesanne 1 kasutades "For"
print("---------------------------------------------------------")
B=input("Palun sisesta oma nimi: ")
j=float(input("Mitu korda soovite, et teid tervitataks? "))
y=j+1
for i in range(int(y)):
    print("Ole tervitatud,",B,i,".korda.")

#4 Ülesanne 1 kasutades "While" ja "For"
print("---------------------------------------------------------")
V=input("Palun sisesta oma nimi: ")
f=float(input("Mitu korda soovite, et teid tervitataks? "))
t=f+1
c=1
while c in range(int(t)):
    print("Ole tervitatud,",V,c,".korda.")
    c +=1

import random

#Ülesanne 0
CG= random.randint(1,10)
gc=0
gl=3
while gc<gl:
    G = int(input('Arva ära number: '))
    gc += 1
    if G == CG:
        print('Palju õnne! Sina võitsid!')
        print('Olete kulutanud nii palju katseid:', gc)
        break
else:
    print('kahju, et kaotasid')
    print("number oli:",CG)
