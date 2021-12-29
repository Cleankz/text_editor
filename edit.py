result = ""
result_con = []
metka = len(result_con) - 1
flag = False

    
def BastShoe(command):
    global result,result_con,metka,flag
    string = command.split(" ",1)
    if int(string[0]) == 1:
        result = result + string[1]
        result_con.append(result)
        metka = len(result_con) - 1
        if flag == True:
            del result_con[0:len(result_con)-2]
            flag = False
        return result
    elif int(string[0]) == 2:
        array = list(result)
        if int(string[1]) >= len(array):
            array.clear()
            result = ''.join(array) 
            result_con.append(result)
            if flag == True:
                del result_con[0:len(result_con)-2]
                flag = False
            metka = len(result_con)
            return result
        else:
            del array[len(array)-int(string[1]):len(array)]
            if flag == True:
                result_con[len(result_con)-1] = result
                del result_con[0:len(result_con)-2]
                flag = False
            result = ''.join(array)
            result_con.append(result)
            metka = len(result_con) - 1
            return result       
    elif int(string[0]) == 3:
        if int(string[1]) <= len(result)-1:
            flag = False
            return result[int(string[1])]
        else:
            flag = False
            return ""
    elif int(string[0]) == 4:
        if len( result_con) <= 1 or len( result_con) <= 2 :
            flag = True
            result = result_con[0]
            return result_con[0]
        if metka <= 0:
            flag = True
            metka = 0
            result = result_con[0]
            return result_con[0]
            
        metka = metka - 1
        flag = True
        #result_con.append(result_con[metka])
        result = result_con[metka]
        return result_con[metka]
    elif int(string[0]) == 5:
        if metka < len(result_con) -1:
            flag = False
            metka = metka + 1
            return result_con[metka]
        else: 
            flag = False
            return result_con[len(result_con)-1]
    
    else:
         return ""