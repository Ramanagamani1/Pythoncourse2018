def get_hcf(list1,list2):
    res=[]
    list1.extend(list2)
    list1.sort()
    for i in range(len(list1)-1):
        if list1[i][0] == list1[i + 1][0]:
            if list1[i][1] < list1[i + 1][1]:
                res.append(list1[i])
    return res

def get_lcm(list1,list2):
    list1.extend(list2)
    list1.sort()
    for i in range(len(list1) - 2):
        if list1[i][0] == list1[i + 1][0]:
            if list1[i][1] < list1[i + 1][1]:
                list1.remove(list1[i])

    return list1

def multiply(list1,list2):
    list1.extend(list2)
    list1.sort()

    if len(list1) == 1:
        return list1

    for i in range(len(list1)-3):
        if list1[i][0] == list1[i + 1][0]:
            x = (list1[i][0], list1[i][1] + list1[i + 1][1])
            list1.remove(list1[i])
            list1.remove(list1[i])
            list1.insert(i, x)
    return list1