import safe
def BastShoe(command):
    string = command.split()
    if int(string[0]) == 1:
        safe.result = safe.result + string[1]
        safe.result_con.append(safe.result)
    elif int(string[0]) == 2:
        array = list(safe.result)
        if int(string[1]) >= len(array):
            array.clear()
            safe.result = ''.join(array) 
            safe.result_con.append(safe.result)
        else:
            del array[len(array)-int(string[1]):len(array)-1]
            safe.result = ''.join(array)
            safe.result_con.append(safe.result)       
    elif int(string[0]) == 3:
        if int(string[1]) <= len(safe.result)-1:
            safe.result_con.append(safe.result[int(string[1])])
            return safe.result[int(string[1])]
        else:
            return ""
        
    elif int(string[0]) == 4:
        ""
    elif int(string[0]) == 5:
        ""
    else:
        ""
    return safe.result
print(BastShoe("3 0"))
