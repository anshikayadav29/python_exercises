# Python program to check if year is a leap year or not

year = 2000



if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))



elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))


else:
    print("{0} is not a leap year".format(year))


    # Python program to find the largest number among the three input numbers

# change the values of num1, num2 and num3
# for a different result
num1 = 10
num2 = 14
num3 = 12

# uncomment following lines to take three numbers from user


if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3

print("The largest number is", largest)
