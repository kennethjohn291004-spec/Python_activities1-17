import random
import time
import numbers

fruits = ["Apple", "Banana", "Grapes", "Avocado"]


fruit_choice = random.choice(fruits)
random_num = random.randint(1,10)
print(random_num)
time.sleep(3)
print("random_fruit", fruit_choice)