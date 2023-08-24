def isPrimeNumber_v1 (n):
    for i in range(2, n):
        if (n % i) == 0:
            return False

        else:
            return True

def isPrimeNumber_v2 (n):
    return 0 not in map(lambda i: n % i, range(2, int(n**0.5+1)))

def writeFile(number, got, expected, fileName):
    with open(fileName, 'a') as file:
        if got == expected:
            file.write(f"{number} passed test. {expected}\n")
        else:
            file.write(f"{number} didn't pass the test, because it didnt get what was expected. Expected: {expected} Result: {int(got)}\n")


def compareResults(file1, file2):

    with open("outputv1.txt", 'w') as out1, open("outputv2.txt", 'w') as out2:
        pass

    with open(file1, 'r') as f1, open(file2, 'r') as f2:
        lines1 = f1.readlines()
        lines2 = f2.readlines()

    for i in range(len(lines1)):
        line1 = lines1[i].strip()
        line2 = lines2[i].strip()

        writeFile(int(line1),isPrimeNumber_v1(int(line1)),int(line2),"outputv1.txt")
        writeFile(int(line1),isPrimeNumber_v2(int(line1)),int(line2),"outputv2.txt")

compareResults("input.txt","expectedoutput.txt")