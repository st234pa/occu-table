#Shariar & Steph
#HW 2
#9/15/16
#Softdev Period 9
import random
import csv



#Make the dict
def createDict():
    data = open('occupations.csv', 'r')
    reader = csv.reader(data)
    d = {}
    occu=[]
    perc=[]
    for row in reader:
        if row[0] != 'Job Class' and  row[0] != 'Total':
            occu.append(row[0])
            perc.append(float(row[1]))
            d[row[0]]=float(row[1])
    data.close()
    return d


#adds onto a running total,
#if thet keys value makes it greater then randomnum
#it returns the key
    
def select():
    randomnum= random.random()*99.8
    total=0.00
    x=0
    print randomnum
    for key in d:
        
        total+=d[key]
        print total
        
        if randomnum<total:
            return key
        
        
     

print createDict()
#print select()


