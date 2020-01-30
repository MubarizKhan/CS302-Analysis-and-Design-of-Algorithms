def list_evenify(list1):
    if len(list1) % 2 != 0:
        list1.insert(0, 0)
        return list1
 
    return list1

def regroup(list2):
    stlist = []
    for i in range(0, len(list2)):
        if i % 2 != 0:
            y += str(list2[i])
            stlist.append(y)
        if i % 2 == 0:
            y = str(list2[i]) 
            continue
    
    for i in range(0, len(stlist)):
        stlist[i] = int(stlist[i])

    return stlist



    

def div_conq(list1, list2):
    list_evenify(list1)
    list_evenify(list2)

    l1 = regroup(list1)
    l2 = regroup(list2)

    print(l1)
    print(l2)

    ter1 = 0

    for i in range(0,len(l1)):

        print(l1[i], "L1")
        shift = (len(l1)- i ) 
        # print(shift, "<---shift")
        # shift = 10 ** shift
        # print(shift, "<---shift")
        mulitple_1 = int(l1[i])
        # print(mulitple_1, "m1")

        for j in range(0, len(l2)):
            # print(l2[j])
            mulitple_2 = int(l2[j])
            # print(mulitple_2, "m2")
            summation = mulitple_1 * mulitple_2

            shift2 = (len(l2) - j ) 
            print(shift2, "<---shift2222")
            shift2 *= shift

            print(shift, "<--shift1")
            if shift2 != 1:

                shift2 = 10 ** shift2
                print(shift2, "<--/-shift2222")
            

                summation *= shift2
                print(summation, "<---summation")
                ter1 += summation
            else:
                # shift2 = 10 ** shift2
                print(shift2, "<--/-shift2222 In else")
            

                summation *= shift2
                print(summation, "<---summation")
                ter1 += summation


    # return ter1
    print(ter1, "ter1")
    
    # print("end")
    
    # print(l1)
    # print(l2)



list1 = [9,8,1]
list2 = [1,2,3,4]

# print( len(list1))
# list_evenify(list2)
div_conq(list1, list2)
# print(len(list1))

# hi = 12345
# hi = str(hi) 
# hi += "0"

# hi = int(hi)
# print(hi + 12)