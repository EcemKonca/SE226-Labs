from abc import ABC


class Count(ABC):
    def __init__(self, address):
        self.address = address

    def calcFreqs(self, address):
        pass


class ListCount(Count):
    def __init__(self, address):
        self.address = address

    def calcFreqs(self, address):
        file = open(address)
        x = file.readline().split()
        wordlist = []
        for i in x:
            if i not in wordlist:
                wordlist.append(i)
        for i in range(0, len(wordlist)):
            print("Frequency of", wordlist[i], "is:", x.count(wordlist[i]))


class DictCount(Count):
    def __init__(self, address):
        self.address = address

    def calcFreqs(self, address):
        file = open(address)
        y = file.readline().split()
        worddictionary = {}
        for word in y:
           worddictionary[word] = worddictionary.get(word, 0) + 1
        for key in worddictionary:
            print("{}: {}".format(key, worddictionary[key]))


address1 = "C:\\Users\\ECEM\\Desktop\\strange.txt"
listfile = ListCount(address1)
listfile.calcFreqs(address1)

address2 = "C:\\Users\\ECEM\\Desktop\\strange.txt"
dictfile = DictCount(address2)
dictfile.calcFreqs(address2)
