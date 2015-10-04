import sys

def main():
    actual = open(sys.argv[1],'r')
    predicted = open(sys.argv[2],'r')
    labels = []
    num_pos = 0
    num_neg = 0
    class_a_p = 0
    class_a_n = 0
    correct_a_n = 0
    correct_a_p = 0
    for line in actual:
        z = line.split()
        labels.append(z[0])
        print(z[0])
    count = 0
    for line2 in predicted: 
        print(line2)
        l = line2.strip() 
        print(l)
        if(l=="POSITIVE" or l=="SPAM"):
            if(labels[count]=="+1"):
                num_pos += 1
                correct_a_p += 1
            class_a_p += 1
        if(l=="NEGATIVE" or l=="HAM"): 
            if(labels[count]=="-1"):
                num_neg += 1
                correct_a_n += 1
            class_a_n += 1
        count = count + 1
    precision_pos = correct_a_p/class_a_p
    precision_neg = correct_a_n/class_a_n
    recall_pos = correct_a_p/num_pos
    recall_neg = correct_a_n/num_neg
    f1_pos = ((2*precision_pos*recall_pos)/(precision_pos+recall_pos))
    f1_neg = ((2*precision_neg*recall_neg)/(precision_neg+recall_neg))
    print(f1_pos)
    print(f1_neg)      

if __name__=="__main__":main()
