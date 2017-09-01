import sys

def main ():
    n = int(sys.argv[1])
    ans = (3*(n**4)+2*(n**3)-(3*(n**2))-(2*n))/12
    print ans

if __name__ == '__main__':
    main ()
