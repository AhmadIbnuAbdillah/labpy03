from random import random
n = int(input("masukan nilai n: "))

count = 0 
while count < n:
    random_number = random()
    if random_number <0.5:
        print(f"data ke {count} = {random_number}")
        count += 1