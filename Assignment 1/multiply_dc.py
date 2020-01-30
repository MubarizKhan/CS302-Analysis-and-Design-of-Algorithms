def list_evenify(list1):
    if len(list1) % 2 != 0:
        list1.insert(0, 0)
        # print(list1)
        return list1
 
    return list1


    

def div_conq(list1, list2):
    list_evenify(list1)
    list_evenify(list2)

    print(list1)
    print(list2)


    # for j in range(0, len(list2)):
    stlist = []
    for i in range(0, len(list2)):
        print(list2[i], "<--")
        # print (list2[0])
        if i % 2 != 0:
            print(i,"=", "P1")
            y += str(list2[i])
            stlist.append(y)
        if i % 2 == 0:
            y = str(list2[i]) 
            print(i,"0")
            # stlist.append(y)
            continue
    
    for i in range(0, len(stlist)):
        stlist[i] = int(stlist[i])


        print(i, "==p2", str(list2[i]))

    print(stlist,"ST")
    # print(len(list1))





list1 = [9,8,1]
list2 = [1,2,3,4,5,6,7]

# list_evenify(list2)
div_conq(list1, list2)
# print(len(list1))

# hi = 12345
# hi = str(hi) 
# hi += "0"

# hi = int(hi)
# print(hi + 12)