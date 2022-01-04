import random
die = []
for i in range(1, 7):
    for j in range(1, 7):
        die.append(f'{i,j}\n')

print(die)

a = []
n = int(input("Enter the number of times you want to roll two die\n"))
for i in range(n):
    a.append(random.choice(die))

#Think from here
for i in range(1, 7):
    for j in range(1, 7):
        num_(i,j) = a.count((i,j))
num_HH = a.count('HH')
num_HT = a.count('HT')
num_TH = a.count('TH')
num_TT = a.count('TT')
prob_hh, prob_ht, prob_th, prob_tt = [num_HH/n, num_HT/n, num_TH/n, num_TT/n]

print(f'Number of heads = {num_HH} and probability of heads = {prob_hh}')
print(f'Number of tails = {num_HT} and probability of tails = {prob_ht}')
print(f'Number of tails = {num_TH} and probability of tails = {prob_th}')
print(f'Number of tails = {num_TT} and probability of tails = {prob_tt}')


