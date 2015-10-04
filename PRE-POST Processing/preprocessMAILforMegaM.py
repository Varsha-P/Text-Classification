
def main():
    inputFile = open('inputDataMAIL.txt','r')
    outputFile = open('correctDataMAIL.txt','w')
    for line in inputFile:
        z = line.split()
        if(z[0]=="SPAM"):
            outputFile.write("1")
        else:
            outputFile.write("0")
        for l in range (1,len(z)):
            tokens1 = z[l].split(':')
            temp = str(int(tokens1[0])+1)
            outputFile.write(" "+temp+" "+tokens1[1])
        outputFile.write('\n')      

if __name__ == "__main__":main()
