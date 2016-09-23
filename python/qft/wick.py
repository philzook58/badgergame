import numpy as np

#Needs to return a list of lists of pairs
def pair(mylist):
    #Base case
    if len(mylist) == 2:
        return [[(mylist[0], mylist[1])]]
    #popoff the first element
    element1 = mylist[0]
    pairs = []
    for i in range(1,len(mylist)):
        #Pick one
        element2 = mylist[i]
        #get all the pairs expluidng the already picked pair
        subpairs = pair(mylist[1:i] + mylist[i+1:])
        #Put the picked pair back in x is a list of pairs.
        pairs = pairs + map(lambda x: [(element1,element2)] + x ,subpairs)
    return pairs

#For Fermionic pairing, it might be conveneitn to extend pairs to (element1,element2,+-1)
#With the sign depending on wheter i is even or odd

'''
pairing = pair([1,2,3,4])
print pairing
print len(pairing)
'''

#Here's an idea, I can use a and adag as objects with indices
#and return functions (two point green's functions)
# or could return matrcies that are discretized green's functions.
def contract(twoguys):
    if twoguys[0] == 'a' and twoguys[1] == 'adag':
        return 1
    else:
        return 0

#Confusing, but what
pairings = pair(['a','a','a','adag','adag','adag'])
print pairings
#could abstract out multiplication as a function passed in. Then if contraction returns functions, I could
#return a new function that multiplies the inner functions
#or could replace multiply with np.dot if returning matrices
def multiplyup(pairing):
    return reduce(lambda acc, val: acc * val,map(contract,pairing))

print sum(map(multiplyup,pairings))
