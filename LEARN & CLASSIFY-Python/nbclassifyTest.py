import pickle
import math
import sys
import ast

def main():
    testfile = open(sys.argv[2],'r')
    inputFile = open(sys.argv[1],"r")
    lines = inputFile.readlines()
    objects = []
    for line in lines:
        objects.append(ast.literal_eval(line))
    myDicts2 = objects[0]
    dp = myDicts2[0]
    dn = myDicts2[1]
    num_pos = 0
    num_neg = 0
    class_a_p = 0
    class_a_n = 0
    correct_a_n = 0
    correct_a_p = 0
    bel_in_pos = 0
    bel_in_neg = 0
    newDict = myDicts2[2]
    for_pos = newDict["prob_p"]
    for_neg = newDict["prob_n"]
    for line in testfile:
        p_p = math.log(for_pos)/math.log(2.718)
        p_n = math.log(for_neg)/math.log(2.718)
        tokens = line.split()
        if(tokens[0]=="POSITIVE" or tokens[0]=="HAM"):
            num_pos = num_pos + 1
        else:
            num_neg = num_neg + 1
        for i in range(1,len(tokens)):
            tokens2 = tokens[i].split(':')
            b = int(tokens2[0])
            a = int(tokens2[1])
            if(b in dn.keys()):
                cn = dn[b]
                p_n = p_n + (a*((math.log(cn)/math.log(2.718))))
                
            if(b in dp.keys()):
                cp = dp[b]
                p_p = p_p + (a*((math.log(cp)/math.log(2.718))))
            
        if(p_p > p_n):
            if(tokens[0]=="POSITIVE" or tokens[0]=="HAM"):
                correct_a_p = correct_a_p + 1
            class_a_p = class_a_p +1
        else:
            if(tokens[0]=="NEGATIVE" or tokens[0]=="SPAM"):
                correct_a_n = correct_a_n + 1
            class_a_n = class_a_n +1
    precision_pos = correct_a_p/class_a_p
    precision_neg = correct_a_n/class_a_n
    recall_pos = correct_a_p/num_pos
    recall_neg = correct_a_n/num_neg
    f1_pos = ((2*precision_pos*recall_pos)/(precision_pos+recall_pos))
    f1_neg = ((2*precision_neg*recall_neg)/(precision_neg+recall_neg))
    print(f1_pos)
    print(f1_neg)
        
if __name__ == "__main__":main()
