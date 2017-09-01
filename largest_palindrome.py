import sys
import math

max_num = int(math.pow(10,int(sys.argv[1])))

def main ():
    print find_ans()

def find_ans():
    n = 0
    for i in range (max_num,0,-1):
        for j in range(i,0,-1):
            if i*j > n and is_palindrome(i*j):
                    n = i*j
    return n 

def is_palindrome(num):
    num = str(num)
    rev = num[::-1]
    return num == rev


if __name__ == '__main__':
    main()
