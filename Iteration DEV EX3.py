#Sean Nicholls
#21/10/14
#Iteraton DEV EX3
character = ("")
message = input("Please enter the message you want to reverse ")
length = len(message)-1
for count in range(length,-1,-1):
    reversemessage = (message[count])
    character =(character + reversemessage)
print(character)
