import numpy as np

data = np.loadtxt("input",dtype="str",delimiter="nothing")
nums = [[np.array(numbers.split()).astype(int) for numbers in d.split(":")[1].split("|")] for d in data]
wins = [len(set(num[0]).intersection(num[1])) for num in nums]
points = [int(2**(w-1)) for w in wins]
print(f"Sum of points: {np.sum(points)}")

cards = np.ones(len(points)).astype(int)
for i,w in enumerate(wins):
    cards[i+1:i+1+w] += cards[i]
print(f"Number of cards: {np.sum(cards)}")