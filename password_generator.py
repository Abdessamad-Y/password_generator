import string
import random


#generating lists of all the charcters neeeded to generate the password
letters = list(string.ascii_lowercase)

numbers = list(string.digits)

special_characters = list("!@#$%^&*()")

char_list = list(letters+numbers+special_characters)

random.seed(2)

random.shuffle(char_list)

#create a random password
length_of_the_password = int(input("how long you want the password:"))
password = []
for _ in range(length_of_the_password):
    password.append(random.choice(char_list))

password_suggested="".join([str(item)for item in password])
print(password_suggested)

#save the password in a file .txt
f=open("password.txt","w+")
f.write(password_suggested)
f.close()