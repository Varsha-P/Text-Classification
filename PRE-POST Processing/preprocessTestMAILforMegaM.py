def main():

    inFile = open("testtestdata.txt",'r')
    outFile = open("testMAIL.txt",'w')
    for line in inFile:
        outFile.write("1")
        z = line.split()
        for i in range(0,len(z)):
            token = z[i].split(':')
            temp1 = token[0]
            temp2 = token[1]
            outFile.write(' '+temp1+' '+temp2)
        outFile.write('\n')
    outFile.close()
if __name__=="__main__":main()
