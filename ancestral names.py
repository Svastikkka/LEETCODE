def romanToInteger(rom):

    value = {
        'M': 1000,
        'D': 500,
        'C': 100,
        'L': 50,
        'X': 10,
        'V': 5,
        'I': 1
    }
    p = 0
    ans = 0
    n = len(rom)
    for i in range(n - 1, -1, -1):

        # If greater than or equal to previous,
        # add to answer
        if value[rom[i]] >= p:
            ans += value[rom[i]]

            # If smaller than previous
        else:
            ans -= value[rom[i]]

            # Update previous
        p = value[rom[i]]

    return ans


def sortRoman(names):
    yoo = [names[sentence][0].split() for sentence in range(len(names))]
    for i in yoo:
        ans=romanToInteger(i[1])
        i.append(ans)
    n = len(yoo)
    for i in range(n - 1):
        for j in range(0, n - i - 1):
            if yoo[j][2] > yoo[j + 1][2]:
                yoo[j], yoo[j + 1] = yoo[j + 1], yoo[j]
    res=[]
    for i in yoo:
        res.append(i[0:2])
    return res









names=[["Louis IX"],["Louis VIII"],["Animal X"]]
print(sortRoman(names))