def Merge(dict1, dict2):
    return (dict1.update(dict2))


dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}

#method1
temp = {**dict1, **dict2}
print(temp)

#method2
temp1 = dict1.copy()
temp1.update(dict2)
print(temp1)

#method3(driver function)
Merge(dict1, dict2)
print(dict1)