import numpy as np

# Filling dictionary by the weights of the amino acids
FileOfWeights = open("weight.txt")

weightsDict = {}
speclist = [0, 97, 97, 99, 101, 103, 196, 198,198, 200, 202, 295, 297, 299, 299, 301, 394, 396, 398, 400, 400, 497]
for line in FileOfWeights:
    line = line.rstrip()
    column = line.split(" ")
    weightsDict[column[0]] = int(column[1])

# input
# Len = input("Enter spetc length:  ")
# Len = int(Len)
# for i in range(0, Len):
#     speclist.append(int(input()))

# Unique, this function made to remove any duplicates in any list
def unique(list1) -> speclist:
    x = np.array(list1)
    list1 = np.unique(x)
    return list1


# Initial List, this function made to get the one mers of the input the spectrum list
def InitialList():
    initialList = []
    for key in weightsDict:
        for j in range(len(speclist)):
            if weightsDict[key] == speclist[j]:
                initialList.append(key)
    return unique(initialList)


print(InitialList())

# Extend, this function takes any k-Mers and extend it to the length of the initial list
# and give us consistent extended k-Mers

def ExtendFunction(temp):
    NewList = []
    for i in range(0, len(temp)):
        for j in range(0, len(initial_list)):
            newstring = temp[i] + initial_list[j]
            NewList.append(newstring)
    temp=[]
    for i in range(0, len(NewList)):
     if isConsistent(LinearScoring(NewList[i]),speclist):
      temp.append(NewList[i])
    return temp


# Linear Spectrum, this function calculates the linear spectrum of a protein sequence.
#and give us list of integers representing the protein’s linear spectrum.
def LinearScoring(word):
    newlist = []
    listsum = []
    for i in range(1, len(word)):
        for j in range(0, len(word) - i + 1):
            newlist.append(word[j:j + i])
    newlist.append(word)
    for h in newlist:
        sum = 0
        for o in h:
            sum += weightsDict[o]
        listsum.append(sum)
    return listsum


# Is Consistant, this function checks whether a certain	sub-peptide	is consistent with the input
#spectrum by checking if its Linear	Spectrum is	contained within the # input spectrum.
def isConsistent(num, speclist2):
    flag = False
    speclist2=speclist.copy()
    for i in range(0, len(num)):
        test=num[i]

        if test in speclist2:
            flag = True
            speclist2.remove(test)
        else:
            return False
    return flag

# Main
Fina_lList = []
initial_list = InitialList()

x = len(initial_list)
initial_list = unique(initial_list)
Fina_lList.extend(initial_list)
for j in range(0, x):
    Fina_lList = ExtendFunction(Fina_lList)
    print(Fina_lList)
    #print(len(Fina_lList))