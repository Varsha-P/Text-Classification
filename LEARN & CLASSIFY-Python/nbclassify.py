import pickle
import math
import sys
import ast

def main():
    inputFile = open(sys.argv[1],"r")
    testfile = open(sys.argv[2],'r')
    lines = inputFile.readlines()
    objects = []
    for line in lines:
        objects.append(ast.literal_eval(line))
    myDicts2 = objects[0]
    dp = myDicts2[0]
    dn = myDicts2[1]
    newDict = myDicts2[2]
    typeOfDict = myDicts2[3]
    for_pos = newDict["prob_p"]
    for_neg = newDict["prob_n"]
    for line in testfile:
        p_p = math.log(for_pos)/math.log(2.718)
        p_n = math.log(for_neg)/math.log(2.718)
        tokens = line.split()
        for i in range(0,len(tokens)):
            tokens2 = tokens[i].split(':')
            b = int(tokens2[0]) #
            a = int(tokens2[1])
            if(b in dn.keys()):
                cn = dn[b]
                p_n = p_n + (a*((math.log(cn)/math.log(2.718))))
                
            if(b in dp.keys()):
                cp = dp[b]
                p_p = p_p + (a*((math.log(cp)/math.log(2.718))))
        if(p_p > p_n): 
            if(typeOfDict["fileType"]=="IMDB"):
                print("POSITIVE")
            else:
                print("HAM")
        else:
            if(typeOfDict["fileType"]=="IMDB"):
                print("NEGATIVE")
            else:
                print("SPAM")
        
if __name__ == "__main__":main()
