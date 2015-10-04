import random
import sys

def main():

    inputFile = open(sys.argv[1],'r')
    outputFile = open(sys.argv[2],'w')
    percent = float(sys.argv[3])/100
    #inputFile = open('labeledBow.feat','r')
    #outputFile = open('processedDataIMDB.txt','w')
    for line in inputFile:
        z = line.split()
        if(int(z[0])>=7):
            outputFile.write("+1")
        else:
            outputFile.write("-1")
        for l in range (1,len(z)):
            tokens1 = z[l].split(':')
            temp = str(int(tokens1[0])+1)
            outputFile.write(" "+temp+":"+tokens1[1])
        outputFile.write('\n') 
    outputFile.close()
    fh = open(sys.argv[2],'r')
    trainfile = open('trainfileIMDBSVM.txt','w')
    testfile = open('testfileIMDBSVM.txt','w')
    t =[]
    count = 0
    for line in fh.readlines():
        t.append(line) 
        count += 1   
    #x = randint(0,24999)
    random.shuffle(t)
    x = int(percent*count)
    train_data = t[:x]
    test_data = t[x:]
    for d in train_data:
        trainfile.write(d)
    for d in test_data:
        testfile.write(d)   

if __name__ == "__main__":main()
