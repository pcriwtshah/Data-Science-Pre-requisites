import random
coin = [1, 2] #1 for head and 2 for tail
a = []
n = int(input("Enter the number of times you want to flip a coin\n"))
for i in range(n):
    a.append(random.choice(coin))

num_1 = a.count(1)
num_2 = a.count(2)
prob_a, prob_b = [num_1/n, num_2/n]

print(f'Number of heads = {num_1} and probability of heads = {prob_a}')
print(f'Number of tails = {num_2} and probability of tails = {prob_b}')

