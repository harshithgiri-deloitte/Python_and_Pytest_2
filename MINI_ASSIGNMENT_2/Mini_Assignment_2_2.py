from itertools import permutations, repeat

list1 = ["Hello ","take "]
list2 = ["Dear","Sir"]
#print(list(list(zip(r, p)) for (r, p) in zip(repeat(list1), permutations(list2))))
#list3 = [(a,b) for a in list1 for b in list2]
#print(list3)

list4 = [a + b for a in list1 for b in list2]
print(list4)
