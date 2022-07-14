result = ""
result_con = []
result_con.append(result)
metka = len(result_con) - 1
done = False # flag - done
done_1 = False # flag_1 - done_1
done_2 = False # flag_2 - done_2
def BastShoe(command):
    global result,result_con,metka,flag,flag_1,flag_2
    string = command.split(" ",1)
    if metka >= len(result_con):
        metka = len(result_con) - 1
    if int(string[0]) == 1:
        if result_con[len(result_con)-1] != result:
            result_con.append(result)
        result += string[1]
        result_con.append(result)
        if done == True:
            result_con[len(result_con)-1] = result
            del result_con[0:len(result_con)-2]
            done = False
        if done_1 == True:
            done_1 = False
        else:
            metka = len(result_con) - 1
            done_1 = False
        metka = len(result_con) - 1
        return result_con[metka]
    if len(result_con) <= 1  and len(result_con[0]) <= 1:
        return ""
    elif int(string[0]) == 2:
        metka = len(result_con) - 1
        array = list(result)
        if int(string[1]) >= len(array):
            array.clear()
            result = ''
            result_con.append(result)
            if done == True:
                del result_con[0:len(result_con)-2]
                done = False
        else:
            del array[len(array)-int(string[1]):len(array)]
            if done == True:
                result_con[len(result_con)-1] = result
                del result_con[0:len(result_con)-2]
                done = False
            result = ''.join(array)
            result_con.append(result)
            metka = len(result_con) - 1
            return result_con[metka]
        return result
    elif int(string[0]) == 3:
        if int(string[1]) <= len(result)-1:
            done = False
            done_1 = True
            return result[int(string[1])]
        else:
            done = False
            done_1 = True
            return ""
    elif int(string[0]) == 4:
        done = True
        done_2 = True
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
        result = result_con[metka]
        return result_con[metka]
    elif int(string[0]) == 5:
        if done_2 == False:
            return result
        done = False
        metka = metka + 1
        if metka >= len(result_con):
          result = result_con[len(result_con)-1]
          return result_con[len(result_con)-1]
        else:
          result = result_con[metka]
          return result_con[metka]
    else:
         return result
