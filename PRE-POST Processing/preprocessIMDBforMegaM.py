
def main():
    inputFile = open('labeledBow.feat','r')
    outputFile = open('correctDataIMDB.txt','w')
    for line in inputFile:
        z = line.split()
        if(int(z[0])>=7):
            outputFile.write("1")
        else:
            outputFile.write("0")
        for l in range (1,len(z)):
            tokens1 = z[l].split(':')
            temp = str(int(tokens1[0])+1)
            outputFile.write(" "+temp+" "+tokens1[1])
        outputFile.write('\n')      

if __name__ == "__main__":main()
