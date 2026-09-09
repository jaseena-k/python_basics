#control flow
#if and elif

age=18

if age<18:
    print("not eligible")
elif age>18:
    print("eligible")  
else:
    print("hi")


#loops
#for loop
#code to be exicuted or each element in the sequence

fruits = ['banana','apple','cherry','guva']

for fruit in fruits:  #fruit is like a varible you can put anything there 
    print(fruit) #banana apple cherry guva


num = [1,2,3,4,5]

for i in num:
    print(i) # 1 2 3 4 5
    print(i*i) #square of each element

# using range      
for n in range(1,6,): # 1 2 3 4 5  you can add parameters in range fnctn (start stop and step )like(1,6,2) 
    print(n)     


#pattern

for i in range(5):
    for j in range(i):
        print("*",end=" ")
    print() 

#while loop - codeo executed as long as condition true

x = 1         #intialate
while x<6:    #condition
    print(x)  # 1 2 3 4 5 
    x=x+1     #exicute until here
