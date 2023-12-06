import numpy as np

data = np.loadtxt("input",dtype="str")

get_calibs = lambda data: [int("".join(np.array([d for d in line if d.isdigit()])[[0,-1]])) for line in data]

calibs = get_calibs(data)
print(f"Sum of calibration values: {np.sum(calibs)}")

digits = {"one":"o1e","two":"t2o","three":"t3e","four":"f4r","five":"f5e","six":"s6x","seven":"s7n","eight":"e8t","nine":"n9e"}
data2 = data.copy()
for i,_ in enumerate(data2):
    for key,num in digits.items():
        data2[i] = data2[i].replace(key,num)
calibs2 = get_calibs(data2)
print(f"New sum of calibration values: {np.sum(calibs2)}")