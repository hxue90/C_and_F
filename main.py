def printTmp(a, b, c):
    print("| C  | F   |")
    for i in range(a, b+1, c):
        fahrenhiet = str(int((i*(9/5)+32)))
        print("| %-3s| %-3s |" % (str(i), fahrenhiet))

def main():
    printTmp(0, 100, 5)

if __name__ == "__main__":
    main()