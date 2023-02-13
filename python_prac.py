def capital_indexes(x):
    list1 = []
    for i in range(len(x)):
        if x[i].isupper():
            list1.append(i)
        else:
            pass
    return list1

x = capital_indexes("HeLlO")
print(x)