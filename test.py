
def mode(L):
    l=set(L)
    mode=max(l,key=L.count)
    return mode
def main():
    l=[10,20,30,40,50,10,10,10,20,20,20,20,30]
    print(mode(l))
if __name__=="__main__":
    main()


