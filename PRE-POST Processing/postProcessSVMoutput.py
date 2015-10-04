import sys

def main():
    inputFile = open(sys.argv[1],'r')
    str_file = sys.argv[2]
    for line in inputFile:
        if(float(line)>0):
            if(str_file == "SENTIMENT"):
                print("POSITIVE")
            else:
                print("SPAM")
        else:
            if(str_file == "SENTIMENT"):
                print("NEGATIVE")
            else:
                print("HAM")

if __name__=="__main__":main()
