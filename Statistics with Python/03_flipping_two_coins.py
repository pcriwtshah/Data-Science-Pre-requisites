import random
coin = ['HH', 'HT', 'TH', 'TT'] #1 for head and 2 for tail
a = []
n = int(input("Enter the number of times you want to flip two coins\n"))
for i in range(n):
    a.append(random.choice(coin))

num_HH = a.count('HH')
num_HT = a.count('HT')
num_TH = a.count('TH')
num_TT = a.count('TT')
prob_hh, prob_ht, prob_th, prob_tt = [num_HH/n, num_HT/n, num_TH/n, num_TT/n]

print(f'Number of heads = {num_HH} and probability of heads = {prob_hh}')
print(f'Number of tails = {num_HT} and probability of tails = {prob_ht}')
print(f'Number of tails = {num_TH} and probability of tails = {prob_th}')
print(f'Number of tails = {num_TT} and probability of tails = {prob_tt}')


