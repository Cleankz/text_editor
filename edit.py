result = ""
result_con = []
result_con.append(result)
metka = len(result_con)
flag = False
flag_1 = False
    
def BastShoe(command):
    global result,result_con,metka,flag,flag_1
    string = command.split(" ",1)
    if int(string[0]) == 1:
        result = result + string[1]
        result_con.append(result)
        if flag == True:
            result_con[len(result_con)-1] = result
            del result_con[0:len(result_con)-2]
            flag = False
        if flag_1 == True:
            flag_1 = False
        else:
            metka = len(result_con) - 1
            flag_1 = False
        return result
        
    if len(result_con) <= 1  and len(result_con[0]) <= 1:
        return ""
    elif int(string[0]) == 2:   
        array = list(result)
        result = ''.join(array) 
        result_con.append(result)
        metka = len(result_con) - 1
        if int(string[1]) >= len(array):
            array.clear()
            result = ''
            result_con.append(result)
            if flag == True:
                del result_con[0:len(result_con)-2]
                flag = False
        else:
            del array[len(array)-int(string[1]):len(array)]
            if flag == True:
                result_con[len(result_con)-1] = result
                del result_con[0:len(result_con)-2]
                flag = False
            result = ''.join(array)
            result_con.append(result)
            return result
        return result
    elif int(string[0]) == 3:
        if int(string[1]) <= len(result)-1:
            flag = False
            flag_1 = True
            return result[int(string[1])]
        else:
            flag = False
            flag_1 = True
            return ""
    elif int(string[0]) == 4:
        flag = True
        if len( result_con) <= 2 :
            result = result_con[0]
            return result_con[0]
        if metka <= 0:
            metka = len(result_con)-1
            result = result_con[0]
            return result_con[0]
        elif metka >= len(result_con):
            metka = len(result_con) - 1
        metka = metka - 1
        #result_con.append(result_con[metka])
        result = result_con[metka]
        return result_con[metka]
    elif int(string[0]) == 5:
        flag = False
        metka = metka + 1
        if metka >= len(result_con):
            return result_con[len(result_con)-1]
        else:
            return result_con[metka]
    
    else:
         return result
print(BastShoe("1 Привет"))
print(BastShoe("5"))
print(BastShoe("4"))
print(BastShoe("1 Привет"))
print(BastShoe("1 , Мир!"))
print(BastShoe("1 ++"))
print(BastShoe("4"))
print(BastShoe("5"))
print(BastShoe("4"))
print(BastShoe("5"))
print(BastShoe("5"))
print(BastShoe("4"))
print(BastShoe("4"))
print(BastShoe("3 4"))
print(BastShoe("1 рота"))
print(BastShoe("4"))
print(BastShoe("5"))