import pickle
import sys

def main():
    trainfile = open(sys.argv[1],'r')
    outfile = open(sys.argv[2], 'w')
    p = []
    n = []
    dp = dict()
    dn = dict()
    p_count = 0   
    n_count = 0
    counter1 = 0
    numberOfLines = 0
    numberOfwordsInP = 0
    numberOfwordsInN = 0
    dpcounter = 0
    npcounter = 0
    typeOfDict = dict()
    for line in trainfile: # read train file and append positive and negative documents to lists p and n respectively
        z = line
        tokens = z.split()
        if(tokens[0]=="POSITIVE" or tokens[0]=="HAM"):
            p.append(z)
        else:
            n.append(z)
        numberOfLines = numberOfLines + 1
        if(tokens[0]=="POSITIVE" or tokens[0]=="NEGATIVE"):
            typeOfDict["fileType"] = "IMDB"
        else:
            typeOfDict["fileType"]="MAIL"
    for i in p: #calculating frequency of each word in documents labeled positive
        tokens1 = i.split()
        for k in range (1,len(tokens1)):
            token1 = tokens1[k].split(':')
            if(int(token1[0]) in dp.keys()):
                init = dp[int(token1[0])]
                dp[int(token1[0])] = int(token1[1])+init
            else:
                dp[int(token1[0])] = int(token1[1])
        p_count = p_count+1

    for key in dp.keys(): #count number of unique words in positive documents
        counter1 = counter1+1  

    counter2 = counter1 #counter2 is total number of unique words in training., ie., vocab size of training data

    for j in n: #calculating frequency of each word in documents labeled negative
        tokens2 = j.split()
        for l in range (1,len(tokens2)):
            token2 = tokens2[l].split(':')
            if(int(token2[0]) in dn.keys()):
                init2 = dn[int(token2[0])]
                dn[int(token2[0])] = int(token2[1])+init2
            else:
                dn[int(token2[0])] = int(token2[1])
        n_count = n_count+1

    for key in dp.keys(): #calculating total number of words in positive documents
        numberOfwordsInP = numberOfwordsInP + dp[key]

    for key in dn.keys(): #calculating total number of words in negative documents
        numberOfwordsInN = numberOfwordsInN + dn[key]

    for key in dn.keys(): #adding unique words in negative documents to vocab
        if(key in dp.keys()):
            counter2 = counter2
        else:
            counter2 = counter2+1

    prob_p = (p_count/numberOfLines)
    prob_n = (n_count/numberOfLines)
    newDict = {"prob_p": prob_p, "prob_n": prob_n}
    vocab_size = counter2

    for key in dp.keys():
        if(key not in dn.keys()):
            dn[key] = 0

    for key in dn.keys():
        if(key not in dp.keys()):
            dp[key] = 0

    for key in dp.keys(): #smoothing negative documents
        dpcounter = dpcounter + 1
        den = numberOfwordsInP+vocab_size
        p = (dp[key]+1)/den
        dp[key] = p
   
    for key in dn.keys(): #smoothing positive documents
        npcounter = npcounter + 1
        den2 = numberOfwordsInN+vocab_size
        p = (dn[key]+1)/den2
        dn[key] = p
    
    MyDicts = [dp,dn,newDict,typeOfDict] #list of dictionaries dp and dn
    outfile.write(str(MyDicts))
    outfile.flush()
    outfile.close()
    
if __name__ == "__main__":main()
