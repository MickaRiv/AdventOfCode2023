import numpy as np

data = np.loadtxt("input",dtype="str",delimiter=":")[:,1]
datas = [[[ddd.strip() for ddd in dd.split(",")] for dd in d.split(";")] for d in data]
datas_dict = [[{d.split()[1]:int(d.split()[0]) for d in draw} for draw in game] for game in datas]

limits = {"red":12,"green":13,"blue":14}
valids = [i+1 for i,game in enumerate(datas_dict) if np.all([num<=limits[color] for draw in game for color,num in draw.items()])]
print(f"Sum of valid IDs: {np.sum(valids)}")

powers = [np.prod([np.max([d[color] for d in game if color in d]) for color in limits]) for game in datas_dict]
print(f"Sum of powers: {np.sum(powers)}")