#input number greater than 1
n = int(input("enter a number :"))

#print the numbers from n to 1
print("numbers from {0} to {1} are :".format(n,1))

#loop to print numbers
for i in range(n,0,-2):
    print(i)