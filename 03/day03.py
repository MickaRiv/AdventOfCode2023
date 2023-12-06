import numpy as np
from collections import defaultdict

data = np.loadtxt("input",dtype="str",comments=None)

symbol_locs = [(i,j) for i,line in enumerate(data) for j,c in enumerate(line) if not c.isdigit() and c != "."]

nums = [[n for n in "".join([c if c.isdigit() else " " for c in line]).split()] for line in data]

num_neighbors = []
part_members = []
stars = defaultdict(lambda: [])
for i,(line,line_nums) in enumerate(zip(data,nums)):
    cursor = 0
    for num in line_nums:
        init = cursor + line[cursor:].find(num)
        num_neighbors.append([(row,col) for row in range(i-1,i+2) for col in range(init-1,init+len(num)+1)])
        symbol_locs_found = [loc for loc in num_neighbors[-1] if loc in symbol_locs]
        if len(symbol_locs_found):
            part_members.append(int(num))
            for sym_loc in symbol_locs_found:
                if data[sym_loc[0]][sym_loc[1]] == "*":
                    stars[sym_loc].append(int(num))
        cursor = init+len(num)
print(f"Sum of part_members: {np.sum(part_members)}")

gear_ratios = [np.prod(vals) for vals in stars.values() if len(vals)==2]
print(f"Sum of gear ratios: {np.sum(gear_ratios)}")