# Program to check if a number is prime or not

num = 29


#num = int(input("Enter a number: "))


flag = False

if num == 0 or num == 1:
    print(num, "is not a prime number")
elif num > 1:
    # check for factors
    for i in range(2, num):
        if (num % i) == 0:
            
            flag = True
            
            break

    
    if flag:
        print(num, "is not a prime number")
    else:
        print(num, "is a prime number")


        # 2.Python program to display all the prime numbers within an interval

lower = 900
upper = 1000

print("Prime numbers between", lower, "and", upper, "are:")

for num in range(lower, upper + 1):
   
   if num > 1:
       for i in range(2, num):
           if (num % i) == 0:
               break
       else:
           print(num)