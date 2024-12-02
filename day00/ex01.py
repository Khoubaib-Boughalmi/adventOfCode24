from collections import Counter
def main():
    dict1 = {}
    dict2 = {}
    with open("./data.txt", 'r') as file:
        for line in file.readlines():
            nb1, nb2 = line.split()
            if nb1 not in dict1:
                dict1[nb1] = 0
            if nb2 not in dict2:
                dict2[nb2] = 0
            dict1[nb1] += 1
            dict2[nb2] += 1

    sum = 0
    for item in dict1:
        if item in dict2:
            sum += dict2[item] * int(item)
    print(sum)
main()