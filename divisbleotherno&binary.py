# Take a list of numbers
my_list = [12, 65, 54, 39, 102, 339, 221,]

result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)


# Python program to convert decimal into other number systems
dec = 344

print("The decimal value of", dec, "is:")
print(bin(dec), "in binary.")
print(oct(dec), "in octal.")
print(hex(dec), "in hexadecimal.")
