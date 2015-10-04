import sys
def main():
    inputFile = open(sys.argv[1],'r')
    outFile = open(sys.argv[2],'w')
    for line in inputFile:
        outFile.write("+1 ")
        z = line.split()
        for l in range (0,len(z)):
            tokens1 = z[l].split(':')
            temp = str(int(tokens1[0]))
            outFile.write(" "+temp+":"+tokens1[1])
        outFile.write('\n') 
    outFile.close()

if __name__=="__main__":main()
