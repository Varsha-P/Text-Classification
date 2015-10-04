def main():
    inFile = open("testBow.feat",'r')
    outFile = open("testIMDB.txt",'w')
    for line in inFile:
        outFile.write("1")
        z = line.split()
        for i in range(0,len(z)):
            token = z[i].split(':')
            temp = int(token[0]) + 1
            temp2 = token[1]
            outFile.write(' ' + str(temp) + ' ' + temp2)
        outFile.write('\n')

if __name__=="__main__":main()
