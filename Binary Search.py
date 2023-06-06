def binary_search(list, low, up):

    status=False
    count=0
    search=int(input("Enter the value to search = "))

    while status==False and count<=up+1: #The searching should be done only up+1(10) times as there are only 10 elements in ARRAY
    
        mid=(up+low)//2

        if list[mid]==search:
            status=True
            index=mid+1
            break

        elif list[up]==search:
            status = True
            index=up+1
            break

        elif list[low] == search:
            status = True
            index=low+1
            break

        else:
            if list[mid]>search:
                up=mid
                count=count+1 #count = number of times UNSUCESSFUL ATTEMPT of searching is done

            elif list[mid]<search:
                low=mid
                count=count+1

    if status==True:
        return "Value successfully found at position " + str(index)

    else:
        msg="not found"
        return msg

list=[0,1,2,3,4,5,6,7,8,9]

low=0
up=9

abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
abc=binary_search(list,low,up)
print(abc)
