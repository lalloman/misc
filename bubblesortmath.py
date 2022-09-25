import random
numbers = []
sortednum = [1,2,3]
exiting = 0
programinfo = 'n1. clear file\n2. load data \n3. Generate random numbers in console\n4. generate random numbers \n5. EXIT\n[lease input number '
WDir = 'Users\bangs\Desktop\bubblesort'
RDir = 'Users\bangs\Desktop\bubblesort'

def numinput(numlen):
    gennumbers = []
    for i in range(numlen):
        numin = random.randint(1,100)
        gennumbers.append(numin)
    return(gennumbers)

def Bub_sort(numbers):
    templist = numbers
    numlen = len(templist)
    sorted = 0
    pos = 0
    sorts = 0
    while sorted == 0:
        for x in range(numlen-1):
            for i in range(numlen-1):
                temp1 = templist[pos]
                temp2 = templist[pos+1]
                if temp1 > temp2:
                    temptemp = temp1
                    temp1 = temp2
                    temp2 = temptemp
                    templist[pos] = temp1
                    templist[pos+1] = temp2
                pos = pos+1
                sorts = sorts+1
            pos = 0
        sorted = 1
    return(numbers)

def SConvert(inputdat):
    tempstr = '['
    for i in range(len(inputdat)-1):
        tempstr = tempstr + str(inputdat[i]) + ','
    tempstr = tempstr + str(inputdat[i+1])
    tempstr = tempstr + ']'
    return(tempstr)

def FileWrite(numbers):
    temp = SConvert(numbers)
    with open(WDir, 'a') as file:
        line ='Question ' + temp
        file.writelines([line,'\n'])
    file.close()

def FileClear():
    with open(WDir, 'w') as file:
        file.writelines('')
    print('File is cleared!')
    file.close()

def FileRLines():
    lines = 0
    with open(RDir,'rt') as file:
        for line in file:
            lines = lines + 1
    return(lines)
    file.close()

def FileRGrabber(Line):
    with open(RDir, 'rt') as file:
        reader = file.readlines()
        return(reader[Line])

def Str_List(Input):
    SynIn = Input.split()
    syninsplit = SynIn[1]
    temp = syninsplit.strip('][').split(',')
    return(temp)

print(programinfo)
while exiting != 1:
    userinput = int(input())
    if userinput in [1,2,3,4,5,6]:
        if userinput !=5:
            if userinput == 1:
                FileClear()
            elif userinput == 2:
                for i in range(FileRLines()-1):
                    print(Bub_sort(Str_List(FileRGrabber(i))))
            elif userinput == 3:
                length = int(input('how many numbers long '))
                quant = int(input('how many do you want to generate?'))
                for i in range(quant):
                    temp = numinput(length)
                    print(temp)
            elif userinput == 4:
                length = int(input('how many numbers long '))
                quant = int(input('how many do you want to generate?'))
                for i in range(quant):
                    temp = numinput(length)
                    FileWrite(temp)
                print('file written')
            print(programinfo)
        else:
            exiting = 1
    else:
        print('invalid input')
