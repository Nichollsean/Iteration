#Sean Nicholls
#iteration REV EX3
counter = 1
total = 0
amount=int(input("How many numbers would you like to average: "))
for count in range(amount):
    num=int(input("Enter number {0} for averaging: ".format(counter)))
    counter = counter + 1
    total = num + total
    average = total / amount
print ("The average is {0}".format(total))

