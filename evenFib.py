import sys

def main ():
    x = 0
    y = 1
    z = 0
    numsum = 0
    while z < int(sys.argv[1]):
        z = x+y 
        if (z%2 == 0):
            numsum += z
        x = y
        y = z
    print numsum

if __name__ == '__main__':
    main()
