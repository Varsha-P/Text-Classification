import sys
import glob
import codecs
import random
import collections

def main():
    outputFile = open(sys.argv[1],'w')
    percent = float(sys.argv[2])/100
    vocabFile = codecs.open('enron.vocab','r',encoding='utf-8',errors='ignore')
    vocabList = dict()
    #vocabList.append("varsha")
    vocabSize = 0
    for l in vocabFile.readlines():
        l = l.rstrip('\n')
        vocabSize += 1
        vocabList[l] = vocabSize
    dp = dict()
    dn = dict()
    for inc in range(1,6):
        if(inc == 3):
            continue
        path = 'enron'+str(inc)+'/ham/*.txt'
        files1 = glob.glob(path)
        for file1 in files1:
            f1 = codecs.open(file1,"r",encoding='utf-8',errors='ignore')
            innerDict1 = dict()
            for line in f1.readlines():
                lineTokens = line.split()
                for i in lineTokens:
                    ind = vocabList[i]
                    if(ind in innerDict1.keys()):
                        innerDict1[ind] +=1 
                    else:
                        innerDict1[ind] = 1
                    if(ind in dp.keys()):
                        dp[ind] += 1
                    else:
                        dp[ind] = 1 
            outputFile.write('HAM')
            innerDictSorted = collections.OrderedDict(sorted(innerDict1.items()))
            for k, v in innerDictSorted.items(): 
                outputFile.write(' '+str(k)+':'+str(innerDict1[k]))
            outputFile.write('\n')
    dpo = collections.OrderedDict(sorted(dp.items()))
    #for k, v in dpo.items():
        #print(k, v)  
    for incr in range(1,6):
        if(incr == 3):
            continue
        path = 'enron'+str(incr)+'/spam/*.txt'
        files2 = glob.glob(path)
        for file2 in files2:
            f2 = codecs.open(file2,"r",encoding='utf-8',errors='ignore')
            innerDict2 = dict()
            for line in f2.readlines():
                lineTokens = line.split()
                for j in lineTokens:
                    inde = vocabList[j]
                    if(inde in innerDict2.keys()):
                        innerDict2[inde] +=1 
                    else:
                        innerDict2[inde] = 1
                    if(inde in dn.keys()):
                        dn[inde] += 1
                    else:
                        dn[inde] = 1
            outputFile.write('SPAM')
            innerDictSorted2 = collections.OrderedDict(sorted(innerDict2.items()))
            for k, v in innerDictSorted2.items(): 
                outputFile.write(' '+str(k)+':'+str(innerDict2[k]))
            outputFile.write('\n')       
    outputFile.close() 
    fh = open(sys.argv[1],'r')
    trainfile = open('trainfile.txt','w')
    testfile = open('testfile.txt','w')
    t =[]
    count = 0
    for line in fh.readlines():
        t.append(line) 
        count += 1
    print(count) 
    x = int(percent*count)
    print(x)
    #x = randint(0,24999)
    random.shuffle(t)
    train_data = t[:x]
    test_data = t[x:]
    for d in train_data:
        trainfile.write(d)
    for d in test_data:
        testfile.write(d)  
    trainfile.close()
    testfile.close()               

if __name__=="__main__":main()
