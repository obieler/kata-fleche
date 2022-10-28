import sys

w = ' '
s = '*'

def print_fleche(x):
    for i in range(x*2):  
        if (i == 0):
            print("{}{}".format((x-1)*w, s))
        elif (i == x-1):
            print(((2*x)-1)*s)
        elif (i < x):
            sp_in_mid = sp_in_mid + 2 if (i > 1) else 1
            print("{}{}{}{}".format((x-(i+1))*w, s, sp_in_mid*w, s))
        else:
            print("{}{}".format((x-1)*w, s))

def main():
    n = int(sys.argv[1])
    if (n < 2 or n > 20):
        print("Entre un chiffre entre 2 et 20")
        exit(0) 
    print_fleche(n)

if __name__ == '__main__':
    main()