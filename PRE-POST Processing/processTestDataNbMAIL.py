import sys
import glob
import codecs
import collections

def main():
    outputFile = open(sys.argv[1],'w')
    vocabFile = codecs.open('enron.vocab','r',encoding='utf-8',errors='ignore')
    vocabList = []
    vocabList.append("varsha")
    vocabSize = 0
    for l in vocabFile.readlines():
        l = l.rstrip('\n')
        vocabSize += 1
        vocabList.append(l)
    dp = dict()
    dn = dict()
    path = 'spam_or_ham_test'+'/*.txt'
    files1 = glob.glob(path)
    for file1 in files1:
        f1 = codecs.open(file1,"r",encoding='utf-8',errors='ignore')
        innerDict1 = dict()
        for line in f1.readlines():
            lineTokens = line.split()
            for i in lineTokens:
                ind = vocabList.index(i)
                if(ind in innerDict1.keys()):
                    innerDict1[ind] +=1 
                else:
                    innerDict1[ind] = 1
                if(ind in dp.keys()):
                    dp[ind] += 1
                else:
                    dp[ind] = 1 
        innerDictSorted = collections.OrderedDict(sorted(innerDict1.items()))
        for k, v in innerDictSorted.items(): 
            outputFile.write(str(k)+':'+str(innerDict1[k])+' ')
        outputFile.write('\n')
            
    outputFile.close() 
if __name__=="__main__":main()
