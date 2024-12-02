
def main():
    lst1 = []
    lst2 = []
    with open("./data.txt", 'r') as file:
        for line in file.readlines():
            nb1, nb2 = line.split()
            lst1.append(int(nb1))
            lst2.append(int(nb2))
    sum = 0
    lst1.sort()
    lst2.sort()
    for i in range(len(lst1)):
        sum += abs(lst1[i] - lst2[i])
    print(sum)
main()