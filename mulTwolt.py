import sys
def mul(x,y):
    return x*y
if __name__=="__main__":
        print(sys.argv)
        if(len(sys.argv)==3):
                x = int(sys.argv[1])
                y = int(sys.argv[2])
                print(mul(x,y))
        elif(len(sys.argv)==2):
                print("error")
        elif(len(sys.argv)==1):
                print("error")
        else:
                print("bye bye")


