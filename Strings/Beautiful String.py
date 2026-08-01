def makeBeautiful(str):
    count1 = 0
    count2 = 0

    for i in range(len(str)):
        if i % 2 == 0:
            if str[i] != '0':
                count1 += 1
            if str[i] != '1':
                count2 += 1
        else:
            if str[i] != '1':
                count1 += 1
            if str[i] != '0':
                count2 += 1

    return min(count1, count2)
