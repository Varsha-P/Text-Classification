import sys
import random

def main():
    inputFile = open(sys.argv[1],'r')
    outputFile = open(sys.argv[2],'w')
    percent = float(sys.argv[3])/100
    for line in inputFile:
        z = line.split()
        if(z[0]=="HAM"):
            outputFile.write("-1")
        else:
            outputFile.write("+1")
        for l in range (1,len(z)):
            tokens1 = z[l].split(':')
            temp = str(int(tokens1[0]))
            outputFile.write(" "+temp+":"+tokens1[1])
        outputFile.write('\n') 
    outputFile.close()
    fh = open(sys.argv[2],'r')
    trainfile = open('trainfileMAILSVM.txt','w')
    testfile = open('testfileMAILSVM.txt','w')
    t =[]
    count = 0
    for line in fh.readlines():
        t.append(line) 
        count += 1 
    random.shuffle(t)
    x = int(percent*count)
    train_data = t[:x]
    test_data = t[x:]
    for d in train_data:
        trainfile.write(d)
    for d in test_data:
        testfile.write(d)   


if __name__=="__main__":main()
