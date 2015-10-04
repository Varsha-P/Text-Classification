import sys 

def main():
    fileType = str(sys.argv[1])
    infile = open("output6.txt",'r')
    outfile = open(sys.argv[2],'w')
    for line in infile:
        z = line.split()
        numb = int(z[0])
        if(numb==1):
            if(fileType=="SENTIMENT"):
                outfile.write("POSITIVE")
            else:
                outfile.write("SPAM")
        if(numb==0):
            if(fileType=="SENTIMENT"):
                outfile.write("NEGATIVE")
            else:
                outfile.write("HAM")
        outfile.write('\n')
    outfile.close()

if __name__=="__main__":main()
