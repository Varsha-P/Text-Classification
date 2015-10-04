import random

def main():
    #fh = open("correctDataIMDB.txt",'r')
    fh = open("correctDataMAIL.txt",'r')
    #trainfile = open("trainIMDB75.txt",'w')
    #testfile = open("testIMDB25.txt",'w') 
    trainfile = open("trainMAIL75.txt",'w')
    testfile = open("testMAIL25.txt",'w')    
    t = []
    count = 0
    for line in fh:
        t.append(line)
        count += 1
    random.shuffle(t)
    percent = int(0.75*count)
    train_data = t[:percent]
    test_data = t[percent:]
    for d in train_data:
        trainfile.write(d)
    for d in test_data:
        testfile.write(d)
     
if __name__ == "__main__":main()
