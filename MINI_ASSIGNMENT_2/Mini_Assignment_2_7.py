d = {'HuEx': [1, 3, 4], 'is': [7, 6], 'best': [4, 5]}
new = []
for a, b in d.items():
    new.append([a]+b)
print(new)