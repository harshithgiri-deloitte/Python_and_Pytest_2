from collections import Counter


class StringClass:
    def __init__(self,demo):
        self.demo = demo
    def list(self):
        return(list(self.demo))
    def len(self):
        return len(self.demo)


class PairsPossible(StringClass):
    def pair(self,test_list):
        res = [(x , y) for c, x in enumerate(test_list) for y in test_list[c +1:]]


class SearchCommonElements:

    def __init__(self, x, z):
        self.x = x
        self.z = z

    def common(self):
        dict1 = Counter(self.x)
        print(dict1)
        dict2 = Counter(self.z)
        common = dict1 & dict2
        common1 = list(common)
        print("Common elements : ", common1)
        return common1


class EqualSumPairs:
    def __init__(self, pairs_1):
        self.sums = []
        self.pairs_1 = pairs_1

    def notequaltosum(self):
        for pair in self.pairs_1:
            inner = [int(i) for i in pair]
            self.sums.append(sum(inner))
        nosum = []
        [nosum.append(sums) for sums in self.sums if sums not in nosum]
        print("The count of pairs who's sum is not duplicate: " + str(len(nosum)))


a = input("Enter the value: ")
b = StringClass(a)
x = "987"
print("The string converted into list is: ", b.list())
print("The length of string entered:", b.len())
c = b.list()
d = PairsPossible(b)
d.pair(c)
e = SearchCommonElements(a, x)
e.common()
f = EqualSumPairs(b.list())
f.notequaltosum()
