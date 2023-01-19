def hasFinalLetter (strList, letters):
    emptyList = []
    for a in strList:
        if a[-1] in letters:
            emptyList.append(a)
    return emptyList
        


strList1=['a','b','c']
strList2=['d','e','f']
strList3=['g','h','r']

f1 = hasFinalLetter(strList1,'abcdef')
print(f1)
f2 = hasFinalLetter(strList2,'abcdef')
print(f2)
f3 = hasFinalLetter(strList3,'abcdef')
print(f3)


def isDivisible (maxInt, twoInts):
    result = []
    for num in range(1,maxInt):
        if num%twoInts[0] == 0 and num%twoInts[1] ==0:
            result.append(num)
    return result

int1=(1,2)
int2=(4,3)
int3=(6,1)

ff1= isDivisible(100,int1)
print(ff1)
ff2= isDivisible(100,int2)
print(ff2)
ff3= isDivisible(0,int3)
print(ff3)
