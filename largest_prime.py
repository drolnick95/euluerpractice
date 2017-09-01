import sys 


def main ():
    i = 2
    num = int(sys.argv[1])
    while i * i < num:
        while num % i == 0:
            num = num / i
        i = i + 1
    print num


    
if __name__ == '__main__':
    main()
