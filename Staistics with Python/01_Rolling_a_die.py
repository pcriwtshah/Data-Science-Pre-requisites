#import matplotlib
import random
die = [1, 2, 3, 4, 5, 6]
a = []
n = int(input("Enter the number of times you want to roll a die\n"))
for i in range(n):
    a.append(random.choice(die))

#print(a)

num_1 = a.count(1)
num_2 = a.count(2)
num_3 = a.count(3)
num_4 = a.count(4)
num_5 = a.count(5)
num_6 = a.count(6)

b = [num_1, num_2, num_3, num_4, num_5, num_6]
print(b)
probability = [num_1/n, num_2/n, num_3/n, num_4/n, num_5/n, num_6/n]
print(probability)
