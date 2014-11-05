#Sean Nicholls
#iteration rev ex3

total = 0 
count = 0
averager = int(input("How many numbers am I going to average: "))
while count in range(averager):
    count = (count+1)
    number = int(input("Please enter number {0} in the sequence: ".format(count)))
    total = (total+number)
finaltotal = total/averager
print(finaltotal)
    
