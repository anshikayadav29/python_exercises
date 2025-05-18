# Sum of natural numbers up to num

num = 16

if num < 0:
   print("Enter a positive number")
else:
   sum = 0

   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)

# Display the powers of 2 using anonymous function

terms = 10
result = list(map(lambda x: 2 ** x, range(terms)))

print("The total terms are:",terms)
for i in range(terms):
   print("2 raised to power",i,"is",result[i])
