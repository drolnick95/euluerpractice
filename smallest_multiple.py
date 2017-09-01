def main ():
    counter = 20
    searching = True
    while searching:
        counter += 20
        searching = is_divisible(counter)
    print counter

def is_divisible(n):
    for i in range(19,10,-1):
        if n%i != 0:
            return True
    return False

if __name__ == '__main__':
    main()
