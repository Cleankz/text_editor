result = ""
result_con = []
metka = len(result_con) - 1
def BastShoe(command):
    global result,result_con,metka
    string = command.split(" ",1)
    if int(string[0]) == 1:
        result = result + string[1]
        result_con.append(result)
        metka = len(result_con) - 1
        print(result)
    elif int(string[0]) == 2:
        array = list(result)
        if int(string[1]) >= len(array):
            array.clear()
            result = ''.join(array) 
            result_con.append(result)
            metka = len(result_con)
            print(result)
        else:
            del array[len(array)-int(string[1]):len(array)]
            result = ''.join(array)
            result_con.append(result)
            metka = len(result_con) - 1
            print(result)       
    elif int(string[0]) == 3:
        if int(string[1]) <= len(result)-1:
            result_con.append(result[int(string[1])])
            print(result[int(string[1])])
        else:
            return ""
    elif int(string[0]) == 4:
        result_con.append(result_con[metka-1])
        metka = len(result_con) - 1
        return result_con[metka-1]
    elif int(string[0]) == 5:
        ""
    else:
        ""
print(BastShoe("1 привет"))
print(BastShoe("1 , Мир"))
print(BastShoe("1 ++"))
print(BastShoe("2 2"))
print(BastShoe("4"))
print(BastShoe("4"))
print(BastShoe("1 *"))
print(BastShoe("4"))
print(BastShoe("4"))
print(BastShoe("4"))
print(BastShoe("3 6"))